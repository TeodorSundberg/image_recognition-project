# Call combine txt file |Combine and Download all data from txt files - create file, scryfall_input.txt
# Call get_data_scryfall |send scryfall_input.txt to scryfall api to get as many images as possible from the list including extra and alternative art and card styles, if mtg card not found go to next row, clean out and save all images in folder scryfall_test_data/images and create label files in scryfall_test_data/labels
# Call build_keras_img_mtg | use the scryfall_test_data downloaded data to train and save a keras modell that recognizes mtg images and produces a clean copy from scryfall 
# Call evaluate_keras_img_mtg | evaluate this keras model
# Call use_keras_img_mtg | sends a picture into a keras modell and get a predicted response over which image is correct and send back the name of predicted card and an image from scryfall
# call picture_from_video | if neccessary build a model that takes video and creates pictures or prepares data for yolo ingestion
# Call build_yolo_mtg | Build a yolo framework that recognizes and draws boxes if a magic card is part of a picture or video - train modell on the keras modell partly
# Call evaluate_yolo_mtg | tests the yolo modell by sending a picture into the modell and see mark which boxes are filled with magic cards
# Call use_yolo_mtg | Uses the yolo modell by sending a picture into the modell and get back the pictures of everything it identifies as a magic card
# call full model | the final part will then use the two trained models to get a video or array of pictures and then for each identified magic card it identifes in the yolo model it will send that data to the keras model to get the predicted name of the card


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
        "2": "get_data_scryfall.py",
        "3": "build_keras_img_mtg.py",
        "4": "evaluate_keras_img_mtg.py",
        "5": "use_keras_img_mtg.py",
        "6": "picture_from_video.py",
        "7": "build_yolo_mtg.py",
        "8": "evaluate_yolo_mtg.py",
        "9": "use_yolo_mtg.py",
        "10": "final_model.py"
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
