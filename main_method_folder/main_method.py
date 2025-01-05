# Call combine txt file |Combine and Download all data from txt files - create file, scryfall_input.txt
# Call get_data_scryfall |send scryfall_input.txt to scryfall api to get as many images as possible from the list including extra and alternative art and card styles, if mtg card not found go to next row, clean out and save all images in folder scryfall_test_data/images and create label files in scryfall_test_data/labels
# Call build_keras_img_mtg | use the scryfall_test_data downloaded data to train and save a keras modell that recognizes mtg images and produces a clean copy from scryfall 
# Call prepare_augment_folders | it calls to augment the code
# Call evaluate_keras_img_mtg | evaluate this keras model
# Call use_keras_img_mtg | sends a picture into a keras model and get a predicted response over which image is correct and send back the name of predicted card and an image from scryfall

# 1,2,3, 31 prepares the data needed to train the model
# It is possible to evaluate this model with only 4, 41, 5.
# 6-10 is future extensions I would like to build, but they are too advanced for me to finish for now.
# Maybe with more time


import subprocess

def run_option(script_name, status_log):
    """Run a subprocess for the given script and update the status log."""
    try:
        # Run the script
        result = subprocess.run(["python", script_name], capture_output=True, text=True, check=True)

        # Simulated extraction of output status
        output_summary = extract_summary(result.stdout)
        print(f"\nOutput from {script_name}:")
        print(result.stdout)

        # Update status log
        status_log[script_name] = f"Ran successfully. {output_summary}"
    except subprocess.CalledProcessError as e:
        # Update status log with error
        status_log[script_name] = f"Error encountered. Details: {e.stderr}"
        print(f"Error while running {script_name}:")
        print(e.stderr)


def extract_summary(output_text):
    """Extract a summary from the subprocess output (simulated example)."""
    # This function could parse the output for specific details.
    # For example, look for 'accuracy' or summary metrics.
    # Here we simulate a summary for illustration.
    if "accuracy" in output_text.lower():
        return output_text.strip().split("\n")[-1]  # Extract the last line as a summary
    return "Output processed successfully."


def main():
    """Main method with a menu of options."""
    options = {
        "1": "combine_txt_file.py",
        "2": "get_data_scryfall.py", # should be updated to get all different versions of each image
        "3": "prepare_image_folders.py",
        "31" : "prepare_augment_folders.py", #added later to improve results
        "4": "build_keras_img_mtg.py",
        "41": "evaluate_keras_img_mtg.py",
        "5": "use_keras_img_mtg.py",
        "6": "prepare_video_folders.py", #will not be used for now
        "7": "build_yolo_mtg.py", #will not be used for now
        "8": "use_yolo_mtg.py", #will not be used for now
        "9": "Runs all 1-8 sequentially", #will not be used for now
        "10": "final_model.py" #will not be used for now, would run all previous steps 1 at the time ideally

    }

    status_log = {script: "Not run yet." for script in options.values()}

    while True:
        # Display menu
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
