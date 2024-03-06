from my_module.data_processing import merge_csv
from my_module.logging import run_all_files
import os
import shutil

def main():
    folder_path = r"C:\Users\Ariake\Desktop\20240304\AP-FOLDER\AP"
    target_folder = r"C:\Users\Ariake\Desktop\full-02"

    run_all_files(folder_path)

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Get a list of CSV files in the source folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

    # Move each CSV file to the target folder
    for csv_file in csv_files:
        source_filepath = os.path.join(folder_path, csv_file)
        target_filepath = os.path.join(target_folder, csv_file)
        shutil.move(source_filepath, target_filepath)

    merge_csv(target_folder)

if __name__ == "__main__":
    main()
