import matplotlib.pyplot as plt
import networkx as nx
import time
from queue import PriorityQueue

def bidirectional_search(graph, start, goal):
  if start == goal:
    return [start]

  active_vertices_path_dict = {start: [start], goal: [goal]}
  inactive_vertices = set()

  while len(active_vertices_path_dict) > 0:
    active_vertices = list(active_vertices_path_dict.keys())
    for vertex in active_vertices:
      current_path = active_vertices_path_dict[vertex]
      origin = current_path[0]
      current_neighbours = set(graph[vertex]) - inactive_vertices

      if len(current_neighbours.intersection(active_vertices)) > 0:
        for meeting_vertex in current_neighbours.intersection(active_vertices):
          nx.draw_networkx_edges(graph, pos, edgelist = [(current_path[-1], meeting_vertex) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'r')
          plt.pause(1)

          if origin != active_vertices_path_dict[meeting_vertex][0]:
            active_vertices_path_dict[meeting_vertex].reverse()
            return active_vertices_path_dict[vertex] + active_vertices_path_dict[meeting_vertex]

      if len(set(current_neighbours) - inactive_vertices - set(active_vertices)) == 0:
        active_vertices_path_dict.pop(vertex, None)
        inactive_vertices.add(vertex)

      else:
        for neighbour_vertex in current_neighbours - inactive_vertices - set(active_vertices):
          nx.draw_networkx_edges(graph, pos, edgelist = [(current_path[-1], neighbour_vertex) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'r')
          plt.pause(1)
          
          active_vertices_path_dict[neighbour_vertex] = current_path + [neighbour_vertex]
          active_vertices.append(neighbour_vertex)
        
        active_vertices_path_dict.pop(vertex, None)
        inactive_vertices.add(vertex)

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

  final_path = bidirectional_search(graph, source, goal)
  if final_path != -1:
    for i in range (int(len(final_path)) - 1) :
      nx.draw_networkx_edges(graph, pos, edgelist = [(final_path[i], final_path[i+1]) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'b')
      plt.pause(1)
  else:
    print("sorry no path available :(")

  plt.show()