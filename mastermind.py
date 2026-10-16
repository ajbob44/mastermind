from itertools import permutations

def remaf(cp,pos,wp):
    tpos = []

    perms = []
    for perm in permutations(wp):
        if not perm in perms:
            perms.append(perm)

    for perm in perms:
        for ipos in pos:
            add = True

            for i in range(4):
                if perm[i] == "e":
                    em = 0
                    for j in range(4):
                        if cp[i] == cp[j] and perm[j] != "e":
                            em+=1
                    if ipos.count(cp[i]) > em:
                        add = False

                if perm[i] == "r":
                    if not cp[i] == ipos[i]:
                        add = False

                if perm[i] == "w":
                    if cp[i] == ipos[i] or not cp[i] in ipos:
                        add = False

            if add:
                if not ipos in tpos:
                    tpos.append(ipos[:])

    return tpos

pos = []
for i in range(7**4):
    comb = [i%7,int(i/7)%7,int(i/49)%7,int(i/343)%7]
    pos.append(comb)

print("best move: [3,2,1,0]")
cp = [3,2,1,0]
while True:
    
    w = int(input("w: "))
    r = int(input("r: "))

    wp = ["e","e","e","e"]
    for i in range(w):
        wp[i] = "w"
    for i in range(w,r+w):
        wp[i] = "r"
    

    pos = remaf(cp,pos,wp)
    print(f"remaining: {len(pos)}")
    if len(pos) < 10:
        print(pos)

    best = len(pos)
    bestm = []
    for ipos in pos:
        wost = 0
        #print(f"{ipos} checked")
        for wi in range(5):
            for ri in range(5-wi):
                wpi = ["e","e","e","e"]
                for i in range(wi):
                    wpi[i] = "w"
                for i in range(wi,ri+wi):
                    wpi[i] = "r"

                pp = remaf(ipos,pos,wpi)
                if len(pp) > wost:
                    wost = len(pp)

        if wost < best:
            bestm = ipos[:]
            best = wost
            print(f"new best move {bestm}\nnew best cutdown {best}")
    print(f"best move {bestm}")
    cp = bestm