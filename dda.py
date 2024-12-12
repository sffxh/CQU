import matplotlib.pyplot as plt
import math
from matplotlib.pyplot import MultipleLocator
def ROUND(a):
    if a>0:
           return int(a + 0.5)
    else:
           return int(a-0.5)



def DrawDDA(x1, y1, x2, y2, time_gap, fixed_axis):
    xs = []
    ys = []

    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) - abs(dy) > 0):  # 比较两参数的绝对值哪一个大，哪一个就作为步长参数（n），
        n = abs(dx)  # 此参数将作为沿直线所画出点的数目
    else:
        n = abs(dy)
    xinc = dx / n
    yinc = dy / n
    x = x1
    y = y1
    xs.append(x)
    ys.append(y)

    for k in range(n):
        x += xinc
        y += yinc
        xs.append(ROUND(x))
        ys.append(ROUND(y))

    plt.figure(figsize=(256, 256))
    plt.axis('equal')

    plt.axvline(x=0, linewidth=1, color='k')
    plt.axhline(y=0, linewidth=1, color='k')
    plt.grid()
    x_major_locator = MultipleLocator(1)
    # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(1)
    # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)

    if (fixed_axis):
        plt.axis([-50, 50, -50, 50])
    plt.title("DDA algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(0,len(xs)):
        plt.scatter(xs[i], ys[i])
        plt.pause(float(time_gap))
        plt.draw()
    plt.show()