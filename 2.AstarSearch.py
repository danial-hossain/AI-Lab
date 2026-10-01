import heapq


graph = {
    'S': [('B', 4), ('C', 3)],
    'B': [('f', 5), ('e', 12)],
    'C': [('e', 10), ('d', 7)],
    'd': [('e', 2)],
    'e': [('G', 5)],
    'f': [('G', 16)],
    'G': []
}


h = {
    'S': 14,
    'B': 12,
    'C': 11,
    'd': 6,
    'e': 4,
    'f': 11,
    'G': 0
}


def A_star(start, goal):
  
    open_list = [(h[start], start)]

 
    g = {start: 0}


    parent = {start: None}

    while open_list:

        f, current = heapq.heappop(open_list)

     
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g[goal]

     
        for neighbor, cost in graph[current]:

            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:

                g[neighbor] = new_g
                parent[neighbor] = current

            
                new_f =  g[neighbor] + h[neighbor]

                heapq.heappush(open_list, (new_f, neighbor))

    return None, float('inf')



path, cost = A_star('S', 'G')

print("Best Path:", " -> ".join(path))
print("Total Cost:", cost)