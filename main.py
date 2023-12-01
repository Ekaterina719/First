import sys

n = list(map(str.strip, sys.stdin))
tuda = []
suda = []
for i in range(len(n)):
    with open(n[i], mode='rb') as f:
        s = f.read()
        if len(s) >= 10:
            sorted([s[x] for x in range(len(s)) if x % 2 == 0], reverse=True)[:5]
            for j in range(5):
                t1 = max([s[x] for x in range(len(s)) if x % 2 == 0])
                tuda.append(t1)
                s[s.index(t1)] = 0
            for j in range(5):
                t1 = max([s[x] for x in range(len(s)) if x % 2 == 1])
                suda.append(t1)
                s[s.index(t1)] = 0
        else:
            tuda = [x for x in range(len(n)) if x % 2 == 0]
            suda = [x for x in range(len(n)) if x % 2 == 1]
        print(n[i][:-4], ' tram, ', abs(tuda), ', ', abs(suda), sep='')
