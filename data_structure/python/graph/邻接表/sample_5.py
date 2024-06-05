from ListGraph import *

## 有向加权图
## sample
def sample():
    g = ListGraph(isDir=True)
    g.addEdge("V0", "V4",6)
    g.addEdge("V1", "V0",9)
    g.addEdge("V1", "V2",3)
    g.addEdge("V2", "V0",2)
    g.addEdge("V2", "V3",5)
    g.addEdge("V3", "V4",1)
    g.print()
    print("深度优先遍历：")
    g.dfs("V1")
    print()
    print("广度优先遍历：")
    g.bfs("V1")
    print()

sample()