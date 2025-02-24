import pandas as pd
import os

def load_large_csv_files(folder_path, output_file, chunk_size=100000):
    """Reads multiple large CSV files from a folder in chunks and combines them efficiently."""
    
    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
    print(f"Found {len(all_files)} CSV files in {folder_path}")

    first_file = True  # Flag to write header only once

    for file in all_files:
        print(f"Processing {file} in chunks of {chunk_size} rows...")
        for chunk in pd.read_csv(file, chunksize=chunk_size):
            chunk.to_csv(output_file, mode='a', index=False, header=first_file)
            first_file = False  # After first write, avoid writing headers again

    print(f"Combined dataset saved to {output_file}")

if __name__ == "__main__":
    input_folder = "path_to_your_csv_folder"  # Change this to your actual folder
    output_csv = "merged_data.csv"
    load_large_csv_files(input_folder, output_csv)
