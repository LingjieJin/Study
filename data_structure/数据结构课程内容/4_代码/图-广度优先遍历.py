
class adjMatrixGraph:
    # 构造方法,n个顶点m条边
    def __init__(self,n,m):
        self.verNum = n #顶点数
        self.edgeNum = m #边数
        self.vertex = [0] * n #顶点列表
        self.edge = [[0 for i in range(self.verNum)] \
                     for j in range(self.verNum)] #邻接矩阵二维列表
        self.vis = [False] * n #顶点的访问列表,默认没访问过
    
    def addVertex (self, ls): #添加顶点列表
        self.vertex = ls
        
    def addEdge(self,fr, to):#添加边(fr,to)
        ifr = self.vertex.index(fr) #起点下标
        ito = self.vertex.index(to) #终点下标
        self.edge[ifr] [ito] = self.edge [ito] [ifr] = 1 #邻接矩阵

def createGraph():
    n, e = map(int, input().split())
    g = adjMatrixGraph(n, e)
    
    g.addVertex(list(input().split()))
        
    for i in range(e):
        fr, to = input().split()
        g.addEdge(fr, to)
    return g

# 定义抽象类型队列Queue, FIFO (First In, First Out)
class Queue:
    # 1. 构造方法,定义一个空的列表
    def __init__(self):
        self.items = []
    # 2. 入队,队尾(列表尾部)入队
    def push(self,item):
        self.items.append(item)
    # 3. 出队,队首(列表头部)出队
    def pop(self):
        return self.items.pop(0)
    # 4. 判断队列是否为空
    def isEmpty(self):
        return self.items == []
    # 5. 取队首
    def getFront(self):
        return self.items[0]
    # 6. 求队列大小
    def getSize(self):
        return len(self.items)
    
# 广度优先遍历,从顶点st(下标)出发搜到的连通分量
def bfs(G, st):
    # 0. 初始化,定义队列,顶点的访问列表
    q = Queue()
    vis = [False] * G.verNum
    # 1. 出发点入队并标记访问过
    q.push(st)
    vis[st] = True
    # 2. 只要队列非空,进入队列循环
    while not q.isEmpty():
        # 2.1 出队并输出当前顶点vt
        vt = q.pop()
        print(" " + str(G.vertex[vt]), end = "")
        # 2.2 遍历邻接矩阵vt行的每个邻接点i
        for i in range(G.verNum):
            # vt的邻接点i只要没访问过就入队
            if G.edge[vt] [i] == 1 and not vis[i]:
                q.push(i)
                vis[i] = True
                
g = createGraph()
v = int(input())
print("BFS from " + g.vertex[v] + " :", end = " ")
bfs(g,v)