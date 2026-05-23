import os

# Specify the directory path
directory_path = '/IIT-M'

# List contents of the directory
contents = os.listdir(directory_path)

# Print each file or folder
for item in contents:
    print(item)
