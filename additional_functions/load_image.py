import sys
from pygame import image
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('../../program_code/checkers/additional_functions/data/pictures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    im = image.load(fullname)
    return im
