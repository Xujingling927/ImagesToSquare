# coding=utf-8
import os
import math
from PIL import Image
from tqdm import tqdm
from scan import scan_dir
from sort import random_sort

def pic_size_adjust(image_list,size):
    # 重新设置图片尺寸
    print('重新设置尺寸')
    img_resize = []
    for i in tqdm(image_list):
        width, height = i.size
        box = (0,0,0,0)
        if width > height:
            box = (int((width-height)/2),0,int((width-height)/2)+height,height)
        else:
            box = (0,int((height-width)/2),width,int((height-width)/2)+width)
        i = i.crop(box)
        new_img = i.resize((size,size))
        img_resize.append(new_img)
    return img_resize

def square_mode(image_list,lens,total):
    # 正方形模式
    total_max = pow(lens,2)
    print(f'总照片数: {len(image_list)}, 拼接照片宽度: {lens}')
    
    if total > total_max:
        print(f'超过当前可拼接的的最大数量，将随机选择{total_max}张照片进行拼接')
        image_list = random_sort(images_list=image_list,n=total_max)
    max_size_set = int(input('请输入目标尺寸'))
    # 重新设置图片尺寸
    print('重新设置尺寸')
    single_size = int(max_size_set / lens)
    img_resize = pic_size_adjust(image_list=image_list,size=single_size)
        
    template = img_resize[0]
    
    # 定义空白图片大小
    result = Image.new(template.mode, (single_size * lens, single_size * lens))

    # 拼接图片
    print('正在拼接')
    for i, im in enumerate(tqdm(img_resize)):
        result.paste(im, box=((i % lens) * single_size, int((i / lens)) * single_size))
    result_size = result.size
    result_dir = str(f'{dir}/result.jpg')
    result.save(result_dir,quality=95)
    result_stats = os.stat(result_dir)
    print(f'拼接完成，拼接图片的尺寸为{result_size},文件大小为{result_stats.st_size/(1024*1024):.3}M B,保存位置为{result_dir}')

def custom_mode(image_list,total):
    # 自定义宽度模式
    print(f'总照片数: {total}')
    width_count = int(input('输入宽度'))
    high_count = math.ceil(total / width_count)
    max_size_set = int(input('请输入目标尺寸'))
    # 重新设置图片尺寸
    print('重新设置尺寸')
    single_size = int(max_size_set / width_count)
    img_resize = pic_size_adjust(image_list=image_list,size=single_size)
        
    template = img_resize[0]
    
    # 定义空白图片大小
    result = Image.new(template.mode, (single_size * width_count, single_size * high_count))

    # 拼接图片
    print('正在拼接')
    for i, im in enumerate(tqdm(img_resize)):
        result.paste(im, box=((i % width_count) * single_size, int((i / width_count)) * single_size))
    result_size = result.size
    result_dir = str(f'{dir}/result.jpg')
    result.save(result_dir,quality=95)
    result_stats = os.stat(result_dir)
    print(f'拼接完成，拼接图片的尺寸为{result_size},文件大小为{result_stats.st_size/(1024*1024):.3}M B,保存位置为{result_dir}')

def main(dir):
    # 获取文件夹内所有图片
    image_list, lens, total = scan_dir(dir)
    mode_select = int(input('模式选择：1.正方形模式 2.自定义宽度模式'))
    if mode_select == 1:
        square_mode(image_list=image_list,lens=lens,total=total)
    if mode_select == 2:
        custom_mode(image_list=image_list,total=total)
    

if __name__ == '__main__':
    dir = input('请输入文件路径：')
    main(dir)
