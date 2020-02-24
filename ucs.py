import matplotlib.pyplot as plt
import networkx as nx
from queue import PriorityQueue

def ucs(graph, start, goal):
  explored = []
  queue = PriorityQueue()
  queue.put((0, [start]))

  if start == goal:
    return 0

  while queue:
    cost, path = queue.get()
    node = path[-1]
    
    if node not in explored:
      neighbours = graph[node]
      for neighbour in neighbours:

        nx.draw_networkx_edges(graph, pos, edgelist = [(node, neighbour) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'r')

        plt.pause(1)

        new_path = list(path)
        new_path.append(neighbour)
        
        total_cost = cost + int(graph[node][neighbour]['weight'])
        
        print(total_cost, new_path)

        queue.put((total_cost, new_path))
        if neighbour == goal:
          return new_path

      explored.append(node)

  return -1

if __name__== "__main__":
  vertices = input('Enter number of edges : ')

  graph = nx.Graph()

  for i in range (int(vertices)):
    source = input('Enter v1 : ')
    goal = input('Enter v2 : ')
    weight = input('Enter weight : ')
    graph.add_edge(source, goal, weight=weight)

  pos = nx.spring_layout(graph)  

  nx.draw(graph, pos, width = 2.5, with_labels = True)

  edge_labels = dict([((u,v,), d['weight']) for u, v, d in graph.edges(data = True)])
  nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges

  source = input('Enter source : ')
  goal = input('Enter goal : ')

  plt.show(block=False)

  final_path = ucs(graph, source, goal)
  if final_path != 0 and final_path != -1:
    for i in range (int(len(final_path)) - 1) :
      nx.draw_networkx_edges(graph, pos, edgelist = [(final_path[i], final_path[i+1]) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'b')
      plt.pause(1)
  elif final_path == 0:
    print("the goal is the start!")
  else:
    print("sorry no path available :(")

  plt.show()