def predict_future(model, future_data):
    # Preprocess and predict using the trained model
    predictions = model.predict(future_data)
    
    return predictions

# Example usage
future_data = pd.DataFrame()  # New data here
future_predictions = predict_future(model, future_data)
print("Future Predictions:", future_predictions)
