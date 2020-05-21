
'''
按照xml数据集中的object的数量来筛选数据（随机）

'''
import os
import xml.etree.ElementTree as ET
from  skimage import io
from random import random


path=r""  #xml所在地
path2=r""     #image所在地
savepath=r''    #要保存的地方
# path='./Annotations/'
mun=0
inflection_list = []
for xml_file in os.listdir(path):
    a, b = os.path.splitext(xml_file)
    tree = ET.parse(path + a + ".xml")
    root = tree.getroot()
    # for inflection_name in root.iter('object'):
    #     i=i+1
    i=random()

    if(i>0.5 and mun<=126): 
        img=io.imread(path2+a+'.jpg')
        io.imsave(savepath+a+'.jpg',img)
        mun=mun+1
        j=j+1
        print('第%g张' %mun)
        tree.write(savepath+a+'.xml',encoding='utf-8',xml_declaration=True)



