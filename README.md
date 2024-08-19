# Random Advice Generator 🎲

Welcome to the Random Advice Generator! This project provides random pieces of advice across various categories to inspire and motivate you.

## Features 🌟

- **Random Advice**: Get a random piece of advice from a variety of categories.
- **Category-Specific Advice**: Fetch advice from specific categories such as creativity, finance, health & wellness, mindfulness, motivation, productivity, and relationships.
- **Rate Limiting**: Prevents abuse by limiting the number of requests per minute.
- **Voice Synthesis**: Reads out the advice using the Web Speech API.

## Categories 📚

The available categories are:
- Creativity
- Finance
- Health & Wellness
- Mindfulness
- Motivation
- Productivity
- Relationships

## Installation 🛠️

### Prerequisites

- Python 3.x
- Flask
- MongoDB

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/zingzy/random-advice-generator.git
    cd random-advice-generator
    ```

2. Install backend dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables:
    ```bash
    mv .env.example .env
    ```

4. Update the `.env` file with your MongoDB URI and other configuration settings.

5. Run the application:
    ```bash
    python main.py
    ```

## Usage 🚀

1. Open your browser and navigate to `http://localhost:5000`.
2. Click on the "Get Advice" button to fetch a random piece of advice.
3. To get advice from a specific category, click on the "Select Category" dropdown and choose the desired category.

## API Endpoints 🌐

### Get Random Advice

- **Endpoint**: `/random`
- **Method**: `GET`
- **Description**: Fetches a random piece of advice from any category.
- **Rate Limit**: 20 requests per minute

### Get Random Advice by Category

- **Endpoint**: `/random/<category>`
- **Method**: `GET`
- **Description**: Fetches a random piece of advice from the specified category.
- **Rate Limit**: 20 requests per minute

### Get Categories

- **Endpoint**: `/categories`
- **Method**: `GET`
- **Description**: Returns a list of all available categories.
- **Rate Limit**: 20 requests per minute

## Example Usage with cURL

### Fetch Random Advice

```sh
curl http://localhost:5000/random
```

### Fetch Random Advice by Category

```sh
curl http://localhost:5000/random/motivation
```

### Fetch Categories

```sh
curl http://localhost:5000/categories
```

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact 📧

For any questions or feedback, please contact us at [admin@spoo.me](mailto:admin@spoo.me).