from PIL import Image

from src.imagework import ImageWork


def main():
    img_work = ImageWork()
    input_img = Image.open('input.bmp')

    output_img = img_work.make_black_and_white(input_img)
    output_img.save('output.bmp')
    
    input_img.close()
    output_img.close()


if __name__ == '__main__':
    main()
