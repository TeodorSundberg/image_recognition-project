import subprocess

def run_option(script_name, status_log):
    """Run a subprocess for the given script and update the status log."""
    try:
        result = subprocess.run(["python", script_name], capture_output=True, text=True, check=True)
        output_summary = extract_summary(result.stdout)
        print(f"\nOutput from {script_name}:")
        print(result.stdout)
        status_log[script_name] = f"Ran successfully. {output_summary}"
    except subprocess.CalledProcessError as e:
        status_log[script_name] = f"Error encountered. Details: {e.stderr}"
        print(f"Error while running {script_name}:")
        print(e.stderr)

def extract_summary(output_text):
    """Extract a summary from the subprocess output."""
    if "accuracy" in output_text.lower():
        return output_text.strip().split("\n")[-1]
    return "Output processed successfully."

def main():
    """Main method with a menu of options."""
    options = {
        "1": "load_large_csv_files.py",  # Load and merge large CSV files
        "2": "clean_csv_data.py",  # Clean the dataset
        "3": "add_data_columns.py",  # Add new features
        "4": "statistical_analysis.py",  # Perform EDA & statistical analysis
        "5": "prepare_training_data.py",  # Feature engineering and transformations
        "6": "train_model.py",  # Train a machine learning model
        "7": "evaluate_model.py",  # Evaluate model performance
        "8": "predict_future.py"  # Make future predictions
    }

    status_log = {script: "Not run yet." for script in options.values()}

    while True:
        print("\nChoose an option:")
        for key, script in options.items():
            print(f"{key}: Run {script} (Status: {status_log[script]})")
        print("0: Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Exiting the program. Goodbye!")
            break
        elif choice in options:
            script_to_run = options[choice]
            print(f"Running {script_to_run}...")
            run_option(script_to_run, status_log)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
