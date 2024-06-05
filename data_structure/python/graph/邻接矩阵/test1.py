from AdjMatrixGraph import AdjMatrixGraph

## 无向图测试
def test_1(data, dir=True):
    n, m, *input_data = data.split()
    n, m = int(n), int(m)
    graph = AdjMatrixGraph(n, m, dir)

    graph.addVertex(input_data[:n])

    edge_data = input_data[n:]
    while edge_data:
        a = edge_data.pop(0)
        b = edge_data.pop(0)
        graph.addEdge(a, b)

    graph.print()
    graph.printDegree()

## 无向图输出
print("\n第一个无向图输出：")
data = """4 6
v1 v2 v3 v4
v1 v2
v1 v3
v1 v4
v2 v3
v2 v4
v3 v4
"""
test_1(data)


## 无向图输出
print("\n第二个无向图输出：")
data = """4 5
v1 v2 v3 v4
v1 v2
v1 v3
v1 v4
v2 v4
v3 v4
"""
test_1(data)

## 有向图输出
print("\n第一个有向图输出：")
data = """4 5
v1 v2 v3 v4
v2 v1
v2 v3
v2 v4
v3 v1
v4 v3
"""
test_1(data, False)

## 有向图输出
print("\n第二个有向图输出：")
data = """3 4
v1 v2 v3
v1 v2
v1 v3
v2 v1
v3 v2
"""
test_1(data, False)