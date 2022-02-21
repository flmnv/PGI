from PIL import Image

from src.imagework import ImageWork


def main():
    img_work = ImageWork()
    input_img = Image.open('input.bmp')

    output_img_small = img_work.resize(input_img, 0.5)
    output_img_big = img_work.resize(input_img, 2)

    print('output_img_small', output_img_small.size)
    output_img_small.save('output_img_small.bmp')

    print('output_img_big', output_img_big.size)
    output_img_big.save('output_img_big.bmp')

    input_img.close()
    output_img_small.close()
    output_img_big.close()


if __name__ == '__main__':
    main()
