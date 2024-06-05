from AdjMatrixGraph import AdjMatrixGraph

## 有限带权图测试
def test_2(data):
    # 读入数据
    ## 有向带权图测试
    n, m, *input_data = data.split()
    n, m = int(n), int(m)
    g = AdjMatrixGraph(n, m, False, False)
    g.addVertex(input_data[:n])
    
    edge_data = input_data[n:]
    while edge_data:
        a = edge_data.pop(0)
        b = edge_data.pop(0)
        c = edge_data.pop(0)
        g.addEdge(a, b, float(c))
    
    g.print()
    g.printDegree()

## 有向带权图
print("\n有向带权图输出：")
data = """6 9
v0 v1 v2 v3 v4 v5
v0 v1 5
v0 v5 2
v1 v2 4
v2 v3 9
v3 v4 7
v3 v5 3
v4 v0 1
v5 v2 1
v5 v4 8
"""
test_2(data)