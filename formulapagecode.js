// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware to parse JSON
app.use(bodyParser.json());

/**   
 * Function to calculate the cost of a corrugated box.
 * @param {number} length - The length of the box (in cm).
 * @param {number} width - The width of the box (in cm).
 * @param {number} height - The height of the box (in cm).
 * @param {number} costPerSquareCm - Cost per square centimeter of the material.
 * @returns {number} - Total cost of the box.
 */
function calculateBoxCost(length, width, height, costPerSquareCm) {
    // Calculate the surface area of the box (2LW + 2LH + 2WH)
    const surfaceArea = 2 * (length * width + length * height + width * height);

    // Calculate total cost
    const totalCost = surfaceArea * costPerSquareCm;
    return totalCost.toFixed(2); // Return cost rounded to 2 decimal places
}

// API endpoint to calculate the cost of the box
app.post('/calculate-box-cost', (req, res) => {
    const { length, width, height, costPerSquareCm } = req.body;

    // Validate inputs
    if (!length || !width || !height || !costPerSquareCm) {
        return res.status(400).json({
            error: 'Please provide all required fields: length, width, height, and costPerSquareCm.',
        });
    }

    if (length <= 0 || width <= 0 || height <= 0 || costPerSquareCm <= 0) {
        return res.status(400).json({
            error: 'All input values must be greater than zero.',
        });
    }

    // Calculate cost
    const cost = calculateBoxCost(length, width, height, costPerSquareCm);

    res.json({
        length,
        width,
        height,
        costPerSquareCm,
        totalCost: cost,
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
