import sys

import librosa
import matplotlib.pyplot as plt
import numpy as np


def show(filename):
    y, sr = librosa.load(filename)
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    D = D + 80
    D = D.T
    t = librosa.get_duration(y)
    n = D.shape[0]
    m = D.shape[1]
    fps = 40
    item_number = 128
    DD = [[D[i, j] for j in range(0, m, int(m / item_number))] for i in range(0, n, int(n / fps / t))]
    DD = np.array(DD)
    print(DD.shape)
    plt.ion()
    for i in range(DD.shape[0]):
        plt.cla()
        plt.axis('off')
        plt.bar(range(len(DD[i])), DD[i], width=1.0)
        plt.pause(1 / fps)
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        show("./PJ1.mp3")
    else:
        show(sys.argv[1])
