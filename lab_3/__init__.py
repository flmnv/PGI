from PIL import Image

from src.imagework import ImageWork


def main():
    img_work = ImageWork()
    input_img = Image.open('input.bmp')

    output_img = img_work.rotate_90(input_img)
    output_img.save('output_90.bmp')
    
    output_img = img_work.rotate_180(input_img)
    output_img.save('output_180.bmp')
    
    output_img = img_work.rotate_270(input_img)
    output_img.save('output_270.bmp')

    input_img.close()
    output_img.close()


if __name__ == '__main__':
    main()
