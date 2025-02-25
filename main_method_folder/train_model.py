from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

def train_model(X_train, y_train, preprocessor):
    # Build the model pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    
    # Fit the model
    model.fit(X_train, y_train)
    
    return model

# Example usage
model = train_model(X_train, y_train, preprocessor)
