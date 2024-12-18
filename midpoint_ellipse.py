import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
def Drawellipse(xc, yc, rx, ry, time_gap, fixed_axis):
    xs = []
    ys = []
    x = 0
    y = ry
    xs.append(x)
    ys.append(y)

    p = ry * ry +rx*rx*(-ry+0.25)
    while ry*ry * (x + 1) < rx*rx * (y - 0.5):
        #椭圆上部
        if p < 0:
            p += ry*ry * (2 * x + 3)
        else:
            y -= 1
            p += ry*ry * (2 * x + 3) + rx*rx * (-2 * y + 2)
        x+=1
        xs.append(x)
        ys.append(y)

    p = (ry * (x + 0.5)) *(ry * (x + 0.5))  + (rx * (y - 1)) * (rx * (y - 1)) - (rx * ry) * (rx * ry)
    while (y > 0):
        #椭圆下部
        if p > 0:
            p += rx*rx * (-2 * y + 3)
        else:
            x += 1
            p += ry*ry * (2 * x + 2) + rx*rx * (-2 * y + 3)
        y-=1
        xs.append(x)
        ys.append(y)
    plt.figure(figsize=(256,256))
    plt.show()
    plt.grid()
    plt.axis('equal')
    plt.axvline(x=0, linewidth=1, color='k')
    plt.axhline(y=0, linewidth=1, color='k')
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
    plt.title('midpoint_ellipse algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(0,len(xs)):
        if i == 0:
            plt.scatter(xs[i] + xc, ys[i] + yc)
            plt.scatter(xs[i] + xc, -ys[i] + yc)
            plt.pause(time_gap)
        else:
            plt.scatter(xs[i] + xc, ys[i] + yc)
            plt.scatter(-xs[i] + xc, ys[i] + yc)
            plt.scatter(xs[i] + xc, -ys[i] + yc)
            plt.scatter(-xs[i] + xc, -ys[i] + yc)
            plt.pause(time_gap)
            plt.draw()
    plt.show()