class Edge:
    def __init__(self, starting_vertex, ending_vertex, color=None):
        self.starting_vertex = int(starting_vertex)
        self.ending_vertex = int(ending_vertex)
        self.color = color

    def __str__(self):
        return f'{int(self.starting_vertex)} {int(self.ending_vertex)} {self.color}'

    def __repr__(self):
        return str(self)


class Vertex:
    def __init__(self, pk):
        self.pk = pk

    def __str__(self):
        return str(self.pk)


class Color:
    def __init__(self, pk):
        self.pk = pk

    def __str__(self):
        return str(self.pk)


class Graph:

    def __init__(self, vertices, edges: [Edge]):
        self.vertices = vertices
        self.edges = edges
        self.colors = self.make_colors()

    def nodes_count(self):
        return len(self.vertices)

    def edges_count(self):
        return len(self.edges)

    def __str__(self):
        return f'{self.find_delta()} {self.get_used_colors()}\n' + "\n".join(str(edge) for edge in self.edges)

    def get_used_colors(self):
        cs = [i.color for i in self.edges]
        counter = 0
        for i in self.colors:
            if i in cs:
                counter += 1
        return counter

    def find_maximal_fan(self, vertex):
        vertex_edges = self.get_vertex_edges(vertex)
        fan = []
        # print(vertex_edges)
        # find a non colored edge for Xf
        for i in vertex_edges:
            if i.color is None:
                fan.append(i)
                # vertex_edges.remove(i)
                break
        if len(fan) < 1:
            return []
        else:
            f = True
            while f:
                len1 = len(fan)
                for i in vertex_edges:
                    if i not in fan:
                        if i.color is None:
                            # TODO make vertex getter by pk
                            c = self.get_free_color(vertex, self.find_end(fan[-1], vertex),
                                                    self.find_end(i, vertex))
                            if c is not None:
                                i.color = c
                                fan.append(i)
                            # vertex_edges.remove(i)
                        else:
                            if i.color not in [e.color for e in fan] and \
                                    self.is_color_free_at(i.color, self.find_end(fan[-1], vertex)):
                                fan.append(i)
                if len(fan) == len1:
                    f = False
            return fan

    def make_colors(self):
        colors = []
        for i in range(self.find_delta() + 1):
            colors.append(Color(i + 1))
        return colors

    def find_cd_path(self, vertex, fan):
        last_vertex = self.find_end(fan[-1], vertex)

        c = self.find_free_color_at(vertex)
        d = self.find_free_color_at(last_vertex)

        # print(c, d)

        cd_path = []

        # f = True
        # while f:
        def fill_cd_path(color, v):
            edges = []
            if len(cd_path) < 1:
                edges = fan
            else:
                edges = self.get_vertex_edges(v)

            for i in edges:
                if i.color == color:
                    cd_path.append(i)
                    return fill_cd_path(d if color == c else c, self.find_end(i, v))
            return

        fill_cd_path(d, vertex)

        return cd_path, c, d

    def find_delta(self):
        ends = []
        for i in self.edges:
            ends.append(i.starting_vertex)
            ends.append(i.ending_vertex)
        v = most_frequent(ends)
        c = 0
        for i in ends:
            if i == v:
                c += 1
        return c

    def rotate_fan(self, fan, w):
        e = self.find_edge_of_fan(fan, w)
        limit = fan.index(e)
        for i in range(limit + 1):
            if fan[i] == fan[limit]:
                fan[i].color = None
            else:
                fan[i].color = fan[i + 1].color

    def color_xw(self, fan, v, w, d):
        for i in fan:
            if self.find_end(i, v) == w:
                i.color = d
                return

    def invert_path(self, path, c, d):
        for i in path:
            if i.color == c:
                i.color = d
            else:
                i.color = c

    def find_w(self, fan, d, vertex):
        for i in fan:
            v = self.find_end(i, vertex)
            if self.is_color_free_at(d, v):
                return v
        return self.find_end(fan[-1], vertex)

    def get_vertex_edges(self, vertex):
        s = []
        v = self.vertices.index(vertex)
        for i in self.edges:
            if i.starting_vertex == v or i.ending_vertex == v:
                s.append(i)
        return s

    def get_free_color(self, vertex, last_fan_vertex, end_vertex):
        for i in self.colors:
            if self.is_color_free_at(i, vertex) and self.is_color_free_at(i, last_fan_vertex) and self.is_color_free_at(
                    i, end_vertex):
                return i
        return None

    def is_color_free_at(self, color, vertex):
        vertex_edges = self.get_vertex_edges(vertex)
        if color not in [i.color for i in vertex_edges]:
            return True
        return False

    def find_free_color_at(self, vertex):
        for i in self.colors:
            if self.is_color_free_at(i, vertex):
                return i
        return None

    def find_end(self, v, source):
        return self.vertices[v.starting_vertex] if not \
            self.vertices[v.starting_vertex] == source else \
            self.vertices[v.ending_vertex]

    def find_edge_of_fan(self, fan, w):
        for i in fan:
            if self.vertices[i.starting_vertex] == w or self.vertices[i.ending_vertex] == w:
                return i


def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num
