import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def drawDDA(x1, y1, x2, y2,a):  # 数值微分法
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
    plt.scatter(x, y,c='b')
    for k in range(n):
        # plt.scatter(int(x + 0.5), int(y + 0.5),c='b')
        # print(int(x+0.5),int(y + 0.5))
        a[int(x+0.5)][int(y + 0.5)]=2

        x += xinc
        y += yinc

def seedFill(x, y, a):
    if(a[x][y] == 0):
        a[x][y] = 1
        if(a[x+1][y] == 0):
            seedFill(x+1, y,a)
        if(a[x][y+1] == 0):
            seedFill(x, y+1,a)
        if(a[x-1][y] == 0):
            seedFill(x-1, y,a)
        if(a[x][y-1] == 0):
            seedFill(x, y-1,a)

def seedfill(x1, y1, x2, y2,x3,y3,x4,y4):
    plt.cla()
    list=[x1, y1, x2, y2,x3,y3,x4,y4]
    k=max(list)
    a=[[0 for i in range(k+2)] for j in range(k+2)]
    plt.figure(1)
    plt.title('seed')
    plt.axis('equal')
    drawDDA(x1, y1, x2, y2,a)
    drawDDA(x2, y2, x3, y3,a)
    drawDDA(x3, y3, x4, y4,a)
    drawDDA(x4, y4, x1, y1,a)
    seedFill(x1+1,y1+1,a)


    x_major_locator = MultipleLocator(1)
    # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(1)
    # 把y轴的刻度间隔设置为1，并存在变量里
    ax = plt.gca()

    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    # 把y轴的主刻度设置为1的倍数

    for i in range(1, k+1):
        for j in range(1, k+1):
            if (a[i][j] == 1):
                plt.scatter(i, j,c='r')
                plt.pause(0.1)
            elif (a[i][j] == 2):
                plt.scatter(i, j,c='b')



    plt.grid()


seedfill(1,1,2,17,9,17,7,1)
plt.show()
