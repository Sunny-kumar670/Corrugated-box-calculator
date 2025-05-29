import pandas as pd

df = pd.read_csv("box_data.csv")
df_encoded = pd.get_dummies(df, columns=['PaperType', 'FluteType'])

X = df_encoded.drop('FinalCost', axis=1)
y = df_encoded['FinalCost']

print("✅ Data ready for ML training.")
print(X.head())