import os
import shutil
import time

# Define paths
source_dir = "/Users/zhenye/Library/Developer/CoreSimulator/Devices/A2F8031A-C996-4E92-841B-EB709AEAED31/data/Containers/Data/Application/3EDD831B-4270-439E-96DE-DFB7AA8DD65C/Documents/ExponentExperienceData/@anonymous/Aqua-6afabf59-50ad-410e-8c68-8313cc9b0e27/AquaRest/"
destination_dir = "/Users/zhenye/PycharmProjects/AqualRestBackEnd"
file_name = "sleepData.json"


# Function to check if file has been modified
def is_modified(file_path, last_modified_time):
    return os.path.getmtime(file_path) > last_modified_time


# Initial last modified time
last_modified_time = os.path.getmtime(os.path.join(source_dir, file_name))

while True:
    # Check if file has been modified
    if is_modified(os.path.join(source_dir, file_name), last_modified_time):
        # Copy the file to the destination directory
        shutil.copy(os.path.join(source_dir, file_name), destination_dir)
        print("File copied.")

        # Update last modified time
        last_modified_time = os.path.getmtime(os.path.join(source_dir, file_name))

    # Sleep for a while before checking again
    time.sleep(1)