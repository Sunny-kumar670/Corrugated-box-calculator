import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Step 2 ki tarah data load karo aur prepare karo
df = pd.read_csv("box_data.csv")
df_encoded = pd.get_dummies(df, columns=['PaperType', 'FluteType'])

X = df_encoded.drop('FinalCost', axis=1)
y = df_encoded['FinalCost']

# Train test split karo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model banao aur train karo
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction karo test set pe
y_pred = model.predict(X_test)

# Accuracy check karo
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Model save karo
joblib.dump(model, 'box_cost_model.pkl')
print("Model saved successfully as 'box_cost_model.pkl'")