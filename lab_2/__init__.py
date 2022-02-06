from PIL import Image

from src.imagework import ImageWork


def main():
    img_work = ImageWork()
    input_img = Image.open('input.bmp')

    output_img = img_work.add_rand_bolder(input_img, 15)
    output_img.save('output.bmp')

    input_img.close()
    output_img.close()


if __name__ == '__main__':
    main()
