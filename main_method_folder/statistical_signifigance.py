from sklearn.feature_selection import SelectKBest, f_regression

X = df.drop(columns=["target_column"])
y = df["target_column"]

selector = SelectKBest(score_func=f_regression, k=5)  # Select top 5 features
selector.fit(X, y)
selected_features = X.columns[selector.get_support()]
print("Top features:", selected_features)
