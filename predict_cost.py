import joblib
import pandas as pd

# Load model
model = joblib.load('box_cost_model.pkl')

# 👇 Yeh order tumhare training ke columns ke according hona chahiye
feature_order = [
    'Length', 'Width', 'Height', 'Quantity',
    'PaperType_Duplex', 'PaperType_Kraft', 'PaperType_Testliner',
    'FluteType_B', 'FluteType_C', 'FluteType_E'
]

# Input
length = int(input("Enter Length: "))
width = int(input("Enter Width: "))
height = int(input("Enter Height: "))
quantity = int(input("Enter Quantity: "))

print("\nPaper Types: Kraft, Duplex, Testliner")
paper_type = input("Enter Paper Type: ").strip().capitalize()

print("\nFlute Types: E, B, C")
flute_type = input("Enter Flute Type: ").strip().upper()

# One-hot encode
paper_types = ['Kraft', 'Duplex', 'Testliner']
flute_types = ['E', 'B', 'C']

input_data = {
    'Length': length,
    'Width': width,
    'Height': height,
    'Quantity': quantity
}

for pt in paper_types:
    input_data[f'PaperType_{pt}'] = 1 if paper_type == pt else 0
for ft in flute_types:
    input_data[f'FluteType_{ft}'] = 1 if flute_type == ft else 0

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# ✅ Reorder columns exactly like training data
input_df = input_df[feature_order]

# Predict
predicted_per_box_cost = model.predict(input_df)[0]
total_cost = predicted_per_box_cost * quantity

print(f"\n📦 Cost per box: ₹{predicted_per_box_cost:.2f}")
print(f"✅ Total cost for {quantity} boxes: ₹{total_cost:.2f}")