from PIL import Image
import argparse

#图片转文字测试--支持多通道图片转换 命令行转换

parser = argparse.ArgumentParser()
#添加命令参数
parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output',default="./OutImage.txt")   #输出文件
parser.add_argument('--t', type = int, default = 50) #输出字符画宽


#获取参数
args = parser.parse_args()

input = args.file
out = args.output
targetSize = args.t

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def getchar(r=0,g=0,b=0,a=256):

    #获取灰度图数值
    ga = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 获取字符长度
    length =len(ascii_char)
    # 这个也是可以理解为透明度,因为以下字符是按照类似于透明度来排列的,最前面的代表透明度值最高（$）
    unit = (a+ 1) / length
    return ascii_char[int(ga/unit)]

def main():
    #缩放系数
    rad = 1
    txt = ""
    targetSizeWidth = targetSize

    img = Image.open(input)
    height = img.height
    width = img.width

    if targetSize == 0:
        targetSizeWidth = width
    else:
        if height > width:
            rad = height / width
            height = rad * targetSizeWidth
        elif width > height:
            rad = width / height
            height = rad * targetSizeWidth
        else:
            width = targetSizeWidth
            height = targetSizeWidth


    img = img.resize((targetSizeWidth,int(height)), Image.NEAREST)

    width = targetSizeWidth

    for i in range(int(height)):
        for j in range(width):
            tm = img.getpixel((j, i))
            if len(tm) == 1:
                txt += getchar(tm[0])
            if len(tm) == 2:
                txt += getchar(tm[0], tm[1])
            elif len(tm) == 3:
                txt += getchar(tm[0],tm[1],tm[2])
            elif len(tm) == 4:
                txt += getchar(tm[0],tm[1],tm[2],tm[3])

        txt += "\n"

    print(txt)

    #输出到文件
    with open(out,"w") as f:
        f.write(txt)
        f.close()
    return ""

main()