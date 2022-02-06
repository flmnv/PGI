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
