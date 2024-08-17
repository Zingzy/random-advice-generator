from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from pymongo import MongoClient
import random
from constants import MONGO_URI

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client['random-advice']


# Flask-Limiter setup
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",
)

CATEGORIES = ['creativity', 'finance', 'health_wellness', 'mindfulness', 'motivation', 'productivity', 'relationships']


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/random', methods=['GET'])
@limiter.limit("40 per minute")
def get_random_advice():
    random_category = random.choice(CATEGORIES)
    collection = db[random_category]
    advice = collection.aggregate([{ "$sample": { "size": 1 } }]).next()
    advice.pop("_id")
    advice["category"] = random_category
    return jsonify(advice)


@app.route('/random/<category>', methods=['GET'])
@limiter.limit("40 per minute")
def get_random_advice_by_category(category):
    if category not in CATEGORIES:
        return jsonify({"error": "Category not found"}), 404
    collection = db[category]
    advice = collection.aggregate([{ "$sample": { "size": 1 } }]).next()
    advice.pop("_id")
    advice["category"] = category
    return jsonify(advice)


@app.route('/categories', methods=['GET'])
@limiter.limit("40 per minute")
def get_categories():
    return jsonify({"categories": CATEGORIES, "total": len(CATEGORIES)})


@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(jsonify({"error": "ratelimit exceeded"}), 429)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")