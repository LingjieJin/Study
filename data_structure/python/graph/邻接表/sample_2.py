from ListGraph import *

## 无向图
## sample
def sample():
    g = ListGraph(isDir=True)
    g.addEdge("A", "C")
    g.addEdge("A", "D")
    g.addEdge("A", "F")
    g.addEdge("B", "C")
    g.addEdge("C", "A")
    g.addEdge("C", "B")
    g.addEdge("C", "D")
    g.addEdge("D", "A")
    g.addEdge("D", "C")
    g.addEdge("E", "G")
    g.addEdge("F", "A")
    g.addEdge("F", "G")
    g.addEdge("G", "E")
    g.addEdge("G", "F")
    g.print()
    print("深度优先遍历：")
    g.dfs("A")
    print()
    print("广度优先遍历：")
    g.bfs("A")
    print()
    
sample()