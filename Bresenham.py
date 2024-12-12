import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
def DrawBresenham(x1, y1, x2, y2, time_gap, fixed_axis):
    # 斜率绝对值是否大于1
    steep = 0
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    #判断画线方向
    if (x2 - x1) > 0:
        sx = 1
    else:
        sx = -1
    if (y2 - y1) > 0:
        sy = 1
    else:
        sy = -1

    if dy > dx:
    #斜率绝对值大于1，转换成小于1的情况（关于y=x对称）
        steep = 1
        x1, y1 = y1, x1
        dx, dy = dy, dx
        sx, sy = sy, sx

    d = (2 * dy) - dx
    xs = []
    ys = []
    x = x1
    y = y1
    for i in range(0, dx):
        if steep: 
            xs.append(y)
            ys.append(x)
        else:
            xs.append(x)
            ys.append(y)
        
        x = x + sx
        if d >= 0:
            y = y + sy
            d = d + 2*dy-2*dx
        else:
            d = d + 2*dy

    xs.append(x2)
    ys.append(y2)
    plt.show()
    plt.figure(figsize=(256,256))
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

    if(fixed_axis):
        plt.axis([-50, 50, -50, 50])
    plt.title("Bresenham algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(len(xs)):
        plt.scatter(xs[i], ys[i])
        plt.pause(time_gap)
        plt.draw()
    plt.show()