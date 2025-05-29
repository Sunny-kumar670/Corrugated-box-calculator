from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('box_cost_model.pkl')

@app.route('/predict_cost', methods=['POST'])
def predict_cost():
    data = request.json  # JSON data frontend se milega

    length = int(data['length'])
    width = int(data['width'])
    height = int(data['height'])
    quantity = int(data['quantity'])
    paper_type = data['papertype'].capitalize()
    flute_type = data['flutetype'].upper()

    paper_types = ['Kraft', 'Duplex', 'Testliner']
    flute_types = ['E', 'B', 'C']

    input_data = {
        'Length': length,
        'Width': width,
        'Height': height,
        'Quantity': quantity,
    }
    for pt in paper_types:
        input_data[f'PaperType_{pt}'] = 1 if paper_type == pt else 0
    for ft in flute_types:
        input_data[f'FluteType_{ft}'] = 1 if flute_type == ft else 0

    feature_order = [
        'Length', 'Width', 'Height', 'Quantity',
        'PaperType_Duplex', 'PaperType_Kraft', 'PaperType_Testliner',
        'FluteType_B', 'FluteType_C', 'FluteType_E'
    ]
    input_df = pd.DataFrame([input_data])[feature_order]
    per_box_cost = model.predict(input_df)[0]
    total_cost = per_box_cost * quantity

    return jsonify({'total_cost': round(total_cost, 2)})

if __name__ == "__main__":
    app.run(debug=True)