### Python
import time
import math
import itertools
import threading
import numpy as np


from psonic     import *
from PIL        import Image, ImageDraw
from matplotlib import pyplot as plt
from matplotlib import animation


from psonic import *
class Graph:
    def __init__(self):
        ### value of window--------------------------------
        self.title = 'Graph'
        ### input data ------------------------------------
        self.length= 50 ### number of graph potints
        self.val_x = [0] * self.length
        self.val_y = [0] * self.length
        self.bias  = 0
        self.anime = None
    ### void setup ----------------------------------------

    ### void draw -----------------------------------------
    def update(self, x=0, y=0):
        for i in range(1, self.length):
            self.val_x[i-1] = self.val_x[i]
            self.val_y[i-1] = self.val_y[i]
        self.val_x[self.length-1] = x
        self.val_y[self.length-1] = y - self.bias

    def render(self, num, label):
        plt.subplot(6, 1, num)
        line, = plt.plot(self.val_x, self.val_y, "o", markersize=1, label="sin") # (x,y)のプロット
        line.set_ydata(self.val_y)                        # y値を更新

        plt.xlabel("x")                                   # x軸ラベル
        plt.ylabel(label)                                   # y軸ラベル
        plt.ylim([-0.5,0.5])                                  # y軸範囲
        plt.xlim([min(self.val_x), max(self.val_x)])      # x軸範囲
        plt.grid()                                        # グリッド表示
        ### plt.draw()                                        # グラフの描画


def main():
    plt.ion()           # 対話モードオン
    g1   = Graph()
    g2   = Graph()
    frame= 0

    while True:
        try:
            frame += 1
            if math.sin(frame/10) >= 0.8:
                play(70)

            g1.update(frame/10, math.sin(frame/10))
            g1.render(1, "x")

            g2.update(frame/10, math.cos(frame/10))
            g2.render(2, "y")
            plt.draw()

            plt.pause(0.01)
            plt.clf()                                         # 画面初期化
        except KeyboardInterrupt:
            break

    plt.close() # 画面を閉じる


if __name__ == '__main__':
    main()
