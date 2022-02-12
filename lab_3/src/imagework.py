from random import randint
from math import ceil, sqrt, sin, cos, pi
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

    def rotate_90(self, img: Image.Image):
        rotate_img = Image.new('RGB', (img.height, img.width))
        
        for x in range(img.width):
            for y in range(img.height):
                rotate_img.putpixel((rotate_img.width - y - 1, x), img.getpixel((x, y)))
                
        return rotate_img
    
    def rotate_180(self, img: Image.Image):
        rotate_img = Image.new('RGB', (img.width, img.height))
        
        for x in range(img.width):
            for y in range(img.height):
                rotate_img.putpixel((rotate_img.width - x - 1, rotate_img.height - y - 1), img.getpixel((x, y)))
                
        return rotate_img
    
    def rotate_270(self, img: Image.Image):
        rotate_img = Image.new('RGB', (img.height, img.width))
        
        for x in range(img.width):
            for y in range(img.height):
                rotate_img.putpixel((y, rotate_img.height - x - 1), img.getpixel((x, y)))
                
        return rotate_img

    def degrees_to_radians(self, degrees: float):
        return pi / 180 * degrees
