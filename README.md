

![UTIn3D Logo](/Assets/logo.jpg)

## 

![UTIn3D Mosaic](Assets/mosaic_1080p.gif)

## 

### University of Toronto Indoor 3D Dataset

This is the homepage for University of Toronto Indoor 3D Dataset (UTIn3D). A robot navigation dataset in crowded indoor environment.

It includes the lidar frames, their localization computed by our ICP based algorithm PointMap, and the labels provided by our automated annotation approach.

If you use your this dataset, please cite our [journal paper](https://arxiv.org/pdf/2108.10585.pdf) (TODO: Update link and bib)

```
@inproceedings{thomas2022learning,
  title={Learning Spatiotemporal Occupancy Grid Maps for Lifelong Navigation in Dynamic Scenes},
  author={Thomas, Hugues and Aurin, Matthieu Gallet de Saint and Zhang, Jian and Barfoot, Timothy D},
  booktitle={2022 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2022},
  organization={IEEE}
}
```

## 

### Download links

You can download the files and uncompress them by hand at the location of your choice.

| Data | Size Compressed | Size Uncompressed | Google Drive |
| :--- | :---: | :---: | :---: |
| UTIn3D_A  | ~122GB |  ~340GB | [link](https://drive.google.com/drive/folders/1fCffwd_Z9v6886LzO9RmkAMGUdaqAX7t?usp=sharing) | 
| UTIn3D_H | ~93GB |  ~243GB | [link](https://drive.google.com/drive/folders/1-XRsO3V5yh6iSZgznRORKP7RoKbWSi2a?usp=sharing) | 

## 

### Download with python

#### Option 1: Use the provided download script

We provide a download script that downloads and uncompress the data automatically.

First install gdown.

```
pip3 install --upgrade gdown
```

Then use the provided script:

```
cd Scripts
python3 download.py
```


#### Option 2: Download in your python project with gdown

You can inspire from our download script to dowload the data in your own projects

First install gdown.

```
pip install --upgrade gdown
```

Then use the following lines to download the data where your project needs it.

```python
import os
import gdown
import shutil

# Links to the data
UTIn3D_A_url = 'https://drive.google.com/drive/folders/1fCffwd_Z9v6886LzO9RmkAMGUdaqAX7t'
UTIn3D_H_url = 'https://drive.google.com/drive/folders/1-XRsO3V5yh6iSZgznRORKP7RoKbWSi2a'

# Path where you want your folder to be saved
UTIn3D_A_path = 'YOUR/PATH/HERE/UTIn3D_A'
UTIn3D_H_path = 'YOUR/PATH/HERE/UTIn3D_H'

# Downlaod with gdown
gdown.download_folder(UTIn3D_A_url, output=UTIn3D_A_path, quiet=False, use_cookies=False)
gdown.download_folder(UTIn3D_H_url, output=UTIn3D_H_path, quiet=False, use_cookies=False)

# Unzip files
folders = ['annotated_frames', 'annotation', 'calibration', 'collisions', 'runs', 'slam_offline']
for path in [UTIn3D_A_path, UTIn3D_H_path]:
    for folder in folders:
        folder_path = os.path.join(path, folder)
        zipfile = folder_path + '.zip'
        shutil.unpack_archive(zipfile, folder_path)
        # # Uncomment if you want he code to remove zip file automatically
        # if os.path.exists(zipfile):
        #     os.remove(zipfile)
```

## 

### References


#### Paper #1: Annotation and learning of 3D lidar point clouds

```
@inproceedings{thomas2021self,
  title={Self-Supervised Learning of Lidar Segmentation for Autonomous Indoor Navigation},
  author={Thomas, Hugues and Agro, Ben and Gridseth, Mona and Zhang, Jian and Barfoot, Timothy D},
  booktitle={2021 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2021},
  organization={IEEE}
}
```


#### Paper #2: [Annotation and learning of SOGM in simulation](https://arxiv.org/pdf/2108.10585.pdf)

```
@inproceedings{thomas2022learning,
  title={Learning Spatiotemporal Occupancy Grid Maps for Lifelong Navigation in Dynamic Scenes},
  author={Thomas, Hugues and Aurin, Matthieu Gallet de Saint and Zhang, Jian and Barfoot, Timothy D},
  booktitle={2022 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2022},
  organization={IEEE}
}


#### Paper #3: Using SOGM for navigation in simualtion and real world

```
Incoming
```