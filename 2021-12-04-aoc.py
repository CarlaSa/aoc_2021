from aocd import get_data
import numpy as np

class bingo():
    def __init__(self, string):
        self.rows = [[int(x) for x in y.split(" ") if x.isnumeric()] for y in string.split("\n")]
        self.columns = np.array(self.rows).T.tolist()
        self.all = [x for y in self.rows for x in y]
    
    def __str__(self):
        return ", ".join(str(x) for x in self.rows) +  ", ".join(str(x) for x in self.columns)

    def check_rc(self, rc, number_list):
        return set(rc) <= set(number_list)

    def check_sheet(self,number_list):
        for r in self.rows:
            if self.check_rc(r, number_list):
                return True, r
        for c in self.columns:
            if self.check_rc(c, number_list):
                return True, c
        return False, None

    def get_winning_score(self, number_list):
        unmarked = set(self.all) - set(number_list)
        return sum(unmarked) * number_list[-1]



def challenge():
    data = get_data(day = 4)
    num, data = data.split("\n\n", 1)
    data = [d for d in data.split("\n\n")]
    num = [int(n) for n in num.split(",")]
    bingo_sheets = {i: bingo(data[i]) for i in range(len(data))}

    print("wins first")
    def check_list():
        for j in range(1, len(num)):
            nums = num[0:j]
            for i in bingo_sheets:
                t, val = bingo_sheets[i].check_sheet(nums)
                if t:
                    print(val)
                    print(bingo_sheets[i].get_winning_score(nums))
                    return
    check_list()

    print("wins last")
    def check_list():
        has_won = [False for i in range(len(bingo_sheets))]
        for j in range(1, len(num)):
            nums = num[0:j]
            for i in bingo_sheets:
                if not has_won[i]:
                    t, val = bingo_sheets[i].check_sheet(nums)
                    if t:
                        has_won[i] = True
                        if all(has_won) == True:
                            print(val)
                            print(bingo_sheets[i].get_winning_score(nums))
                            return
    check_list()

                    
                



challenge()