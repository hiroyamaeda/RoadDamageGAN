import cv2
import os
import numpy as np

basePath = '/Volumes/HDCA-UT/MyCityReport/FY2018/IEEE_BigData_Paper/croppedDataset/'

cls_name = os.listdir(basePath)

sizeCount = []

for cls in cls_name:

    file_list = os.listdir(basePath + cls)
    file_list.remove(".DS_Store")

    for file in file_list:

        # open image
        img = cv2.imread(basePath + cls + '/' + file)

        sizeCount.append(img.shape[0:2])

sizeCount = np.array(sizeCount)
print(np.average(sizeCount, axis=0))

