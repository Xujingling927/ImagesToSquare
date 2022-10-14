# coding=utf-8
from PIL import Image
from scan import scan_dir

def main(dir):
    # 获取文件夹内所有图片
    image_list, lens, total = scan_dir(dir)
    print(f'总照片数: {len(image_list)}, 拼接照片: {lens}')

    # 重新设置大小
    single_size = int(4000 / lens)
    img_resize = list(map(lambda image: image.resize((single_size, single_size)), image_list))

    template = img_resize[0]
    width, height = template.size

    # 定义空白图片大小
    result = Image.new(template.mode, (width * lens, height * lens))

    # 拼接图片
    for i, im in enumerate(img_resize):
        result.paste(im, box=((i % lens) * height, int((i / lens)) * height))
    result.show()

if __name__ == '__main__':
    main('/Users/xujingling/Downloads/LM')
