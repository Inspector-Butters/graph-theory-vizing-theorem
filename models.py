class Graph:

    def __init__(self, number_of_nodes, edges):
        self._nodes_count = number_of_nodes
        self.edges = edges

    def nodes_count(self):
        return self._nodes_count

    def edges_count(self):
        return len(self.edges)

    def get_edges(self):
        return self.edges

    def __str__(self):
        return ",\n".join(str(edge) for edge in self.edges)


class Edge:
    def __init__(self, starting_vertex: int, ending_vertex, color=0):
        self.starting_vertex = int(starting_vertex),
        self.ending_vertex = int(ending_vertex),
        self.color = color

    def __str__(self):
        return f'({int(self.starting_vertex[0])}-{int(self.ending_vertex[0])}) : {self.color}'

    def __repr__(self):
        return str(self)
