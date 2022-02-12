from PIL import Image

from src.imagework import ImageWork


def main():
    img_work = ImageWork()
    input_img = Image.open('input.bmp')

    output_img_16 = img_work.convert_color(input_img, 16)
    output_img_256 = img_work.convert_color(input_img, 256)
    
    input_img.show('true_color_image.bmp')
    output_img_16.show('output_16_color.bmp')
    output_img_256.show('output_256_color.bmp')
    
    output_img_16.save('output_16_color.bmp')
    output_img_256.save('output_256_color.bmp')
    
    input_img.close()
    output_img_16.close()
    output_img_256.close()


if __name__ == '__main__':
    main()
