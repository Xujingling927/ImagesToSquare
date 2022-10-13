# coding=utf-8 
from os import listdir
from PIL import Image


def main():
    #文件夹路径
    dir = '/Users/xujingling/Downloads/LM'
    
    #获取文件夹内所有图片
    image_list = []
    for fileName in listdir(dir):
        if fileName.endswith(('.JPG','.jpg',)):
            print(fileName)
            image_list.append(Image.open(dir+'/'+fileName))
    total = len(image_list)
    lens =  int(pow(total,0.5))
    print('总图片数为:',len(image_list),'宽度为:',lens)
    
    #重新设置大小
    img_resize = []
    single_size = int(4000 / lens)
    for i in image_list:
        new_img = i.resize((single_size,single_size))
        img_resize.append(new_img)
    
    
    width,height = img_resize[0].size
    
    #定义空白图片大小
    result = Image.new(img_resize[0].mode,(width*lens,height*lens))
    
    #拼接图片
    for i, im in enumerate(img_resize):
        result.paste(im,box=((i%lens)*height,int((i/lens))*height))
    result.show()
    
        
    
if __name__ == '__main__':
    main()
