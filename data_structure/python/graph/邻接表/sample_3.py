from ListGraph import *

## 有向图
## sample3
def sample():
    g = ListGraph(isDir=True)
    g.addEdge("A", "B")
    g.addEdge("B", "C")
    g.addEdge("B", "E")
    g.addEdge("B", "F")
    g.addEdge("C", "E")
    g.addEdge("D", "C")
    g.addEdge("E", "B")
    g.addEdge("E", "D")
    g.addEdge("F", "G")
    g.print()
    print("深度优先遍历：")
    g.dfs("A")
    print()
    print("广度优先遍历：")
    g.bfs("A")
    print()

sample()