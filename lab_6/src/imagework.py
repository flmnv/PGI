from math import ceil
from random import randint

from PIL import Image


class ImageWorkException(Exception):
    pass


class ImageWork:
    def __init__(self) -> None:
        pass

    def add_logo(self, img: Image.Image, logo: Image.Image,
                 logo_visibility: float = 0.45, img_logo_size: float = 0.10,
                 edge_distance: float = 0.03):
        img_with_logo = img

        if logo_visibility < 0 or logo_visibility > 1:
            raise ImageWorkException(
                'Incorrect logo_visibility value (0 <= logo_visibility <= 1)')
        elif img_logo_size <= 0:
            raise ImageWorkException(
                'Incorrect img_logo_size value (img_logo_size > 0)')

        logo_size = max(
            img_logo_size * img.height / logo.height,
            img_logo_size * img.width / logo.width)

        logo_resized = self.resize(logo, logo_size)
        min_side = min(img_with_logo.width, img_with_logo.height) - 1

        logo_start_x = (img_with_logo.width -
                        round(min_side * edge_distance) - logo_resized.width)
        logo_start_y = (img_with_logo.height -
                        round(min_side * edge_distance) - logo_resized.height)

        for x in range(logo_resized.width):
            for y in range(logo_resized.height):
                r, g, b, a = logo_resized.getpixel((x, y))
                logo_resized.putpixel(
                    (x, y), (r, g, b, round(a * logo_visibility)))

        img_with_logo.paste(
            logo_resized, (logo_start_x, logo_start_y), logo_resized)

        return img_with_logo

    def __dict_count(self, dictionary: dict, element):
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1

        return dictionary

    def remove_bg(self, img: Image.Image, clr_diff: float):
        no_bg_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
        bg_color_dict = {}

        if clr_diff < 0 or clr_diff > 1:
            raise ImageWorkException(
                'Incorrect clr_diff value (0 <= clr_diff <= 1)')

        for x in range(img.width):
            bg_color_dict = self.__dict_count(
                bg_color_dict, img.getpixel((x, 0)))
            bg_color_dict = self.__dict_count(
                bg_color_dict, img.getpixel((x, img.height - 1)))

        for y in range(img.height):
            bg_color_dict = self.__dict_count(
                bg_color_dict, img.getpixel((0, y)))
            bg_color_dict = self.__dict_count(
                bg_color_dict, img.getpixel((img.width - 1, y)))

        sort_colors = sorted(bg_color_dict.items(),
                             key=lambda element: element[1], reverse=True)

        bg_color = sort_colors[0][0]

        for x in range(img.width):
            for y in range(img.height):
                color_alpha = 255
                color = img.getpixel((x, y))
                color_diff = (
                    abs(bg_color[0] - color[0]) +
                    abs(bg_color[1] - color[1]) +
                    abs(bg_color[2] - color[2]))

                if color_diff / 765 < clr_diff:
                    color_alpha = round((color_diff / 765) * 255)

                no_bg_img.putpixel(
                    (x, y), (color[0], color[1], color[2], color_alpha))

        return no_bg_img

    def __put_square(self, img: Image.Image, xy: tuple, size: int, value: tuple):
        for x in range(size):
            for y in range(size):
                if y >= img.size[1]:
                    break

                img.putpixel((xy[0] + x, xy[1] + y), value)

            if x >= img.size[0]:
                break

        return img

    def resize(self, img: Image.Image, size_multiply: int):
        img_resize = Image.new(
            'RGBA', (round(img.width * size_multiply), round(img.height * size_multiply)))

        if size_multiply < 0.1 or size_multiply > 10:
            raise ImageWorkException(
                'Incorrect size_multiply value (0.1 <= size_multiply <= 10)')

        if size_multiply < 1:
            for x in range(img.width):
                for y in range(img.height):
                    resize_x = round(x * size_multiply)
                    resize_y = round(y * size_multiply)

                    if resize_x >= img_resize.width or resize_y >= img_resize.height:
                        continue

                    img_resize.putpixel(
                        xy=(resize_x, resize_y),
                        value=img.getpixel((x, y)))
        elif size_multiply > 1:
            enlarged_pixel = ceil(size_multiply)

            for x in range(img.width):
                for y in range(img.height):
                    resize_x = round(x * size_multiply)
                    resize_y = round(y * size_multiply)

                    img_resize = self.__put_square(
                        img=img_resize, xy=(resize_x, resize_y),
                        size=enlarged_pixel, value=img.getpixel((x, y)))
        else:
            return img

        return img_resize

    def convert_color(self, img: Image.Image, colors: int):
        img_color = Image.new('RGB', img.size)

        palette = []
        color_palette = {}

        while len(palette) != colors:
            color = img.getpixel(
                (randint(0, img.width - 1), randint(0, img.height - 1)))

            if color not in palette:
                palette.append(color)

        for x in range(img.width):
            if len(palette) == colors:
                break

            for y in range(img.height):
                color = img.getpixel((x, y))

                if color not in palette:
                    palette.append(color)

                    if len(palette) == colors:
                        break

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                color_diff = []

                if str((r, g, b)) not in color_palette:
                    for num, color in enumerate(palette):
                        diff = (
                            abs(color[0] - r) +
                            abs(color[1] - g) +
                            abs(color[2] - b))

                        color_diff.append((num, diff))

                    color_diff.sort(
                        key=lambda element: element[1])

                    color_palette[str((r, g, b))] = palette[color_diff[0][0]]

                img_color.putpixel((x, y), color_palette[str((r, g, b))])

        return img_color

    def convert_to_wb_palette(self, img: Image.Image, colors: int):
        img_color = Image.new('RGB', img.size)

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))

                rgb = (r + g + b) / 3

                for i in range(colors):
                    if rgb <= (255 / colors) * (i + 1):
                        if i == 0:
                            rgb = 0
                        else:
                            rgb = round((255 / colors) * (i + 1))
                        break

                img_color.putpixel((x, y), (rgb, rgb, rgb))

        return img_color

    def rotate_270(self, img: Image.Image):
        rotate_img = Image.new('RGB', (img.height, img.width))

        for x in range(img.width):
            for y in range(img.height):
                rotate_img.putpixel(
                    (y, rotate_img.height - x - 1), img.getpixel((x, y)))

        return rotate_img

    def rotate_180(self, img: Image.Image):
        rotate_img = Image.new('RGB', (img.width, img.height))

        for x in range(img.width):
            for y in range(img.height):
                rotate_img.putpixel(
                    (rotate_img.width - x - 1, rotate_img.height - y - 1), img.getpixel((x, y)))

        return rotate_img

    def rotate_90(self, img: Image.Image):
        rotate_img = Image.new('RGB', (img.height, img.width))

        for x in range(img.width):
            for y in range(img.height):
                rotate_img.putpixel(
                    (rotate_img.width - y - 1, x), img.getpixel((x, y)))

        return rotate_img

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

    def make_black_and_white(self, img: Image.Image):
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                bw = (r + g + b) // 3
                img.putpixel((x, y), (bw, bw, bw))

        return img
