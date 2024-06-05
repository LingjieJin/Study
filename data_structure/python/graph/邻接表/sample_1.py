from ListGraph import *

## 无向图
## sample 1
def sample():
    g = ListGraph()
    g.addEdge("v1", "v2")
    g.addEdge("v2", "v1")
    g.addEdge("v2", "v3")
    g.addEdge("v3", "v2")
    g.addEdge("v3", "v4")
    g.addEdge("v4", "v3")
    g.addEdge("v4", "v1")
    g.addEdge("v1", "v4")
    g.print()
    print("深度优先遍历：")
    g.dfs("v1")
    print()
    print("广度优先遍历：")
    g.bfs("v1")
    print()

sample()
