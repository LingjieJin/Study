from ListGraph import *

## 有向非连通图
## sample 4
def sample():
    g = ListGraph(isDir=True)
    g.addEdge("v1", "v2")
    g.addEdge("v1", "v4")
    g.addEdge("v2", "v3")
    g.addEdge("v4", "v3")
    g.addEdge("v5", "v6")
    g.print()
    print("深度优先遍历：")
    g.dfs_all("v1")
    print()
    print("广度优先遍历：")
    g.bfs_all()
    print()

sample()