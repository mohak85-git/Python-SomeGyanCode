import os

Onedrive_Path = 'C:\\Users\\mannu\\OneDrive\\Personal Vault'
RedDrive_Path = 'J:\\'
# SilverDrive_Path = 'H:\\'
# startPath = os.curdir
# print(startPath)


def MyFunc(inp_path, save_file):

    for root, directories, files in sorted(os.walk(inp_path)):

        if ('System Volume Information' in root) or ('FOUND.000' in root):
            continue
        # print(os.path.dirname(root), file=save_file)
        # print(f"The current folder/root is {root}", file=save_file)
        # print(f'There are {len(os.listdir(root))} items in {root}',
        #       file=save_file)
        for filesAndDirs in sorted(os.listdir(root)):
            print(f'\t{filesAndDirs}', file=save_file)

#         Compare Silver Drive and OneDrive
# with open(file="C:\\Users\\moham\\Desktop\\FilesAndDirectories_OneDrive.txt",
#           mode='w', encoding="utf-8") as OneDrive, \
#         open(file="C:\\Users\\moham\\Desktop\\FilesAndDirectories_SilverDrive.txt",
#              mode='w', encoding="utf-8") as SilverDrive:

#         Compare Silver Drive and RedDrive
# with open(file="C:\\Users\\moham\\Desktop\\FilesAndDirectories_RedDrive.txt",
#           mode='w', encoding="utf-8") as RedDrive, \
#         open(file="C:\\Users\\moham\\Desktop\\FilesAndDirectories_SilverDrive.txt",
#              mode='w', encoding="utf-8") as SilverDrive:

#         Compare RedDrive and OneDrive
with open(file="C:\\Users\\mannu\\Desktop\\FilesAndDirectories_OneDrive.txt",
          mode='w', encoding="utf-8") as OneDrive, \
        open(file="C:\\Users\\mannu\\Desktop\\FilesAndDirectories_RedDrive.txt",
             mode='w', encoding="utf-8") as RedDrive:


    MyFunc(Onedrive_Path, OneDrive)
    MyFunc(RedDrive_Path, RedDrive)
    # MyFunc(SilverDrive_Path, SilverDrive)
