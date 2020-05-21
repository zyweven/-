# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:51:12 2019

@author: even zhang
给path文件夹中的.jpg文件重命名
"""
import os

class ImageRename():
    def __init__(self):
        
        self.path=r''
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            # if item.endswith('.JPG'):
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
#                dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + 'dots'+'.png')
                # dst = os.path.join(os.path.abspath(self.path), 't_' + format(str(i), '0>3s') +'.JPG')
                dst = os.path.join(os.path.abspath(self.path), 't_' + format(str(i), '0>3s') +'.jpg')
                os.rename(src, dst)
                print('converting %s to %s ...' % (src, dst))
                i = i + 1
        print('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
