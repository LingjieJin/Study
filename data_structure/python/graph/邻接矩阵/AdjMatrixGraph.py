# 邻接矩阵图
class AdjMatrixGraph:
    #
    def __init__(self, n, m, dir=True, w=True):
        # 顶点数
        self.verNum = n
        # 边数
        self.edgeNum = m
        # 无向图标记和带权标记
        self.dir, self.wt = dir, w
        # 顶点列表
        self.vertex = [0] * n
        # 边列表
        ## 如果 w 为 True，那么初始时每个元素都是 0
        ## 如果 w 为 False，则每个元素都是 float('inf')，表示无穷大
        self.edge = [
            [0 if self.wt else float("inf") for i in range(self.verNum)]
            for j in range(self.verNum)
        ]
                
    def print(self):
        print("顶点数：%d, 边数:%d" % (self.verNum, self.edgeNum))
        print("顶点列表:", self.vertex)
        print("边:")
        ## 更好看地输出
        for edge in self.edge:
            print(edge)

    # 添加/设置顶点
    def addVertex(self, index, value):
        self.vertex[index] = value

    # 设置顶点列表
    def addVertex(self, ls):
        self.vertex = ls

    def addEdge(self, fr, to, w=1):  # 添加边，(fr,to)边权是w
        ifr = self.vertex.index(fr)  # 起点下标
        ito = self.vertex.index(to)  # 终点下标
        if self.dir:  # 无向图
            self.edge[ifr][ito] = self.edge[ito][ifr] = w
        else:  # 有向图
            self.edge[ifr][ito] = w

    # 求度数
    def printDegree(self):
        ## 存放度数用
        in_degrees = [0] * self.verNum
        out_degrees = [0] * self.verNum

        ## 从第一个顶点开始遍历
        for i in range(self.verNum):
            in_degree = out_degree = 0
            for j in range(self.verNum):
                ## 出度是以该顶点为起点
                if self.edge[i][j] != 0 and self.edge[i][j] != float("inf"):
                    out_degree += 1
                ## 入度是以该顶点为终点
                if self.edge[j][i] != 0 and self.edge[j][i] != float("inf"):
                    in_degree += 1
            in_degrees[i] = in_degree
            out_degrees[i] = out_degree

        for i in range(self.verNum):
            ## 无向图
            if self.dir:
                print("顶点 %d 的度数为 %d" % (i, in_degrees[i] + out_degrees[i]))
            else:
                print(
                    "顶点 %d 的入度为 %d, 出度为 %d"
                    % (i, in_degrees[i], out_degrees[i])
                )


def test():
    g = AdjMatrixGraph(4, 6)
    g.vertex[0] = "v1"
    g.addVertex(list("v1 v2 v3 v4".split()))
    g.edge[1][2] = g.edge[2][3] = 1
    g.print()
    g.printDegree()


if __name__ == '__main__':
    test()