import matplotlib.pyplot as plt
import networkx as nx
import time

def bfs_shortest_path(graph, start, goal):
  explored = []
  queue = [[start]]

  if start == goal:
    return "That was easy! Start = goal"

  while queue:
    path = queue.pop(0)
    node = path[-1]
    
    if node not in explored:
      neighbours = graph[node]
      for neighbour in neighbours:

        nx.draw_networkx_edges(graph, pos, edgelist = [(node, neighbour) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'r')
        time.sleep(1)
        plt.pause(0.01)

        new_path = list(path)
        new_path.append(neighbour)
        queue.append(new_path)
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
    graph.add_edge(source, goal)

  pos = nx.spring_layout(graph)  

  nx.draw(graph, pos, width = 2.5, with_labels = True)

  source = input('Enter source : ')
  goal = input('Enter goal : ')

  plt.show(block=False)

  final_path = bfs_shortest_path(graph, source, goal)
  if final_path != -1:
    for i in range (int(len(final_path)) - 1) :
      nx.draw_networkx_edges(graph, pos, edgelist = [(final_path[i], final_path[i+1]) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'b')
      time.sleep(1)
      plt.pause(0.01)
  else:
    print("sorry no path available :(")

  plt.show()