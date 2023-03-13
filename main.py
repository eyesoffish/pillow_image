from PIL import Image, ImageFont
import numpy as np
import os
import time

def ascii_art(file):
    im = Image.open(file)
    # 转化成灰色图片
    im = im.convert("L")
    # 降低采样率因为如果图片每张图片像素都对应一个字符,那这回导致图片无比巨大
    sample_rate = 0.15
    # 解决字符拉伸问题
    # font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf")
    # font.getbbox("x")
    # aspect_ratio = font.getlength("x")
    # new_im_size = [int(x * sample_rate) for x in im.size]
    new_im_size = np.array([im.size[0] * sample_rate, im.size[1] * sample_rate * 0.5]).astype(int)
    im = im.resize(new_im_size)
    #转化成一个numpy数组
    im= np.array(im)
    #定义字符集
    symbols = np.array(list(" .-vM"))
    #将图片中的亮度值转成0-5之间的索引
    im = (im - im.min()) / (im.max() - im.min()) * (symbols.size - 1)
    #完成字符转换
    ascii = symbols[im.astype(int)]
    lines = "\n".join("".join(r) for r in ascii)
    return lines

def gifSplit(src_path, dest_path, suffix="png"):
    img = Image.open(src_path)
    paths = []
    for i in range(img.n_frames):
        img.seek(i)
        new = Image.new("RGBA", img.size)
        new.paste(img)
        fileName = "%d.%s" % (i, suffix)
        new.save(os.path.join(dest_path, fileName))
        paths.append(dest_path +"/"+ fileName)
    return paths

if __name__ == "__main__":
    # lines = ascii_art("a.webp")
    paths = gifSplit("b.gif", "pics")
    for i in paths:
        lines = ascii_art(i)
        os.system("clear")
        print(lines)
        time.sleep(0.1)

