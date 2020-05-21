'''
参考 https://github.com/ShubhankarRawat/Airplane-Detection-for-Satellites/blob/master/keras_frcnn/pascal_voc_parser.py
目标检测相关
加载xml文件显示框在图片上。
需要的文件路径：
path
├─Annotations
├─images
├─ImageSets
│  └─Main
└─labels（可以不要，取决于train.txt里面的内容）
'''
import os
import cv2
from skimage import io
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
def change(a):
    a=a.replace('\\','/').replace("//",'/')
    return a
def get_data(input_path):
    all_imgs = []

    classes_count = {}

    class_mapping = {}
    visualise = False
    visualise = True

    # data_path = [os.path.join(input_path,s) for s in ['VOC2007', 'VOC2012']]

    # print(data_paths)

    data_path = input_path

    print('Parsing annotation files')

    # for data_path in data_paths:

    annot_path =change(os.path.join(data_path, 'Annotations'))
    # print(data_path)
    # imgs_path = os.path.join(data_path, 'JPEGImages')
    imgs_path = change(os.path.join(data_path, 'images'))
    # imgsets_path_trainval = change(os.path.join(data_path, 'ImageSets','Main','trainval.txt'))
    imgsets_path_test = change(os.path.join(data_path, 'ImageSets','Main','test.txt'))

    # trainval_files = []
    test_files = []
    # try:
    #     with open(imgsets_path_trainval) as f:
    #         for line in f:
    #             trainval_files.append(line.strip() + '.jpg')
    # except Exception as e:
    #     print(e)

    try:
        with open(imgsets_path_test) as f:
            for line in f:
                test_files.append(line.strip() + '.jpg')
    except Exception as e:
        if data_path[-7:] == 'VOC2012':
            # this is expected, most pascal voc distibutions dont have the test.txt file
            pass
        else:
            print(e)
    # print(os.listdir(annot_path))
    annots = [os.path.join(annot_path, s) for s in os.listdir(annot_path)]
    idx = 0
    for annot in annots:
        try:
            idx += 1
            et = ET.parse(annot)
            element = et.getroot()

            element_objs = element.findall('object')
            element_filename = element.find('filename').text

            element_width = int(element.find('size').find('width').text)
            element_height = int(element.find('size').find('height').text)

            if len(element_objs) > 0:
                annotation_data = {'filepath': os.path.join(imgs_path, element_filename), 'width': element_width,
                                    'height': element_height, 'bboxes': []}
                # print(annotation_data['filepath'])

                # if element_filename in trainval_files:
                #     annotation_data['imageset'] = 'trainval'
                # elif element_filename in test_files:
                #     annotation_data['imageset'] = 'test'
                # else:
                #     annotation_data['imageset'] = 'trainval'

            for element_obj in element_objs:
                class_name = element_obj.find('name').text
                if class_name not in classes_count:
                    classes_count[class_name] = 1
                else:
                    classes_count[class_name] += 1

                if class_name not in class_mapping:
                    class_mapping[class_name] = len(class_mapping)

                obj_bbox = element_obj.find('bndbox')
                x1 = int(round(float(obj_bbox.find('xmin').text)))
                y1 = int(round(float(obj_bbox.find('ymin').text)))
                x2 = int(round(float(obj_bbox.find('xmax').text)))
                y2 = int(round(float(obj_bbox.find('ymax').text)))
                difficulty = int(element_obj.find('difficult').text) == 1
                annotation_data['bboxes'].append(
                    {'class': class_name, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'difficult': difficulty})
            all_imgs.append(annotation_data)

            if visualise:
                # print(change(annotation_data['filepath']))
                # img = cv2.imread(annotation_data['filepath'].replace('\\','/').replace("//",'/'))
                img=io.imread(change(annotation_data['filepath']))
                for bbox in annotation_data['bboxes']:
                    cv2.rectangle(img, (bbox['x1'], bbox['y1']), (bbox[
                                    'x2'], bbox['y2']), (255, 0, 0))
                # print(img)
                # cv2.imshow('img', img)
                # cv2.waitKey(0)
                # io.imshow(img)
                # plt.ion()
                # plt.pause(0.01)
                name=element_filename.split('.')[0]
                io.imsave(name+".png",img)
                # input("Press Enter to Continue")#之后改成识别输出

        except Exception as e:
            print(e)
            continue
    return all_imgs, classes_count, class_mapping
path=r''#输入文件所在的文件夹地址

get_data(path)
