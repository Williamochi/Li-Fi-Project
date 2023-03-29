import filecmp

# Define the paths of the two files to be compared
file1_path = "code.txt"
file2_path = "code_send.txt"

# Use the filecmp.cmp() function to compare the two files
are_files_equal = filecmp.cmp(file1_path, file2_path)

# Print the result
if are_files_equal:
    print("The files are equal.")
else:
    print("The files are not equal.")
