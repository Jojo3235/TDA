class Graph:
    def __init__(self):
        self.vertex_list = []
        self.edge_list = []

    def add_vertex(self, vertex):
        self.vertex_list.append(vertex)

    def add_edge(self, edge):
        self.edge_list.append(edge)
        start_vertex = edge.start_vertex
        end_vertex = edge.end_vertex
        start_vertex.adjacencies_list.append((end_vertex, edge.weight))
        end_vertex.adjacencies_list.append((start_vertex, edge.weight))

    def prim(self, start_vertex):
        # Initialize the heap and visited set
        start_vertex.min_distance = 0
        heap = [start_vertex]
        visited = set()

        while heap:
            # Get the vertex with the minimum distance from the heap
            current_vertex = min(heap)
            heap.remove(current_vertex)
            visited.add(current_vertex)

            # Update the distances of the adjacent vertices
            for adjacent_vertex, weight in current_vertex.adjacencies_list:
                if adjacent_vertex not in visited and weight < adjacent_vertex.min_distance:
                    adjacent_vertex.predecessor = current_vertex
                    adjacent_vertex.min_distance = weight
                    if adjacent_vertex not in heap:
                        heap.append(adjacent_vertex)

        # Return the list of edges in the MST
        mst = []
        for vertex in self.vertex_list:
            if vertex != start_vertex and vertex.predecessor is not None:
                mst.append((vertex.predecessor.name, vertex.name, vertex.min_distance))
        return mst
    
    def kruskal(self):
        self.vertex_list.sort()
        disjoint_set = DisjointSet(self.vertex_list)
        mst = []
        for edge in self.edge_list:
            u = edge.start_vertex
            v = edge.end_vertex
            if disjoint_set.find(u.index) != disjoint_set.find(v.index):
                mst.append((u.name, v.name))
                disjoint_set.union(u.index, v.index)
        return mst
    
    def dijkstra(self, start_vertex):
        # Initialize the heap and visited set
        start_vertex.min_distance = 0
        heap = [start_vertex]
        visited = set()

        while heap:
            # Get the vertex with the minimum distance from the heap
            current_vertex = min(heap)
            heap.remove(current_vertex)
            visited.add(current_vertex)

            # Update the distances of the adjacent vertices
            for adjacent_vertex, weight in current_vertex.adjacencies_list:
                if adjacent_vertex not in visited:
                    distance = current_vertex.min_distance + weight
                    if distance < adjacent_vertex.min_distance:
                        adjacent_vertex.predecessor = current_vertex
                        adjacent_vertex.min_distance = distance
                        if adjacent_vertex not in heap:
                            heap.append(adjacent_vertex)

        # Return the list of edges in the MST
        shortest_paths = []
        for vertex in self.vertex_list:
            if vertex != start_vertex and vertex.predecessor is not None:
                shortest_paths.append((vertex.predecessor.name, vertex.name, vertex.min_distance))
        return shortest_paths
    
import sys

class Vertex:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.adjacencies_list = []
        self.min_distance = sys.maxsize
        self.predecessor = None

    def __lt__(self, other):
        return self.min_distance < other.min_distance

    def __repr__(self):
        return self.name
    
class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight

class DisjointSet:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_nodes = [None] * len(vertex_list)
        self.node_count = 0
        self.make_sets(vertex_list)
    
    def make_sets(self, vertex_list):
        for v in vertex_list:
            self.make_set(v)
    
    def make_set(self, vertex):
        vertex.parent = vertex
        vertex.rank = 0
        self.root_nodes[vertex.index] = vertex
        self.node_count += 1
    
    def find(self, vertex_index):
        vertex = self.vertex_list[vertex_index]
        root = vertex
        while root.parent != root:
            root = root.parent
        current = vertex
        while current != root:
            temp = current.parent
            current.parent = root
            current = temp
        return root.index
    
    def union(self, index1, index2):
        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]
        if root1.rank < root2.rank:
            root1.parent = root2
        elif root1.rank > root2.rank:
            root2.parent = root1
        else:
            root2.parent = root1
            root1.rank += 1
        self.node_count -= 1

def main():
    # Create the vertices
    vertex_a = Vertex("A", 0)
    vertex_b = Vertex("B", 1)
    vertex_c = Vertex("C", 2)
    vertex_d = Vertex("D", 3)
    vertex_e = Vertex("E", 4)
    vertex_f = Vertex("F", 5)
    vertex_g = Vertex("G", 6)
    vertex_h = Vertex("H", 7)
    vertex_i = Vertex("I", 8)

    # Create the edges
    edge_a = Edge(vertex_a, vertex_b, 4)
    edge_b = Edge(vertex_a, vertex_h, 8)
    edge_c = Edge(vertex_b, vertex_h, 11)
    edge_d = Edge(vertex_b, vertex_c, 8)
    edge_e = Edge(vertex_h, vertex_i, 7)
    edge_f = Edge(vertex_i, vertex_g, 6)
    edge_g = Edge(vertex_c, vertex_i, 2)
    edge_h = Edge(vertex_c, vertex_f, 4)
    edge_i = Edge(vertex_c, vertex_d, 7)
    edge_j = Edge(vertex_g, vertex_f, 2)
    edge_k = Edge(vertex_d, vertex_f, 14)
    edge_l = Edge(vertex_d, vertex_e, 9)
    edge_m = Edge(vertex_e, vertex_f, 10)

    # Create the graph and add the vertices and edges
    graph = Graph()
    graph.add_vertex(vertex_a)
    graph.add_vertex(vertex_b)
    graph.add_vertex(vertex_c)
    graph.add_vertex(vertex_d)
    graph.add_vertex(vertex_e)
    graph.add_vertex(vertex_f)
    graph.add_vertex(vertex_g)
    graph.add_vertex(vertex_h)
    graph.add_vertex(vertex_i)
    graph.add_edge(edge_a)
    graph.add_edge(edge_b)
    graph.add_edge(edge_c)
    graph.add_edge(edge_d)
    graph.add_edge(edge_e)
    graph.add_edge(edge_f)
    graph.add_edge(edge_g)
    graph.add_edge(edge_h)
    graph.add_edge(edge_i)
    graph.add_edge(edge_j)
    graph.add_edge(edge_k)
    graph.add_edge(edge_l)
    graph.add_edge(edge_m)

    # Run Prim's algorithm on vertex G
    mst = graph.prim(vertex_g)
    print("Prim's Algorithm:")
    print(mst)

    # Run Kruskal's algorithm
    mst = graph.kruskal()
    print("Kruskal's Algorithm:")
    print(mst)

    # Run Dijkstra's algorithm on vertex A
    shortest_paths = graph.dijkstra(vertex_a)
    print("Dijkstra's Algorithm:")
    print(shortest_paths)

if __name__ == "__main__":
    main()