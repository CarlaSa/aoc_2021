from aocd import get_data
import numpy as np
from scipy.ndimage.measurements import label


def challenge():
    data = get_data(day = 9)
    data = [[int(dd) for dd in d] for d in data.split("\n")]
    # data = ["2199943210","3987894921", "9856789892","8767896789","9899965678", "9999999999", "9999999999", "9999999999", "9999999999", "9999999999"]
    # data = [[int(dd) for dd in d] for d in data]
    data = np.array(data)

    def is_local_min(i,j):
        ind = [[i-1,j], [i+1,j], [i,j-1], [i,j+1]]
        def is_valid(lam):
            return lam >= 0 and lam < 100
        candidates = [data[k,l] for k,l in ind if is_valid(k) and is_valid(l) ]
        return all(data[i,j] < c for c in candidates)

    risk_level = 0
    n, m = data.shape

    for i in range(n):
        for j in range(m):
            if is_local_min(i,j):
                risk_level += 1 + data[i,j]
    print(risk_level)

    data = data < 9
    structure = np.array([[0,1,0],[1,1,1],[0,1,0]])
    labeled, ncomponents = label(data, structure)
    s = [np.sum(labeled == l) for l in range(1, ncomponents+1)]
    print(np.prod(sorted(s)[-3:]))

    

if __name__ == "__main__":
    challenge()


    