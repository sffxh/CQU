import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
def Drawcircle(x_off, y_off, r, time_gap, fixed_axis):
    xs =[]
    ys =[]
    x = 0
    y = r

    d = 1 - r
    xs.append(x)
    ys.append(y)
    while x <y:
        if d < 0:
            #中点在圆内
            d += 2 * x + 3
        else:
            #中点在圆外
            y -= 1
            d += 2 * (x - y) + 5
        x+=1
        xs.append(x)
        ys.append(y)
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
    plt.axvline(x=0,linewidth=1, color='k')
    plt.axhline(y=0,linewidth=1, color='k')
    if(fixed_axis):
        plt.axis([-50, 50, -50, 50])
    plt.title('midpoint_circle algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')

    for i in range(0,len(xs)):



            plt.scatter(xs[i] + x_off, ys[i] + y_off)
            plt.scatter(-xs[i] + x_off, ys[i] + y_off)
            plt.scatter(xs[i] + x_off, -ys[i] + y_off)
            plt.scatter(-xs[i] + x_off, -ys[i] + y_off)
            plt.scatter(ys[i] + x_off, xs[i] + y_off)
            plt.scatter(-ys[i] + x_off, xs[i] + y_off)
            plt.scatter(ys[i] + x_off, -xs[i] + y_off)
            plt.scatter(-ys[i] + x_off, -xs[i] + y_off)
            plt.pause(time_gap)
            plt.draw()
            plt.show()