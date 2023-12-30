# Backup Script
# Uses shutil library for file operations

import shutil
import datetime

def backup_files(source_dir, dest_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = f"{dest_dir}/backup_{timestamp}"

    try:
        shutil.copytree(source_dir, backup_folder)
        print(f"Backup successful. Files copied to: {backup_folder}")
    except Exception as e:
        print(f"Backup failed. Error: {str(e)}")

if __name__ == "__main__":
    source_directory = "/path/to/source"
    destination_directory = "/path/to/backup"
    backup_files(source_directory, destination_directory)
