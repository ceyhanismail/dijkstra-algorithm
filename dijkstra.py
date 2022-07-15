# sys library is used for INT_MAX
import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
 
    # a function to find the vertex with minimum distance value, from the set of vertices which is not yet included in shortest path tree.
    def minDistance(self, dist, setSpt):
 
        # the minimum distance is initialized for next node.
        min = sys.maxsize
 
        # searching not nearest vertex not in the shortest path tree.
        for u in range(self.V):
            if dist[u] < min and setSpt[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # function that implements Dijkstra's single source shortest path algorithm for a graph represented by using adjacency matrix 
    def dijkstra(self, source):
 
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # the minimum distance vertex is picked from the set of vertices not yet processed.
            # x is always equal to source in first iteration
            x = self.minDistance(dist, sptSet)
 
            # the minimum distance vertex is put in the shortest path tree
            sptSet[x] = True
 
            # the dist value of the adjacent vertices of the picked vertex is updated only if the current distance is greater than new distance and the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)
 

g = Graph(9)

# the graph is represented by adjacency matrix 
wmat = g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ];
# the source node is '0' in this case
g.dijkstra(0);