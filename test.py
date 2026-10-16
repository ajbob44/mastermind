check = [0,0,0,0]
cp = [3,2,1,0]

w = 0
r = 0
tcheck = check[:]
for i in range(4):
    if cp[i] == tcheck[i]:
        r+=1
        tcheck[i] = None
        cp[i]
print(tcheck)
for i in range(4):
    if cp[i] in tcheck:
        w+=1
        tcheck[tcheck.index(cp[i])] = None
print(f"w:{w}\nr:{r}")