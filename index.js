// index.js

const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());

function calculateBoxRate(length, width, height, paperType, fluteType, quantity) {
    const baseRate = 0.05;
    const area = 2 * (length * width + width * height + height * length);

    let paperMultiplier = paperType === 'kraft' ? 1.2 : 1;
    let fluteMultiplier = fluteType === 'B' ? 1.1 : fluteType === 'C' ? 1.3 : 1;

    const costPerBox = baseRate * area * paperMultiplier * fluteMultiplier;
    return (costPerBox * quantity).toFixed(2);
}

app.post('/calculate', (req, res) => {
    const { length, width, height, paperType, fluteType, quantity } = req.body;

    if (!length || !width || !height || !paperType || !fluteType || !quantity) {
        return res.status(400).json({ error: 'Missing input fields' });
    }

    const totalCost = calculateBoxRate(length, width, height, paperType, fluteType, quantity);
    res.json({ totalCost });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
