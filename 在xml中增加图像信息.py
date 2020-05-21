'''
在xml中增加图像信息
'''
from xml.etree.ElementTree import ElementTree,Element
import xml.etree.ElementTree as ET
import os
from skimage import io
path=r''#原始xml文件所在位置
path2=r''#图片所在位置
path3=r''#增加了信息的xml所在位置
for xml_file in os.listdir(path):
    a, b = os.path.splitext(xml_file)
    tree = ET.parse(path + a + ".xml")
    root = tree.getroot()
    savepath=path3 + a + ".xml"
    imgpath=path2+a+'.jpg'
    # path=r'D:\Document And Settings2\张译文\Desktop\水下\train\train\box\000001.xml'
    # tree = ET.parse(path)
    # root = tree.getroot()
    img=io.imread(imgpath)
    element=Element("size")
    w=Element('width')
    w.text=str(img.shape[1])
    h=Element('height')
    h.text=str(img.shape[0])
    element.append(w)
    element.append(h)
    root.append(element)
    tree.write(savepath,encoding='utf-8',xml_declaration=True)