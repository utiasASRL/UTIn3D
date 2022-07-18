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
    UTIn3D_A_path = '../Data/UTIn3D_A'
    UTIn3D_H_path = '../Data/UTIn3D_H'

    # Downlaod with gdown
    print('Download UTIn3D_A:')
    print('******************\n')
    gdown.download_folder(UTIn3D_A_url, output=UTIn3D_A_path, quiet=False, use_cookies=False)
    print('Download UTIn3D_H:')
    print('******************\n')
    gdown.download_folder(UTIn3D_H_url, output=UTIn3D_H_path, quiet=False, use_cookies=False)
    
    # Unzip files
    folders = ['annotated_frames', 'annotation', 'calibration', 'collisions', 'runs', 'slam_offline']
    for path in [UTIn3D_A_path, UTIn3D_H_path]:
        for folder in folders:

            # Unpack
            folder_path = os.path.join(path, folder)
            zipfile = folder_path + '.zip'
            shutil.unpack_archive(zipfile, folder_path)

            # Now remove the file to save space
            if exists(zip_file):
                remove(zip_file)













