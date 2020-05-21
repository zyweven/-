#提取目录下所有图片,更改尺寸后保存到另一目录
from PIL import Image
import os.path
import glob
width=1920
height=1080
def convertjpg(jpgfile,outdir,width=width,height=height):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
inpath=''
outpath=''
for jpgfile in glob.glob(inpath):
    convertjpg(jpgfile,outpath)
# convertjpg('/public/home/liutao/jiang/zhang/yolov3-master/yolov3-master-other/data/images',"/public/home/liutao/jiang/zhang/yolov3-master/yolov3-master-other/data/images")

