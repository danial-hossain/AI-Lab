import heapq
graph = {
    'A': [('B', 11), ('C', 14), ('D', 7)],
    'B': [('E', 15)],
    'C': [('E', 8), ('F', 10)],
    'D': [('F', 25)],
    'E': [('H', 9)],
    'F': [('G', 20)],
    'H': [('G', 10)],
    'G': []
}
h = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0
}
def best_first_search(start, goal):

   
    open_list = [(h[start], start)]

    parent = {start: None}


    closed = []

    while open_list:

       
        value, current = heapq.heappop(open_list)

       
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path

      
        closed.append(current)

        for neighbor, cost in graph[current]:

         
            if neighbor in closed:
                continue

      
            if neighbor not in parent:
                parent[neighbor] = current

            
                heapq.heappush(
                    open_list,
                    (h[neighbor], neighbor)
                )

    return None



path = best_first_search('A', 'G')

print("Best Path:", " -> ".join(path))