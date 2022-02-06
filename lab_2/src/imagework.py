from random import randint

from PIL import Image


class ImageWork:
    def __init__(self) -> None:
        pass

    def make_black_and_white(self, img: Image.Image):
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                bw = (r + g + b) // 3
                img.putpixel((x, y), (bw, bw, bw))

        return img

    def add_rand_bolder(self, img: Image.Image, bolder_size: int):
        new_image = Image.new(
            'RGB', (img.width + bolder_size * 2, img.height + bolder_size * 2))

        new_image.paste(img, (bolder_size, bolder_size))

        for x in range(new_image.width):
            if x > bolder_size and x < new_image.width - bolder_size:
                for y in range(new_image.height):
                    if y > bolder_size and y < new_image.height - bolder_size:
                        continue

                    new_image.putpixel(
                        (x, y), (randint(0, 255), randint(0, 255), randint(0, 255)))
            else:
                for y in range(new_image.height):
                    new_image.putpixel(
                        (x, y), (randint(0, 255), randint(0, 255), randint(0, 255)))

        return new_image
