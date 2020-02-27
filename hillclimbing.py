import matplotlib.pyplot as plt
import networkx as nx

def getTotalCost(graph, condition):
  total_cost = 0
  for index in range(len(condition) - 1):
    total_cost = total_cost + graph[condition[index]][condition[index + 1]]['weight'] 
  return total_cost

def evaluate(graph, initial_condition):
  local_minimum_cost = getTotalCost(graph, initial_condition)
  local_minimum_condition = initial_condition.copy()
  local_minimum_changed = False

  first_index = 0

  while first_index in range(len(initial_condition) - 1):
    second_index = first_index + 1
    while second_index < len(initial_condition):
      modified_condition = initial_condition.copy()
      modified_condition[first_index], modified_condition[second_index] = initial_condition[second_index], initial_condition[first_index]
      print(modified_condition)

      for i in range (int(len(modified_condition)) - 1) :
        nx.draw_networkx_edges(graph, pos, arrows = True, edgelist = [(modified_condition[i], modified_condition[i+1]) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'r')
        plt.show(block=False)
        plt.pause(1)

      modified_condition_cost = getTotalCost(graph, modified_condition)
      if modified_condition_cost < local_minimum_cost:
        local_minimum_cost = modified_condition_cost
        local_minimum_condition = modified_condition.copy()
        local_minimum_changed = True

      for i in range (int(len(modified_condition)) - 1) :
        nx.draw_networkx_edges(graph, pos, edgelist = [(modified_condition[i], modified_condition[i+1]) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'black')
        plt.show(block=False)

      plt.pause(1)

      second_index = second_index + 1
    first_index = first_index + 1

  if local_minimum_changed:
    return evaluate(graph, local_minimum_condition)

  return local_minimum_condition, local_minimum_cost

if __name__== "__main__":

  # vertices = input('Enter number of edges : ')

  graph = nx.Graph()

  # for i in range (int(vertices)):
  #   source = input('Enter v1 : ')
  #   goal = input('Enter v2 : ')
  #   weight = input('Enter weight : ')
  #   graph.add_edge(source, goal, weight=weight)

  graph.add_edge('A', 'B', weight=3)
  graph.add_edge('A', 'C', weight=4)
  graph.add_edge('B', 'C', weight=5)

  pos = nx.spring_layout(graph)  

  nx.draw(graph, pos, width = 2.5, with_labels = True)

  edge_labels = dict([((u,v,), d['weight']) for u, v, d in graph.edges(data = True)])
  nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges

  initial_condition = input('Initial condition : ').split(' ')

  print(initial_condition)
  local_minimum_condition, local_minimum_cost = evaluate(graph, initial_condition)

  print('Local Minimum Condition : ', local_minimum_condition)
  print('Local Minimum Cost : ', local_minimum_cost)

  for i in range (int(len(local_minimum_condition)) - 1) :
    nx.draw_networkx_edges(graph, pos, arrows = True, edgelist = [(local_minimum_condition[i], local_minimum_condition[i+1]) for u, v, d in graph.edges(data=True)], width = 2.5, edge_color = 'b')
    plt.show(block=False)
    plt.pause(1)

  plt.show()