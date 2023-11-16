import os
import shutil

from PIL import Image
from matplotlib import pyplot as plt

from constants import PLOT_DIR
from my_types import ArrayNxM, ArrayNx2


def save_best(population: ArrayNxM[int], cities_coordinates: ArrayNx2[float], score: float, iteration: int) -> None:
    path = cities_coordinates[population]
    plt.clf()
    plt.plot(path[:, 0], path[:, 1], 'o-')
    plt.title(f'[{iteration}] Best score: {score:.3f}')
    plt.savefig(os.path.join(f'{PLOT_DIR}', f'{iteration:06d}.png'))


def save_gif():
    png_files = [f for f in sorted(os.listdir(PLOT_DIR)) if f.lower().endswith('.png')]
    images = []
    for png_file in png_files:
        image_path = os.path.join(PLOT_DIR, png_file)
        img = Image.open(image_path)
        images.append(img)
    images[0].save("animation.gif", save_all=True, append_images=images[1:], loop=0, duration=300)


def clear_plots():
    if not os.path.isdir(PLOT_DIR):
        os.mkdir(PLOT_DIR)
    shutil.rmtree(PLOT_DIR)
    os.mkdir(PLOT_DIR)
