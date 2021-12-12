from aocd import get_data

class Graph:
    def __init__(self, data, verbose = False):
        self.v = sorted(list(set([x for xx in data for x in xx])))
        self.e = dict()
        for v in self.v:
            self.e[v] = []
            if v == 'end':
                continue
            for u in self.v:
                if u == 'start':
                    continue
                if ([u,v] in data) or ([v,u] in data):
                    self.e[v].append(u) 
        self.no_paths = 0
        self.verbose = verbose

    def walk(self, u, d, visited, path, small_cave_visits):
        visited[u] = True
        path.append(u)

        if u == d:
            self.no_paths += 1
            if self.verbose:
                print(path)
        else:
            for v in self.e[u]:
                if visited[v] == False or v.isupper():
                    self.walk(v, d, visited.copy(), path.copy(), small_cave_visits)
                elif small_cave_visits == 1:
                    self.walk(v,d,visited.copy(), path.copy(), 0 )

    def all_paths(self, part):
        path = []
        visited = {v: 0 for v in self.v}
        if part == 1:
            self.walk("start", "end", visited, path, 0)
        if part == 2:
            self.walk("start", "end", visited, path, 1)
        print(self.no_paths)


def challenge():
    data = get_data(day = 12)
    data = [dd.split("-")  for dd in data.split("\n")]
    #d = "start-A,start-b,A-c,A-b,b-d,A-end,b-end"
    #data = [dd.split("-") for dd in d.split(",")]
    G = Graph(data)
    G.all_paths(1)
    G.all_paths(2)

if __name__ == "__main__":
    challenge()