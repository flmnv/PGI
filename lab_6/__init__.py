from PIL import Image

from src.imagework import ImageWork


def main():
    img_work = ImageWork()
    input_img = Image.open('input.bmp')
    input_logo = Image.open('logo.bmp')

    output_logo_no_bg = img_work.remove_bg(input_logo, 0.50)
    output_img_with_logo = img_work.add_logo(
        input_img, output_logo_no_bg)

    output_logo_no_bg.save('output_logo_no_bg.png')
    output_img_with_logo.save('output_img_with_logo.png')

    input_img.close()
    input_logo.close()
    output_logo_no_bg.close()
    output_img_with_logo.close()


if __name__ == '__main__':
    main()
