import os
import shutil

from_dir = "C:\\Users\\SESA457837\\Downloads"
to_dir = "C:/Users/SESA457837/Downloads/C102_assets-main"

list_of_files = os.listdir(from_dir)

# Move all image files from Downloads folder to another folder
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Image_Files")
        path3 = os.path.join(to_dir, "Image_Files", file_name)

        # Check if folder/directory path exists before moving
        # Else make a new folder/directory then move
        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)
