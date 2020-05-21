'''
统计xml中object的类别和数量
'''

import os
import xml.etree.ElementTree as ET



path=r''#xml文件的地址
# path='./Annotations/'
inflection_list = []
for xml_file in os.listdir(path):
    a, b = os.path.splitext(xml_file)
    tree = ET.parse(path + a + ".xml")
    root = tree.getroot()
    for inflection_name in root.iter('object'):
        target = inflection_name.find('name').text
        inflection_list.append(target)

inflection_set = set(inflection_list)

inflection_dict = {}
for i in inflection_set:
    inflection_dict[i] = inflection_list.count(i)

# print(inflection_list)
print(inflection_dict)
