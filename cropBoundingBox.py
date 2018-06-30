import cv2
import os
from xml.etree import ElementTree

'''
"D00", #ひび割れ 線状ひび割れ 縦方向 輪走行部
"D01", #ひび割れ 線状ひび割れ 縦方向 施工ジョイント部
"D02", #ひび割れ 線状ひび割れ 縦方向 施工ジョイント部やBWP等様々

"D10", #ひび割れ 線状ひび割れ 横方向 間隔が均等
"D11", #ひび割れ 線状ひび割れ 横方向 施工ジョイント部

"D20", #ひび割れ 亀甲状ひび割れ 車輪走行部
"D21", #ひび割れ 亀甲状ひび割れ 舗装面全域
"D22", #ひび割れ 亀甲状ひび割れ 部分的

"D30", #わだち掘れ わだち掘れ

"D40", #その他破損 段差
"D41", # その他破損 ポットホール
"D42", # その他破損 剥離
"D43", # その他破損 横断歩道のかすれ
"D44", # その他破損 区画線のかすれ
'''

for gov in ['adachi', 'muroran', 'chiba', 'ichihara', 'nagakute', 'matsudo', 'konan']:
    file_list = os.listdir('/Volumes/HDCA-UT/MyCityReport/FY2017/new_annotation/' + gov + '/Annotations')

    for file in file_list:

        im_name = file.split('.')[0] + '.jpg'

        full_impath = '/Volumes/HDCA-UT/MyCityReport/FY2017/new_annotation/' + gov + '/JPEGImages/' + im_name


        infile_xml = open('/Volumes/HDCA-UT/MyCityReport/FY2017/new_annotation/' + gov + '/Annotations/' + file)
        tree = ElementTree.parse(infile_xml)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls_name = obj.find('name').text
            xmlbox = obj.find('bndbox')
            xmin = int(xmlbox.find('xmin').text)
            xmax = int(xmlbox.find('xmax').text)
            ymin = int(xmlbox.find('ymin').text)
            ymax = int(xmlbox.find('ymax').text)

            if xmin>xmax:
                xmin = int(xmlbox.find('xmax').text)
                xmax = int(xmlbox.find('xmin').text)

            if ymin>ymax:
                ymin = int(xmlbox.find('ymax').text)
                ymax = int(xmlbox.find('ymin').text)

            # open image
            img = cv2.imread(full_impath)

            # crop bounding box
            roi = img[ymin:ymax, xmin:xmax]

            cv2.imwrite('/Volumes/HDCA-UT/MyCityReport/FY2018/IEEE_BigData_Paper/croppedDataset/' + cls_name + '/' + im_name, roi)
