from aocd import get_data
import numpy as np
from queue import PriorityQueue
import time
start_time = time.time()


class Graph():
    def __init__(self, data) -> None:
        self.v = len(data) * len(data[0]) # number vertices
        # matrix is mxn groß
        self.m = len(data)
        self.n = len(data[0])
        flatten_data = [dd for d in data for dd in d]
        self.adj_list = {vv : [] for vv in range(self.v)}

        def is_neighbor(i,j):
            if i >= 0 and j >= 0 and i < self.v and j < self.v:
                if (i == j+1  and i % self.m != 0) or (j == i+1 and j % self.m != 0):
                    return True
                if i == j + len(data) or i == j - len(data):
                    return True
            return False
        
        self.is_neighbor = is_neighbor

        for i in range(self.v):
            for j in [i +1, i-1, i + self.m, i - self.m]:
                if is_neighbor(i,j):
                    self.adj_list[i].append([j, flatten_data[j]])

    def dijkstra(self, start, stop):
        visited = np.zeros((self.v))

        distances = [np.inf for _ in range(self.v)]
        distances[start] = 0

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            (d, v) = pq.get()
            visited[v] = 1
            if v == stop:
                break
            for [n_vert, n_dist] in self.adj_list[v]:
                if not visited[n_vert]:
                    old_dist = distances[n_vert] 
                    new_dist = distances[v] + n_dist
                    if old_dist > new_dist:
                        pq.put((new_dist, n_vert))
                        distances[n_vert] = new_dist
        return distances

def build_data(data):
    data_block = np.array(data)
    new_data = np.block([
        [(data_block + i + j - 1) % 9 + 1 for i in range(5)]
        for j in range(5)
    ])
    return new_data



def challenge():
    data = get_data(day = 15)
    #data = "1163751742\n1381373672\n2136511328\n3694931569\n7463417111\n1319128137\n1359912421\n3125421639\n1293138521\n2311944581"
    data = [[int(dd) for dd in d] for d in data.split("\n")]
    G = Graph(data)
    dist = G.dijkstra(0, 9999)
    print("Task 1")
    print(dist[-1])

    data = build_data(data)
    G = Graph(data)
    dist = G.dijkstra(0, 10**4 * 25 -1)
    print("Task 2")
    print(dist[-1])

if __name__ == "__main__":
    challenge()

print("--- %s seconds ---" % (time.time() - start_time))

