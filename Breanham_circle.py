import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
def DrawBreanhamcircle(x_off, y_off, r, time_gap, fixed_axis):
    xs = []
    ys = []

    # 使用相对点进行画图
    xr = 0
    yr = int(r)
    xs.append(xr)
    ys.append(yr)

    dd = 2 * (xr - yr + 1)
    dhd = 2 * (dd + yr) - 1
    dvd = 2 * (dd - xr) - 1

    while yr>=0:
        # 转化坐标和对称画圆与mid一样
        if dd < 0:
            if dhd < 0:
                xr += 1
                dd += 2 * xr + 1
                dhd = 2 * (dd + yr) - 1
                dvd = 2 * (dd - xr) - 1
            else:
                xr += 1
                yr -= 1
                dd += 2 * (xr - yr + 1)
                dhd = 2 * (dd + yr) - 1
                dvd = 2 * (dd - xr) - 1
        elif dd == 0:
            xr += 1
            yr -= 1
            dd += 2 * (xr - yr + 1)
            dhd = 2 * (dd + yr) - 1
            dvd = 2 * (dd - xr) - 1
        else:
            if dvd < 0:
                xr += 1
                yr -= 1
                dd += 2 * (xr - yr + 1)
                dhd = 2 * (dd + yr) - 1
                dvd = 2 * (dd - xr) - 1
            else:
                yr -= 1
                dd += -2 * yr + 1
                dhd = 2 * (dd + yr) - 1
                dvd = 2 * (dd - xr) - 1

        xs.append(xr)
        ys.append(yr)

    plt.figure(figsize=(100, 100))
    plt.show()
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
    plt.axis('equal')
    plt.axvline(x=0, linewidth=1, color='k')
    plt.axhline(y=0, linewidth=1, color='k')
    if (fixed_axis):
        plt.axis([-50, 50, -50, 50])
    plt.title('midpoint_circle algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')

    for i in range(0, len(xs)):
        plt.scatter(xs[i] + x_off, ys[i] + y_off)
        plt.scatter(-xs[i] + x_off, ys[i] + y_off)
        plt.scatter(xs[i] + x_off, -ys[i] + y_off)
        plt.scatter(-xs[i] + x_off, -ys[i] + y_off)

        plt.pause(time_gap)
        plt.draw()
        plt.show()