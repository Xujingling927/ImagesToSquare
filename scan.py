# coding=utf-8
import re
from os import listdir
from PIL import Image
from tqdm import tqdm
def scan_dir(dir):
    
    #获取文件夹内所有图片
    image_list = []
    dirs = listdir(dir)
    for file_name in tqdm(dirs):
        if bool(re.search(r'\.(png|jpg|jpeg)$', file_name, re.IGNORECASE)):
            image_list.append(Image.open(f'{dir}/{file_name}'))

    total = len(image_list)
    lens =  int(pow(total, 0.5))

    return (image_list, lens, total)
