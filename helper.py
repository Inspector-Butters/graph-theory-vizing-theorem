from models import Edge, Graph, Vertex

test_head = '5 7'
test_body = ['0 1', '0 3', '1 2', '1 4', '2 3', '2 4', '3 4']
DEBUG = False


class GraphUtils:

    @staticmethod
    def create_graph():
        inp = input() if not DEBUG else test_head
        node_count, edge_count = int(inp.split(' ')[0]), int(inp.split(' ')[1])
        vertices = []
        counter = 0
        for i in range(node_count):
            v = Vertex(counter)
            vertices.append(v)
            counter += 1

        edges = []
        for i in range(edge_count):
            inp = input() if not DEBUG else test_body[i]
            e = Edge(int(inp.split(' ')[0]), int(inp.split(' ')[1]))
            edges.append(e)
        g = Graph(vertices, edges)
        return g
