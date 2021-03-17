graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def dfs(visited, graph, node):
    if(node not in visited):
        visited.append(node)
        print(node, end = ' ')

        for child in graph[node]:
            dfs(visited, graph, child)


# Driver Code
bfs(visited, graph, 'A')
visited = [] 
queue = []   
print("DFS")    
dfs(visited, graph, 'A')
