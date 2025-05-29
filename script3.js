function calculate() {
    const length = parseFloat(document.getElementById('length').value);
    const width = parseFloat(document.getElementById('width').value);
    const height = parseFloat(document.getElementById('height').value);
    const paperType = document.getElementById('paperType').value;
    const fluteType = document.getElementById('fluteType').value;
    const quantity = parseInt(document.getElementById('quantity').value);
  
    if (!length || !width || !height || !quantity) {
      alert("Please fill all fields.");
      return;
    }
  
    fetch('http://localhost:3000/calculate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ length, width, height, paperType, fluteType, quantity })
    })
    .then(res => res.json())
    .then(data => {
      console.log("Backend Response:", data);
      document.getElementById('result').textContent = "Total Cost: ₹" + data.totalCost;
    })
    .catch(err => {
      console.error("Error:", err);
      document.getElementById('result').textContent = "Error calculating cost.";
    });
  }