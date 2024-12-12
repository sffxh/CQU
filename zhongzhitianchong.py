import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import sys
import win32api,win32con
sys.setrecursionlimit(5000)
np.set_printoptions(threshold=np.inf)
# 初始化450*450的矩阵为零
a = np.zeros((450, 450))
from matplotlib.pyplot import MultipleLocator

# 种子填充算法
def is_in_poly(p, poly):
    """
    :param p: [x, y]
    :param poly: [[], [], [], [], ...]
    :return:
    """
    px, py = p
    is_in = False
    for i, corner in enumerate(poly):
        next_i = i + 1 if i + 1 < len(poly) else 0
        x1, y1 = corner
        x2, y2 = poly[next_i]
        if y1==0 and y2==0:
            if(x1,x2)<px<max(x1,x2):
                is_in=True;
                break
        if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
            is_in = True
            break
        if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
            x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x == px:  # if point is on edge
                is_in = True
                break
            elif x > px:  # if point is on left-side of line
                is_in = not is_in
    return is_in

def seedFill(x, y):
    if (a[x][y] == 0):
        a[x][y] = 1
        if (a[x][y] == 1):
            plt.scatter(x, y, color='#00CED1')
            plt.pause(0.001)
        if (a[x + 1][y] == 0):
            seedFill(x + 1, y)
        if (a[x + 1][y + 1] == 0 and a[x + 1][y] != 2 and a[x][y + 1] != 2):
            seedFill(x + 1, y + 1)
        if (a[x + 1][y + 1] == 0 and a[x + 1][y] == 2 and a[x][y + 1] == 2 and a[x + 1][y + 2] == 2 and a[x + 2][
            y + 1] == 2):
            seedFill(x + 1, y + 1)
        if (a[x][y + 1] == 0):
            seedFill(x, y + 1)
        if (a[x-1][y + 1] == 0 and a[x-1][y] !=2 and a[x][y+1] !=2):
            seedFill(x-1, y + 1)
        if (a[x - 1][y + 1] == 0 and a[x - 1][y] == 2 and a[x][y+1 ] == 2 and a[x - 1][y + 2] == 2 and a[x -2][
            y + 1] == 2):
            seedFill(x - 1, y + 1)
        if (a[x - 1][y] == 0):
            seedFill(x - 1, y)
        if (a[x - 1][y - 1] == 0 and a[x-1][y] !=2 and a[x][y-1] !=2):
            seedFill(x - 1, y - 1)
        if (a[x - 1][y - 1] == 0 and a[x -1][y] == 2 and a[x][y - 1] == 2 and a[x - 1][y - 2] == 2 and a[x - 2][
            y - 1] == 2):
            seedFill(x - 1, y - 1)
        if (a[x ][y-1] == 0):
            seedFill(x , y-1)
        if (a[x+1][y - 1] == 0 and a[x+1][y] !=2 and a[x][y-1] !=2):
            seedFill(x+1, y - 1)
        if (a[x + 1][y -1] == 0 and a[x + 1][y] == 2 and a[x][y - 1] == 2 and a[x + 1][y - 2] == 2 and a[x + 2][
                y - 1] == 2):
                seedFill(x + 1, y - 1)



# DDA直线扫描算法，用于绘制多边形的边界
def DDA(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    k = dy / dx
    x, y = x1, y1
    # 网格线

    for i in range(0, int(abs(dx) + 1)):
        # 需要四舍五入

        plt.scatter(int(round(x)), int(round(y)), color="#000000")
        plt.pause(0.1)

        a[int(round(x))][int(round(y))] = 2

        x += 1
        y += float(k)

# 绘制多边形的边\
def draw(x, y, xEnd, yEnd):
    if xEnd < x:
        x, y, xEnd, yEnd = xEnd, yEnd, x, y
    DDA(x, y, xEnd, yEnd)


# 绘制多边形
def drawLine():
    draw(0, 10, 10, 0)
    draw(10, 0, 20, 10)
    draw(0, 10, 10, 8)
    draw(10, 8,20,10)
    # 网格线




def TC(x_off,y_off):

 point = [x_off, y_off]
 poly = [[0, 10], [10, 0], [20,10], [10, 8]]
 print(is_in_poly(point, poly))
 if(is_in_poly(point, poly)):
     x_major_locator = MultipleLocator(1)
     # 把x轴的刻度间隔设置为1，并存在变量里
     y_major_locator = MultipleLocator(1)
     # 把y轴的刻度间隔设置为10，并存在变量里
     ax = plt.gca()
     # ax为两条坐标轴的实例
     ax.xaxis.set_major_locator(x_major_locator)
     # 把x轴的主刻度设置为1的倍数
     ax.yaxis.set_major_locator(y_major_locator)
     plt.grid()
     drawLine()
     seedFill(x_off, y_off)
     plt.show()
 else:{
        win32api.MessageBox(0,"种子不在多边形内","提醒",win32con.MB_OK)}

