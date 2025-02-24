import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, chi2_contingency

def perform_eda(df):
    # Descriptive statistics
    print("Descriptive Statistics:\n", df.describe())

    # Correlation Matrix
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Matrix")
    plt.show()

    # Histograms for distributions
    df.hist(bins=20, figsize=(15, 10))
    plt.suptitle("Histograms of Features")
    plt.show()

    # Chi-Square Test (example between customer_type and sales_outlier)
    contingency_table = pd.crosstab(df['customer_type'], df['sales_outlier'])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    print(f"Chi-Square Test result: p-value = {p}")
    
    return corr_matrix

# Example usage
eda_results = perform_eda(df_transformed)
