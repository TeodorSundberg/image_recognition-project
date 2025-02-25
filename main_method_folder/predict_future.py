import pandas as pd
import joblib
import numpy as np

# Load last known data
latest_data = pd.read_csv("latest_data.csv")  # Replace with actual path

# Load trained model
model = joblib.load("trained_model.pkl")

# Identify companies staying, leaving, and new ones
current_companies = latest_data["company"].unique()
new_companies = ["Company_X"]  # Update dynamically
leaving_companies = ["Company_Y"]  # Update dynamically

# Filter relevant data
filtered_data = latest_data[~latest_data["company"].isin(leaving_companies)]  # Remove leaving companies

# Generate future timestamps
future_months = pd.date_range(start=latest_data["date"].max(), periods=13, freq="M")[1:]

# Generate predictions for each company
predictions = []
for company in filtered_data["company"].unique():
    company_data = filtered_data[filtered_data["company"] == company].drop(columns=["company", "date", "target"])  # Drop non-numeric
    for month in future_months:
        pred_value = model.predict(company_data.mean().values.reshape(1, -1))  # Use mean of past data
        predictions.append({"company": company, "date": month, "predicted_value": pred_value[0]})

# Convert to DataFrame and save
predictions_df = pd.DataFrame(predictions)
predictions_df.to_csv("predictions.csv", index=False)

print("Future predictions saved to predictions.csv")
