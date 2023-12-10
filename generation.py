from numpy import floor
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt


def generationMatixLandscape(scale=300):
    noise = PerlinNoise(octaves=2, seed=4522)
    amp = 8
    period = 32
    scale = 300

    landscale = [[0 for i in range(scale)] for i in range(scale)]

    for position in range(scale**2):
        x = floor(position / scale)
        y = floor(position % scale)
        z = floor(noise([x/period, y/period])*amp) - 0.5
        landscale[int(x)][int(y)] = int(z)

    return landscale


# plt.imshow(landscale)
# plt.show()