from queue import Queue

# 顶点
class Vertex:
    def __init__(self, name):
        self.id = name
        ## 使用字典存储顶点合集
        self.connectedTo = {}
        ## 出度
        self.out_degree = 0
        ## 入度
        self.in_degree = 0
        
    ## 加入相邻的顶点
    ## nbr为该顶点相邻的顶点名称，weight权重默认为0
    def addNeighbor(self, name, weight = 0):
        self.connectedTo[name] = weight
        ## 每加入一个相邻点，出度加1
        self.out_degree += 1 
        ## 对于相邻点，其入度也加1
        name.in_degree += 1 

# 邻接表建图
class ListGraph:
    def __init__(self, isDir=False):
        ## 是否是有向图
        self.isDir = isDir
        ## 图的顶点合集
        self.vertices = {}
        self.numVertices = 0
        ## 顶点访问集
        self.vis = set()
        ## 搜索全部顶点的辅助变量
        self.helper_vis = [False]*self.numVertices

    ## 增加顶点
    def addVertex(self, name):
        self.numVertices = self.numVertices + 1
        ## 创建一个新的顶点
        newVertex = Vertex(name)
        self.vertices[name] = newVertex
        return newVertex

    ## 查找当前图中是否存在该name的顶点
    def getVertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        else:
            return None

    ## 判断该id的vertex是否在该顶点集合中
    def __contains__(self, name):
        return name in self.vertices

    ## 添加邻接边，f-from起点 t-to终点,cost-边权
    def addEdge(self, f, t, cost=0):
        ## f，t 都是顶点，需要加入顶点集合里面
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)

        ## 顶点f的邻接表添加邻接边
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    ## 获取所有的顶点
    def getVertices(self):
        return list(self.vertices.keys())

    ## 输出该图
    def print(self):
        for i in self.vertices.keys():
            v = self.vertices[i]
            if self.isDir:
                ## 有向图输出
                print(v.id, end=":In-Degree=" + str(v.in_degree) + ",Out-Degree=" + str(v.out_degree) + ",Connected To")
            else:
                ## 无向图输出
                print(v.id, end=":Degree=" + str(v.in_degree+v.out_degree) + ",Connected To")

            for j in v.connectedTo.keys():
                print("->", j.id, end="")
            print()

    ## 深度优先遍历，从顶点st（名称，字符串类型）出发搜到的连通分量
    def dfs(self, st, d=0):
        # 标记当前顶点st已访问
        self.vis.add(st)  

        if d > 0:  # 边界条件，第1个点前没有逗号
            print("->", end=" ")
        print(st, end=" ")  # 输出当前顶点

        ## 遍历st的所有邻接节点
        for v in self.vertices[st].connectedTo.keys():
            ## 当前顶点没访问过
            if v.id not in self.vis:
                ## 递归访问顶点
                self.dfs(v.id, d + 1)  

    ## 深度优先遍历全部顶点
    def dfs_all(self, st):
        ## 初始化变量
        self.vis.clear()
        self.helper_vis = [False]*self.numVertices
        ## 获取顶点名
        key_ls = list(self.vertices.keys())
        ## 获取起始index
        start = key_ls.index(st)
        r1 = range(start, self.numVertices)
        r2 = range(0, start)
        ## 合并下标列表
        index_ls = list(r1) + list(r2)
        ## 遍历所有顶点
        for i in index_ls:
            ## 当前顶点没访问过
            if key_ls[i] not in self.vis:
                self.dfs_helper(key_ls, i, 1)
                print()

    ## 深度优先辅助方法
    def dfs_helper(self, key_ls, index, depth):
        ## 标记当前index的顶点为访问过
        self.helper_vis[index] = True
        self.vis.add(key_ls[index])

        if depth > 1:
            print("->", end=" ")
        print(key_ls[index], end=" ")

        ## 遍历当前顶点的邻接顶点
        for v in self.vertices[key_ls[index]].connectedTo.keys():
            ## 如果当前邻接顶点没有访问过，继续使用深度优先访问
            if v.id not in self.vis:
                next_index = key_ls.index(v.id)
                if not self.helper_vis[next_index]:
                    self.dfs_helper(key_ls, next_index, depth + 1)

    ## 广度优先遍历，从顶点st出发搜到的连通分量
    def bfs(self, st):
        ## 初始化，定义队列，顶点的访问列表
        q=Queue()
        vis=set()
        ## 出发点入队并标记访问过
        q.put(st)
        vis.add(st)
        print(st, end="->")
        ## 只要队列非空，进入队列循环
        while not q.empty():
            ## 出队并输出当前顶点vt
            vt=q.get()
            ## 遍历邻接表
            for v in self.vertices[vt].connectedTo.keys():
                ## vt的邻接点v只要没访问过就入队
                if v.id not in vis:
                    q.put(v.id)
                    vis.add(v.id)
                    print(v.id, end="->")

    ## 广度优先遍历全部顶点
    def bfs_all(self):
        ## 初始化访问集合
        vis = set()
        ## 遍历所有节点
        for vertex_id in self.vertices:
            if vertex_id not in vis:
                self.bfs_helper(vertex_id, vis)
                print()

    ## 广度优先搜索辅助函数
    def bfs_helper(self, st, vis):
        ## 初始化队列
        q = Queue()
        ## 将起始顶点入队并标记访问
        q.put(st)
        vis.add(st)
        
        ## 遍历队列
        while not q.empty():
            vt = q.get()
            print(vt, end="->")
            ## 遍历邻接表
            for v in self.vertices[vt].connectedTo.keys():
                ## 如果邻接点未访问过，入队并标记访问
                if v.id not in vis:
                    q.put(v.id)
                    vis.add(v.id)
