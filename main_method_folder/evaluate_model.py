
import pandas as pd
import joblib  # For loading the trained model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load test data
test_data = pd.read_csv("test_data.csv")  # Replace with actual test dataset path
X_test = test_data.drop(columns=["target"])  # Adjust based on actual target column
y_test = test_data["target"]

# Load trained model
model = joblib.load("trained_model.pkl")  # Replace with actual model path

# Generate predictions
y_pred = model.predict(X_test)

# Evaluate performance
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"Model Evaluation:\nR² Score: {r2:.4f}\nRMSE: {rmse:.4f}\nMAE: {mae:.4f}")

# Plot Actual vs. Predicted
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs. Predicted Sales")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')  # 1:1 line
plt.show()


'''from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test):
    # Predict the values
    y_pred = model.predict(X_test)
    
    # Calculate evaluation metrics
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    print(f"Root Mean Squared Error (RMSE): {rmse}")
    print(f"R-squared: {r2}")

    # Visualize the predictions vs actual values
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values')
    plt.show()

# Example usage
evaluate_model(model, X_test, y_test)
'''