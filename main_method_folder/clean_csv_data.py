import pandas as pd

def clean_csv_data(input_file, output_file):
    """Cleans the dataset by handling missing values, removing duplicates, and standardizing column names."""
    
    # Load data
    df = pd.read_csv(input_file)
    print(f"Original dataset: {df.shape[0]} rows, {df.shape[1]} columns")

    # Standardize column names (lowercase and replace spaces with underscores)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Drop duplicates
    df = df.drop_duplicates()
    print(f"After removing duplicates: {df.shape[0]} rows")

    # Handle missing values (fill numeric columns with median, categorical with mode)
    for col in df.columns:
        if df[col].dtype == 'object':  # Categorical columns
            df[col] = df[col].fillna(df[col].mode()[0])
        else:  # Numeric columns
            df[col] = df[col].fillna(df[col].median())

    print(f"After handling missing values: {df.isnull().sum().sum()} missing values left")

    # Save cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    input_csv = "raw_data.csv"  # Change to your actual file
    output_csv = "cleaned_data.csv"
    clean_csv_data(input_csv, output_csv)
