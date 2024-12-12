from PySide2.QtCore import *
from copy import deepcopy


class Polygon:
    def __init__(self, vertics, seed):
        """ p:多边形顶点坐标 seeds：种子坐标"""
        self.vertics = vertics
        self.seed = seed

    def seed_is_in_polygon(self):
        """判断种子是否位于多边形内部"""
        i = 0
        j = len(self.vertics) - 1

        c = False
        sx = self.seed.x()
        sy = self.seed.y()
        while i < len(self.vertics):
            ix = self.vertics[i].x()
            iy = self.vertics[i].y()
            jx = self.vertics[j].x()
            jy = self.vertics[j].y()
            if ((iy > sy) != (jy > sy)) and (sx < (jx - ix) * (sy - iy) / (jy - iy) + ix):
                c = not c

            j = i
            i = i + 1
        return c

    def max_x(self):
        max1 = 0
        for p in self.vertics:
            if p.x() > max1:
                max1 = p.x()
        return max1

    def min_x(self):
        min1 = self.max_x()
        for p in self.vertics:
            if p.x() < min1:
                min1 = p.x()
        return min1

    def max_y(self):
        max1 = 0
        for p in self.vertics:
            if p.y() > max1:
                max1 = p.y()
        return max1

    def min_y(self):
        min1 = self.max_y()
        for p in self.vertics:
            if p.y() < min1:
                min1 = p.y()
        return min1

    def get_points_set(self):
        """返回需要画的像素点集"""
        points_set = []

        if (not self.seed_is_in_polygon()) or (len(self.vertics) < 3):
            return points_set

        m = self.max_y() - self.min_y() + 1
        n = self.max_x() - self.min_x() + 1
        # 需要声明二维矩阵的大小
        MF = [[False] * n for i in range(m)]  # MF[m][n]

        v = len(self.vertics)
        p0 = self.vertics[0]
        p1 = self.vertics[1]
        for k in range(0, v):
            if k < v - 1:
                p0 = self.vertics[k]
                p1 = self.vertics[k + 1]
            else:
                p0 = self.vertics[k]
                p1 = self.vertics[0]

            x0 = p0.x()
            y0 = p0.y()
            x1 = p1.x()
            y1 = p1.y()

            if y0 == y1:
                y = y0
                if x0 > x1:
                    temp = x0
                    x0 = x1
                    x1 = temp

                for x in range(x0, x1):
                    MF[y - self.min_y()][x - self.min_x()] = True

            elif x0 == x1:
                x = x0
                if y0 > y1:
                    temp = y0
                    y0 = y1
                    y1 = temp

                for y in range(y0, y1):
                    MF[y - self.min_y()][x - self.min_x()] = True

            else:
                dy = float(y1 - y0) / float(x1 - x0)
                dx = 1 / dy

                if dy > -1 and dy < 1:
                    if x0 > x1:
                        temp = x0
                        x0 = x1
                        x1 = temp
                        temp = y0
                        y0 = y1
                        y1 = temp

                    ty = y0
                    for x in range(x0, x1 + 1):
                        y = (int)(ty + 0.5)
                        MF[y - self.min_y()][x - self.min_x()] = True
                        ty += dy

                else:
                    if y0 > y1:
                        temp = y0
                        y0 = y1
                        y1 = temp
                        temp = x0
                        x0 = x1
                        x1 = temp

                    tx = x0
                    for y in range(y0, y1 + 1):
                        x = int(tx + 0.5)
                        MF[y - self.min_y()][x - self.min_x()] = True
                        tx += dx

        seed_stack = []
        seed_stack.append(self.seed)
        MF[self.seed.y() - self.min_y()][self.seed.x() - self.min_x()] = True
        while len(seed_stack) > 0:
            ps = seed_stack.pop()

            p0.setX(ps.x() - 1)
            p0.setY(ps.y())
            if not MF[p0.y() - self.min_y()][p0.x() - self.min_x()]:
                p = deepcopy(p0)  # 深拷贝与浅拷贝
                seed_stack.append(p)
                MF[p0.y() - self.min_y()][p0.x() - self.min_x()] = True

            p0.setX(ps.x() + 1)
            p0.setY(ps.y())
            if not MF[p0.y() - self.min_y()][p0.x() - self.min_x()]:
                p = deepcopy(p0)  # 深拷贝与浅拷贝
                seed_stack.append(p)
                MF[p0.y() - self.min_y()][p0.x() - self.min_x()] = True

            p0.setX(ps.x())
            p0.setY(ps.y() - 1)
            if not MF[p0.y() - self.min_y()][p0.x() - self.min_x()]:
                p = deepcopy(p0)  # 深拷贝与浅拷贝
                seed_stack.append(p)
                MF[p0.y() - self.min_y()][p0.x() - self.min_x()] = True

            p0.setX(ps.x())
            p0.setY(ps.y() + 1)
            if not MF[p0.y() - self.min_y()][p0.x() - self.min_x()]:
                p = deepcopy(p0)  # 深拷贝与浅拷贝
                seed_stack.append(p)
                MF[p0.y() - self.min_y()][p0.x() - self.min_x()] = True

        for j in range(0, m):
            for i in range(0, n):
                if MF[j][i] == True:
                    points_set.append(QPoint(i + self.min_x(), j + self.min_y()))

        return points_set