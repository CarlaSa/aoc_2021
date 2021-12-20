from itertools import permutations
from aocd import get_data
import re
from numpy import ceil, floor


def rel(b1, b2):
    return [b2[0]- b1[0], b2[1] - b1[1], b2[2] - b1[2]]

# this is super inefficient because the task says there are 24 rotations but I am testing 48
# however, the way I thought they could be rotated did not work
def rotate(a):
    l = [
        [[aa[0]* i, aa[1]* j, aa[2]* k] for aa in a]
        for i in [1,-1] for j in [1,-1] for k in [1,-1]
    ]
    #l = [ [aa[n:] + aa[:n] for aa in b] for b in l for n in range(3)]
    l = [ [[aa[i], aa[j], aa[k]] for aa in b] for b in l for (i,j,k) in permutations([0,1,2])]
    return l

def overlap(l1, l2):
    m = []
    for i, e1 in enumerate(l1):
        for e2 in l2:
            if e1 == e2:
                m.append(i)
                break
    return(m)

def get_overlap(scanner0, scanner1, num_overlap =12):
    relb0 = [[rel(b, b2) for b2 in scanner0] for b in scanner0]
    relb1 = [[rel(b, b2) for b2 in scanner1] for b in scanner1]
    for i in range(len(scanner0) - 11):
        for j in range(len(scanner1)):
            for k, r in enumerate(rotate(relb1[j])):
                o = overlap(r, relb0[i])
                if len(o) > num_overlap -1:
                    # position scanner1 relativ to scanner2
                    rels1 = rel(rotate(scanner1)[k][j], scanner0[i])
                    #print(rels1)
                    # move scanner1 into coordinates of scanner 0
                    rr = rel(scanner0[i],r[j])
                    new_scanner1 = [rel(rr, b2) for b2 in r]
                    return True, rels1, new_scanner1
    return False, "", ""

def manhatten(b1,b2):
    return sum([abs(b2[0]- b1[0]), abs(b2[1] - b1[1]), abs(b2[2] - b1[2])])


def challenge():
    data = get_data(day = 19)
    #data = "--- scanner 0 ---\n404,-588,-901\n528,-643,409\n-838,591,734\n390,-675,-793\n-537,-823,-458\n-485,-357,347\n-345,-311,381\n-661,-816,-575\n-876,649,763\n-618,-824,-621\n553,345,-567\n474,580,667\n-447,-329,318\n-584,868,-557\n544,-627,-890\n564,392,-477\n455,729,728\n-892,524,684\n-689,845,-530\n423,-701,434\n7,-33,-71\n630,319,-379\n443,580,662\n-789,900,-551\n459,-707,401\n\n--- scanner 1 ---\n686,422,578\n605,423,415\n515,917,-361\n-336,658,858\n95,138,22\n-476,619,847\n-340,-569,-846\n567,-361,727\n-460,603,-452\n669,-402,600\n729,430,532\n-500,-761,534\n-322,571,750\n-466,-666,-811\n-429,-592,574\n-355,545,-477\n703,-491,-529\n-328,-685,520\n413,935,-424\n-391,539,-444\n586,-435,557\n-364,-763,-893\n807,-499,-711\n755,-354,-619\n553,889,-390\n\n--- scanner 2 ---\n649,640,665\n682,-795,504\n-784,533,-524\n-644,584,-595\n-588,-843,648\n-30,6,44\n-674,560,763\n500,723,-460\n609,671,-379\n-555,-800,653\n-675,-892,-343\n697,-426,-610\n578,704,681\n493,664,-388\n-671,-858,530\n-667,343,800\n571,-461,-707\n-138,-166,112\n-889,563,-600\n646,-828,498\n640,759,510\n-630,509,768\n-681,-892,-333\n673,-379,-804\n-742,-814,-386\n577,-820,562\n\n--- scanner 3 ---\n-589,542,597\n605,-692,669\n-500,565,-823\n-660,373,557\n-458,-679,-417\n-488,449,543\n-626,468,-788\n338,-750,-386\n528,-832,-391\n562,-778,733\n-938,-730,414\n543,643,-506\n-524,371,-870\n407,773,750\n-104,29,83\n378,-903,-323\n-778,-728,485\n426,699,580\n-438,-605,-362\n-469,-447,-387\n509,732,623\n647,635,-688\n-868,-804,481\n614,-800,639\n595,780,-596\n\n--- scanner 4 ---\n727,592,562\n-293,-554,779\n441,611,-461\n-714,465,-776\n-743,427,-804\n-660,-479,-426\n832,-632,460\n927,-485,-438\n408,393,-506\n466,436,-512\n110,16,151\n-258,-428,682\n-393,719,612\n-211,-452,876\n808,-476,-593\n-575,615,604\n-485,667,467\n-680,325,-822\n-627,-443,-432\n872,-547,-609\n833,512,582\n807,604,487\n839,-516,451\n891,-625,532\n-652,-548,-490\n30,-46,-14"
    data = data.split("\n\n")
    data = [[[int(ddd) for ddd in d.split(",")] for d in dd.split("\n")[1:]]for dd in data]

    not_shifted = [True for _ in range(len(data))]
    not_shifted[0] = False
    shifted_beacons = data[0]
    scanners = [[0,0,0]]
    tried = {i:[] for i in range(len(data))}

    while sum(not_shifted) > 0:
        change = False
        for i in range(len(data)):
            if not not_shifted[i]:
                for j in range(len(data)):
                    if not_shifted[j] and j not in tried[i]:
                        tried[i].append(j)
                        b, coord, new = get_overlap(data[i], data[j])
                        if b:
                            print(coord)
                            print(j)
                            data[j] = new
                            not_shifted[j] = False
                            scanners.append(coord)
                            for beacon in new:
                                change = True
                                if beacon not in shifted_beacons:
                                    shifted_beacons.append(beacon)
        if not change:
            break
    print(sum(not_shifted))
    print(len(shifted_beacons))

    # for i in range(1, len(data)):
    #     if not_shifted[i]:
    #         b, coord, new = get_overlap(shifted_beacons, data[i], 5)
    #         if b:
    #             print(coord)
    #             print(i)
    #             data[i] = new
    #             not_shifted[i] = False
    #             for beacon in new:
    #                 change = True
    #                 if beacon not in shifted_beacons:
    #                     shifted_beacons.append(beacon)
    
    print(max([manhatten(b1,b2) for b1 in scanners for b2 in scanners]))


if __name__ == "__main__":
    challenge()
