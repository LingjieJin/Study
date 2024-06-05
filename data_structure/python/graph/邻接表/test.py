from ListGraph import *

## 测试基本功能
def test():
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

test()