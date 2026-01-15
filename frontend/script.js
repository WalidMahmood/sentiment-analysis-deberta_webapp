document.getElementById('sentiment-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const text = document.getElementById('text-input').value;

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        // Display results
        document.getElementById('result-text').textContent = data.text;
        document.getElementById('result-class').textContent = data.class_label;

        // Probabilities
        const probs = data.probabilities;
        document.getElementById('neg-score').textContent = (probs[0] * 100).toFixed(2) + '%';
        document.getElementById('neu-score').textContent = (probs[1] * 100).toFixed(2) + '%';
        document.getElementById('pos-score').textContent = (probs[2] * 100).toFixed(2) + '%';

        // Animate bars
        document.getElementById('neg-bar').style.setProperty('--width', (probs[0] * 100) + '%');
        document.getElementById('neu-bar').style.setProperty('--width', (probs[1] * 100) + '%');
        document.getElementById('pos-bar').style.setProperty('--width', (probs[2] * 100) + '%');

        // Chart
        document.getElementById('chart').src = 'data:image/png;base64,' + data.chart;

        // Show results
        document.getElementById('results').classList.remove('hidden');

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while analyzing the sentiment. Please try again.');
    }
});