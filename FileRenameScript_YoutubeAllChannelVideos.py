import os

# print(f"{num:>03d}")
working_directory = "C:\\Users\\moham\\Desktop\\warikoo - Copy"
listing = os.walk(working_directory)

for root, directory, files in os.walk(working_directory):
    file_counter = len(files)
    print(f"Total number of files is: {file_counter}")
    if files:
        for file in files:
            split_filename = file.split('.')
            file_number = f"{file_counter:>03d}"
            # file_extn = split_filename[2]
            new_filename = file_number + '-' + split_filename[1].strip() + '.' + split_filename[2]
            src = f"{root}\\{file}"
            dst = f"{root}\\{new_filename}"
            file_counter -= 1

            os.rename(src=src, dst=dst)
