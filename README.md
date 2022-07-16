

![UTIn3D Logo](/Assets/logo.jpg)

## 

![UTIn3D Mosaic](Assets/mosaic_1080p.gif)

## 

### University of Toronto Indoor 3D Dataset

This is the homepage for University of Toronto Indoor 3D Dataset (UTIn3D). A robot navigation dataset in crowded indoor environment.

It includes the lidar frames, their localization computed by our ICP based algorithm PointMap, and the labels provided by our automated annotation approach.

## 

### Download links

#### Option 1: Google Drive links


| Data | Size Compressed | Size Uncompressed | Google Drive |
| :--- | :---: | :---: | :---: |
| UTIn3D_A  | ~122GB |  ~340GB | [link](https://drive.google.com/drive/folders/1fCffwd_Z9v6886LzO9RmkAMGUdaqAX7t?usp=sharing) | 
| UTIn3D_H | ~???GB |  ~243GB | [link](https://drive.google.com/drive/folders/1-XRsO3V5yh6iSZgznRORKP7RoKbWSi2a?usp=sharing) | 


#### Option 2: Use the provided download script


TODO


#### Option 3: Dowload in your python project with gdown

First install gdown.

```
pip install --upgrade gdown
```

Then use the following lines to download the data

```python
import gdown

# Links to the data
UTIn3D_A_url = 'https://drive.google.com/drive/folders/1fCffwd_Z9v6886LzO9RmkAMGUdaqAX7t?usp=sharing'
UTIn3D_H_url = 'https://drive.google.com/drive/folders/1-XRsO3V5yh6iSZgznRORKP7RoKbWSi2a?usp=sharing'

# Downlaod with gdown
gdown.download_folder(UTIn3D_A_url, quiet=True, use_cookies=False)
gdown.download_folder(UTIn3D_H_url, quiet=True, use_cookies=False)

# # same as the above, and you can copy-and-paste a URL from Google Drive with fuzzy=True
# url = "https://drive.google.com/file/d/0B9P1L--7Wd2vNm9zMTJWOGxobkU/view?usp=sharing"
# gdown.download(url=url, output=output, quiet=False, fuzzy=True)

```

## 

### References

```
@inproceedings{thomas2021self,
  title={Self-Supervised Learning of Lidar Segmentation for Autonomous Indoor Navigation},
  author={Thomas, Hugues and Agro, Ben and Gridseth, Mona and Zhang, Jian and Barfoot, Timothy D},
  booktitle={2021 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2021},
  organization={IEEE}
}
```

```
@inproceedings{thomas2022learning,
  title={Learning Spatiotemporal Occupancy Grid Maps for Lifelong Navigation in Dynamic Scenes},
  author={Thomas, Hugues and Aurin, Matthieu Gallet de Saint and Zhang, Jian and Barfoot, Timothy D},
  booktitle={2022 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2022},
  organization={IEEE}
}
```