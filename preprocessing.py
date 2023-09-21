import os


import os

def move_files(source_directory):
    """
    Move files from the source directory to specific target directories based on the prefix and suffix of the filenames.

    The function performs the following operations:
    1. Creates 'MDD' and 'HC' directories inside the source directory if they do not exist.
    2. Moves files from the source directory to either the 'MDD' or 'HC' directory based on the prefix of the filename.
    3. Creates 'EO', 'EC', and 'TASK' subdirectories inside both the 'MDD' and 'HC' directories if they do not exist.
    4. Moves files from the 'MDD' and 'HC' directories to the appropriate subdirectory based on the suffix of the filename.

    Parameters:
    source_directory (str): The path to the source directory containing the files to be moved.

    Exceptions:
    - Raises an exception and prints an error message if unable to list the files in the source directory.
    - Prints an error message if a file cannot be moved due to any reason (e.g., permission issues, incorrect filepath).

    Usage:
    # Replace 'your_source_directory' with the path to your source directory
    move_files('your_source_directory')
    """
    # Define the target directories
    mdd_directory = os.path.join(source_directory, "MDD")
    hc_directory = os.path.join(source_directory, "HC")

    # Create target directories if they do not exist
    os.makedirs(mdd_directory, exist_ok=True)
    os.makedirs(hc_directory, exist_ok=True)

    try:
        # List all files in the source directory
        files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]
    except Exception as e:
        print(f"Could not list files in the source directory. Error: {e}")
        return

    # Loop through all files and move them to the respective directories
    for file in files:
        try:
            if file.startswith("MDD"):
                os.rename(os.path.join(source_directory, file), os.path.join(mdd_directory, file))
            elif file.startswith("H"):
                os.rename(os.path.join(source_directory, file), os.path.join(hc_directory, file))
        except Exception as e:
            print(f"Could not move file '{file}'. Error: {e}")

    # Define and create subdirectories
    subdirs = ["EO", "EC", "TASK"]
    for subdir in subdirs:
        os.makedirs(os.path.join(mdd_directory, subdir), exist_ok=True)
        os.makedirs(os.path.join(hc_directory, subdir), exist_ok=True)

    # Move each file into a respective EO, EC, and TASK subdirectory within either MDD or HC
    mdd_files = [f for f in os.listdir(mdd_directory) if os.path.isfile(os.path.join(mdd_directory, f))]
    hc_files = [f for f in os.listdir(hc_directory) if os.path.isfile(os.path.join(hc_directory, f))]

    for file in mdd_files:
        # If file ends with "EO", move it to the EO subfolder in MDD, etc.
        if file.endswith("EO.edf"):
            os.rename(os.path.join(mdd_directory, file), os.path.join(mdd_directory, "EO", file))
        elif file.endswith("EC.edf"):
            os.rename(os.path.join(mdd_directory, file), os.path.join(mdd_directory, "EC", file))
        elif file.endswith("TASK.edf"):
            os.rename(os.path.join(mdd_directory, file), os.path.join(mdd_directory, "TASK", file))

    for file in hc_files:
        if file.endswith("EO.edf"):
            os.rename(os.path.join(hc_directory, file), os.path.join(hc_directory, "EO", file))
        elif file.endswith("EC.edf"):
            os.rename(os.path.join(hc_directory, file), os.path.join(hc_directory, "EC", file))
        elif file.endswith("TASK.edf"):
            os.rename(os.path.join(hc_directory, file), os.path.join(hc_directory, "TASK", file))



def filter():
    pass