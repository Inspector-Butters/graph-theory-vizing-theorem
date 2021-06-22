from helper import GraphUtils
from models import *

g = GraphUtils.create_graph()

# print(g)

# g.edges[0].color = 10

# print(g.edges[0].starting_vertex == 0)
# a = g.find_maximal_fan(g.vertices[0])
# print(a)
# b, c, d = g.find_cd_path(g.vertices[0], a)
# print(b)

# if len(b) > 0:
#     g.invert_path(b, c, d)

# w = g.find_w(a, d, g.vertices[0])
# print(w)
# g.rotate_fan(a, w)
# g.color_xw(a, g.vertices[0], w, d)


for v in g.vertices:
    print('vertex: ', g.vertices.index(v))
    fan = g.find_maximal_fan(v)
    print('fan: ', fan)
    if len(fan) > 0:
        path, c, d = g.find_cd_path(v, fan)
        print('path: ', path, 'c: ', c, 'd: ', d)
        if len(path) > 0:
            g.invert_path(path, c, d)
        w = g.find_w(fan, d, v)
        print('w: ', w)
        g.rotate_fan(fan, w)
        g.color_xw(fan, v, w, d)

    print(g)
    print('------------------------')

print(g)
