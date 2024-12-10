import os
import json

# Compares two json files returns True if they are equal, False otherwise
# renice 20 -p $$

def are_json_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)
        return json1 == json2


def remove_duplicate_files(directory):
    # don't iterate over list of files while removing files from same list...
    files = os.listdir(directory)
    files_to_remove = []

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = os.path.join(directory, files[i])
            file2 = os.path.join(directory, files[j])

            if are_json_files_equal(file1, file2):
                print(f"Removing duplicate files: {files[i]} and {files[j]}")
                # don't remove files while iterating over list of files...
                files_to_remove.append(file2)

    # once you  have looped through all files, remove the duplicates
    for f in files_to_remove:
        os.remove(f)


if __name__ == "__main__":
    directory_path = './temp'
    print(f"Checking for duplicate files in: {directory_path}")
    remove_duplicate_files(directory_path)
    print("Duplicate files removal complete.")
