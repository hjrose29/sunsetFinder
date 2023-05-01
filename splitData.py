import os
import shutil

def split_data(directory):
    # Create subdirectories for train and valid
    train_dir = os.path.join(directory, 'train')
    valid_dir = os.path.join(directory, 'valid')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    # Get a list of all files in the directory
    files = os.listdir(directory)
    # Remove any subdirectories from the list
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    # Calculate the number of files to move to the valid directory
    valid_size = int(len(files) * 0.2)

    # Move files to the valid directory
    for i in range(valid_size):
        filename = files[i]
        src_path = os.path.join(directory, filename)
        dst_path = os.path.join(valid_dir, filename)
        shutil.move(src_path, dst_path)

    # Move remaining files to the train directory
    for i in range(valid_size, len(files)):
        filename = files[i]
        src_path = os.path.join(directory, filename)
        dst_path = os.path.join(train_dir, filename)
        shutil.move(src_path, dst_path)

import os
import random
import shutil

def move_to_temp(directory_path):
    # Create the "temp" subdirectory
    temp_dir = os.path.join(directory_path, "temp")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    # Get the list of files in the directory
    file_list = os.listdir(directory_path)

    # Shuffle the file list randomly
    random.shuffle(file_list)

    # Compute the number of files to move to "temp"
    num_files_to_move = len(file_list) // 3

    # Move the first "num_files_to_move" files to "temp"
    for filename in file_list[:num_files_to_move]:
        file_path = os.path.join(directory_path, filename)
        temp_path = os.path.join(temp_dir, filename)
        shutil.move(file_path, temp_path)

move_to_temp("/Users/henry/Documents/sunsetFinder/Data/trainNew/Non-Sunsets")