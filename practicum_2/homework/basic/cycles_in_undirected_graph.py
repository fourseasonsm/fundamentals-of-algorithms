import networkx as nx



TEST_GRAPH_FILES = [
    "graph_1_wo_cycles.edgelist",
    "graph_2_w_cycles.edgelist",
]


def has_cycles(G: nx.Graph):
    global flag
    double_visited = -1
    visited = 1
    not_visited = 0
    status = [not_visited] * len(G)
    parent = [None] * len(G)
    def dfs_visit(node):
        global flag
        status[int(node)] = visited
        for i in G.neighbors(node):
            if status[int(i)] == not_visited:
                parent[int(i)] = node
                for j in G.neighbors(i):
                    if (status[int(j)] == visited or status[int(j)] == double_visited) and (j != parent[int(i)]):
                        flag = True
                dfs_visit(i)
        status[int(node)] = double_visited

    flag = False
    for node in G:
        if status[int(node)] == not_visited:
            dfs_visit(node)
    return flag

if __name__ == "__main__":
    for filename in TEST_GRAPH_FILES:
        #G = nx.read_edgelist(f"D://algorithm//spbu-fundamentals-of-algorithms//practicum_2//homework//basic//{filename}", create_using=nx.Graph)
        # Output whether it has cycles
        G = nx.read_edgelist(f"C://Users/Alexandra//Documents//Универ//Algos//fundamentals-of-algorithms//practicum_2//homework//basic//{filename}", create_using=nx.Graph)
        print(f"Graph {filename} has cycles: {has_cycles(G)}")
