# coding=utf-8
from os import listdir
from PIL import Image

def scan_dir(dir):
    #获取文件夹内所有图片
    image_list = []
    for fileName in listdir(dir):
        if fileName.endswith(('.JPG','.jpg','.png')):
            print(f'扫描照片: {fileName}')
            image_list.append(Image.open(f'{dir}/{fileName}'))

    total = len(image_list)
    lens =  int(pow(total, 0.5))

    return (image_list, lens, total)
