document.addEventListener('DOMContentLoaded', async () => {
    const adviceBox = document.getElementById('advice-box');
    const generateBtn = document.getElementById('generate-btn');
    const categorySelect = document.getElementById('category-select');
    const readAloudBtn = document.getElementById('read-aloud-btn');
    const copyBtn = document.getElementById('copy-btn');

    // Fetch categories
    const categoriesResponse = await fetch('/categories');
    const categoriesData = await categoriesResponse.json();
    categoriesData.categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category.charAt(0).toUpperCase() + category.slice(1);
        categorySelect.appendChild(option);
    });

    // Fetch random advice
    const fetchAdvice = async () => {
        adviceBox.classList.add('loading');
        adviceBox.textContent = '';

        generateBtn.disabled = true;
        readAloudBtn.disabled = true;
        copyBtn.disabled = true;

        const category = categorySelect.value;
        const url = category === 'random' ? '/random' : `/random/${category}`;

        await new Promise(resolve => setTimeout(resolve, 500));

        const adviceResponse = await fetch(url);
        const adviceData = await adviceResponse.json();

        adviceBox.classList.remove('loading');
        adviceBox.textContent = adviceData.advice;

        generateBtn.disabled = false;
        readAloudBtn.disabled = false;
        copyBtn.disabled = false;
    };

    generateBtn.addEventListener('click', fetchAdvice);
    fetchAdvice();

    // Read Aloud functionality
    readAloudBtn.addEventListener('click', () => {
        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(adviceBox.textContent);
            speechSynthesis.speak(utterance);
        } else {
            alert('Text-to-speech is not supported in your browser.');
        }
    });

});