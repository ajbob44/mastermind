from itertools import permutations, product
from time import perf_counter

pegs = 4
colors = 7


def remaf(cp,pos,wp):
    tpos = []

    perms = []
    for perm in permutations(wp):
        if not perm in perms:
            perms.append(perm)

    for perm in perms:
        em = [0]*pegs
        for i in range(pegs):
            for j in range(pegs):
                if cp[i] == cp[j] and perm[j] != "e":
                    em[i]+=1
        for ipos in pos:
            add = True

            for i in range(pegs):
                if perm[i] == "e":
                    if ipos.count(cp[i]) > em[i]:
                        add = False
                        break

                if perm[i] == "r":
                    if not cp[i] == ipos[i]:
                        add = False
                        break

                if perm[i] == "w":
                    if cp[i] == ipos[i] or not cp[i] in ipos:
                        add = False
                        break


            if add:
                if not ipos in tpos:
                    tpos.append(ipos[:])

    return tpos

pos = []
for comb in product(list(range(colors)), repeat=pegs):
    pos.append(list(comb))

cp = []
for i in range(pegs):
    cp.append(i%colors)

print(f"best move: {cp}")

while True:
    
    w = int(input("w: "))
    r = int(input("r: "))

    wp = ["e"]*pegs
    for i in range(w):
        wp[i] = "w"
    for i in range(w,r+w):
        wp[i] = "r"

    start = perf_counter()
    
    pos = remaf(cp,pos,wp)
    print(f"remaining: {len(pos)}")
    if len(pos) == 1:
        print(f"answer = {pos[0]}")

    best = len(pos)
    bestm = []
    for ipos in pos:
        wost = 0
        g = False
        for ri in range(pegs+1):
            for wi in range(pegs+1-ri):
                wpi = ["e"]*pegs
                for i in range(wi):
                    wpi[i] = "w"
                for i in range(wi,ri+wi):
                    wpi[i] = "r"

                pp = remaf(ipos,pos,wpi)
                if len(pp) > wost:
                    wost = len(pp)
                if wost >= best:
                    g = True
                    break
            if g:
                break
        if wost < best:
            bestm = ipos[:]
            best = wost
            print(f"new best move {bestm}\nnew best cutdown {best}")

    print(f"best move {bestm}")
    cp = bestm
    print(f"time to compute: {perf_counter()-start}")