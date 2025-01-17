document.addEventListener('DOMContentLoaded', () => {
    const trendsList = document.getElementById('trends-list');
    const trendSelect = document.getElementById('trend-select');
    const generateBtn = document.getElementById('generate-btn');
    const generatedContent = document.getElementById('generated-content');

    function fetchTrends() {
        fetch('/trends')
            .then(response => response.json())
            .then(data => {
                trendsList.innerHTML = '';
                trendSelect.innerHTML = '';
                data.trends.forEach((trend, index) => {
                    const li = document.createElement('li');
                    li.textContent = trend.join(', ');
                    trendsList.appendChild(li);

                    const option = document.createElement('option');
                    option.value = index;
                    option.textContent = `Trend ${index + 1}`;
                    trendSelect.appendChild(option);
                });
            });
    }

    generateBtn.addEventListener('click', () => {
        const selectedTrend = trendsList.children[trendSelect.value].textContent;
        fetch('/generate-content', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ trend: selectedTrend }),
        })
            .then(response => response.json())
            .then(data => {
                generatedContent.innerHTML = `
                    <h3>Content Idea:</h3>
                    <p>${data.content_idea}</p>
                    <h3>Suggested Hashtags:</h3>
                    <p>${data.hashtags.join(' ')}</p>
                `;
            });
    });

    fetchTrends();
    setInterval(fetchTrends, 300000); // Refresh trends every 5 minutes
});
