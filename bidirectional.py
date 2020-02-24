import matplotlib.pyplot as plt
import networkx as nx
import time
from queue import PriorityQueue

def bi_directional_search(graph, start, goal):
    # Check if start and goal are equal.
    if start == goal:
      return [start]
    # Get dictionary of currently active vertices with their corresponding paths.
    active_vertices_path_dict = {start: [start], goal: [goal]}
    # Vertices we have already examined.
    inactive_vertices = set()

    while len(active_vertices_path_dict) > 0:

      # Make a copy of active vertices so we can modify the original dictionary as we go.
      active_vertices = list(active_vertices_path_dict.keys())
      for vertex in active_vertices:
        # Get the path to where we are.
        current_path = active_vertices_path_dict[vertex]
        # Record whether we started at start or goal.
        origin = current_path[0]
        # Check for new neighbours.
        current_neighbours = set(graph[vertex]) - inactive_vertices
        neighbours_list = list(current_neighbours)

        print(neighbours_list)

        # Check if our neighbours hit an active vertex
        if len(current_neighbours.intersection(active_vertices)) > 0:
          for meeting_vertex in current_neighbours.intersection(active_vertices):
            nx.draw_networkx_edges(graph, pos, edgelist = [(current_path[-1], meeting_vertex) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'r')
            plt.pause(1)
            # Check the two paths didn't start at same place. If not, then we've got a path from start to goal.
            if origin != active_vertices_path_dict[meeting_vertex][0]:
              # Reverse one of the paths.
              active_vertices_path_dict[meeting_vertex].reverse()
              # return the combined results
              return active_vertices_path_dict[vertex] + active_vertices_path_dict[meeting_vertex]

        # No hits, so check for new neighbours to extend our paths.
        if len(set(current_neighbours) - inactive_vertices - set(active_vertices))  == 0:
          # If none, then remove the current path and record the endpoint as inactive.
          active_vertices_path_dict.pop(vertex, None)
          inactive_vertices.add(vertex)

        else:
          # Otherwise extend the paths, remove the previous one and update the inactive vertices.
          for neighbour_vertex in current_neighbours - inactive_vertices - set(active_vertices):
            nx.draw_networkx_edges(graph, pos, edgelist = [(current_path[-1], neighbour_vertex) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'r')
            plt.pause(1)
            active_vertices_path_dict[neighbour_vertex] = current_path + [neighbour_vertex]
            active_vertices.append(neighbour_vertex)
          active_vertices_path_dict.pop(vertex, None)
          inactive_vertices.add(vertex)

    return None

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

  final_path = bi_directional_search(graph, source, goal)
  # final_path = bfs_shortest_path(graph, source, goal)
  if final_path != -1:
    for i in range (int(len(final_path)) - 1) :
      nx.draw_networkx_edges(graph, pos, edgelist = [(final_path[i], final_path[i+1]) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'b')
      plt.pause(1)
  else:
    print("sorry no path available :(")

  plt.show()