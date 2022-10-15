# coding=utf-8
import os
from PIL import Image
from tqdm import tqdm
from scan import scan_dir
from sort import random_sort

def main(dir):
    # 获取文件夹内所有图片
    image_list, lens, total = scan_dir(dir)
    total_max = pow(lens,2)
    print(f'总照片数: {len(image_list)}, 拼接照片宽度: {lens}')
    
    if total > total_max:
        print(f'超过当前可拼接的的最大数量，将随机选择{total_max}张照片进行拼接')
        image_list = random_sort(images_list=image_list,n=total_max)
    


    # 重新设置大小
    print('重新设置大小')
    single_size = int(4096 / lens)
    img_resize = []
    for i in tqdm(image_list):
        new_img = i.resize((single_size,single_size))
        img_resize.append(new_img)

    template = img_resize[0]
    width, height = template.size

    # 定义空白图片大小
    result = Image.new(template.mode, (width * lens, height * lens))

    # 拼接图片
    print('正在拼接')
    for i, im in enumerate(tqdm(img_resize)):
        result.paste(im, box=((i % lens) * height, int((i / lens)) * height))
    result_size = result.size
    result_dir = str(f'{dir}/result.jpg')
    result.save(result_dir,quality=95)
    result_stats = os.stat(result_dir)
    print(f'拼接完成，拼接图片的尺寸为{result_size}，文件大小为{result_stats.st_size/(1024*1024):.3}MB')

if __name__ == '__main__':
    dir = '/Users/xujingling/Downloads/LM'
    main(dir)
