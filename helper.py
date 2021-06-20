from models import Edge, Graph


class GraphUtils:

    @staticmethod
    def create_graph():
        inp = input()
        node_count, edge_count = int(inp.split(' ')[0]), int(inp.split(' ')[1])
        edges = []
        for i in range(edge_count):
            inp = input()
            e = Edge(int(inp.split(' ')[0]), int(inp.split(' ')[1]))
            edges.append(e)
        g = Graph(node_count, edges)
        return g
