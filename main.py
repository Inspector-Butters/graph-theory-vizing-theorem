from helper import GraphUtils
from models import *

g = GraphUtils.create_graph()

print(g)

g.edges[0].color = 10

print(g)
