# Got a messy download folder?
# Run the script things will be more organized :D

from pathlib import Path
import os
import glob
import shutil
downloads_path = Path.home() / 'Downloads'
folder_mapping = {
    '.pptx': 'Powerpoints',
    '.ppt' : 'Powerpoints',
    '.pdf' : 'PDF',
    '.mp4' : 'Videos',
    '.mp3' : 'Videos',
    '.mkv' : 'Videos',
    '.m4a' : 'Videos',
    '.png' : 'Pictures',
    '.log' : 'Texts',
    '.txt' : 'Texts',
    '.docx': 'Texts',
    '.zip' : 'Zips',
    '.exe' : 'Installer',
    '.msi' : 'Installer'
}

# Create necessary folders if they don't exist
for folder_name in folder_mapping.values():
    folder_path = downloads_path / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

# Move files to appropriate folders
for file in glob.glob(str(downloads_path / '*.*'), recursive=True):
    file_extension = Path(file).suffix.lower()
    # print(file_extension)
    if file_extension in folder_mapping:
        target_folder = downloads_path / folder_mapping[file_extension]
        if not os.path.exists(target_folder / Path(file).name):
            shutil.move(file, target_folder)
            print(f"Moved {file} to {target_folder}")
        else:
            print(f"File {file} already exists at {target_folder}. Skipping move.")
