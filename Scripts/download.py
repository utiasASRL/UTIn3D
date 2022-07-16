#
#
#      0======================0
#      |    UTIn3D Dataset    |
#      0======================0
#
#
# ----------------------------------------------------------------------------------------------------------------------
#
#      Callable script to download the data
#
# ----------------------------------------------------------------------------------------------------------------------
#
#      Hugues THOMAS - 16/07/2022
#


# ----------------------------------------------------------------------------------------------------------------------
#
#           Imports and global variables
#       \**********************************/
#

# Common libs
import os
import gdown
import shutil


# ----------------------------------------------------------------------------------------------------------------------
#
#           Main call
#       \***************/
#


if __name__ == '__main__':


    # Links to the data
    UTIn3D_A_url = 'https://drive.google.com/drive/folders/1fCffwd_Z9v6886LzO9RmkAMGUdaqAX7t'
    UTIn3D_H_url = 'https://drive.google.com/drive/folders/1-XRsO3V5yh6iSZgznRORKP7RoKbWSi2a'

    # Path where you want your folder to be saved
    UTIn3D_A_path = 'Data/UTIn3D_A'
    UTIn3D_H_path = 'Data/UTIn3D_H'

    # Downlaod with gdown
    gdown.download_folder(UTIn3D_A_url, output=UTIn3D_A_path, quiet=True, use_cookies=False)
    gdown.download_folder(UTIn3D_H_url, output=UTIn3D_H_path, quiet=True, use_cookies=False)

    # Unzip files
    folders = ['annotated_frames', 'annotation', 'calibration', 'collisions', 'runs', 'slam_offline']
    for path in [UTIn3D_A_path, UTIn3D_H_path]:
        for folder in folders:
            folder_path = os.path.join(path, folder)
            zipfile = folder_path + '.zip'
            shutil.unpack_archive(zipfile, folder_path)




















    
    # Parameters
    roots = ['../Data/UTI3D_A', '../Data/UTI3D_H']
    folders = ['annotated_frames',
               'annotation',
               'calibration',
               'collisions',
               'runs',
               'slam_offline']

    gdrive_parents = ['1fCffwd_Z9v6886LzO9RmkAMGUdaqAX7t', '1-XRsO3V5yh6iSZgznRORKP7RoKbWSi2a']


    for root, gdrive_parent in zip(roots, gdrive_parents):

        print('\n')
        print('-------------------------------------------------------------------------')
        print('\nPreparing' + root)
        print('*********' + '*' * len(root))


        for folder in folders:

            folder_path = join(root, folder)
            print('\n    ' + folder_path)

            # First zip folder
            print('        > zipping')
            shutil.make_archive(folder_path, 'zip', folder_path)

            # Upload the zip file on google drive
            print('        > uploading')
            zip_file = folder_path + '.zip'
            os.system('gdrive upload -p {:s} {:s}'.format(gdrive_parent, zip_file))

            # Now remove the file to save space
            print('        > removing')
            if exists(zip_file):
                remove(zip_file)
    
























