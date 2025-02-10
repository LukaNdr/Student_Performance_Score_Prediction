async function predictExamScore() {
    const form = document.getElementById('predictionFormEl');
    const formData = new FormData(form);
  
    const dataObj = {};
    formData.forEach((value, key) => {
      dataObj[key] = value;
    });
  
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dataObj),
      });
  
      if (!response.ok) {
        throw new Error('Failed to fetch prediction. Please try again.');
      }
  
      const result = await response.json();
      document.getElementById('predictionResult').textContent = `ქულა: ${result.predictedScore}%`;
    } catch (error) {
      console.error(error);
      document.getElementById('predictionResult').textContent = 'დაფიქსირდა შეცდომა. სცადეთ თავიდან.';
    }
  }
  