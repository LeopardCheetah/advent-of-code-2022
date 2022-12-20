import sys

# i have no clue how to do this other than simulation
giantls = [[] for a in range(9)] # !!
test = [0 for b in range(9)] # holds number of elements in giantls

# fill with initial config
# input:
# 8 lines of crates
# two lines of "nothing"
# 501 lines of instruction

for i in range(8):
    s = sys.stdin.readline().strip()
    # access each based on index
    for j in range(9):
        if s[4*j] != '[':
            continue
        giantls[j].append(s[1+4*j])

for ls in range(9):
    giantls[ls] = giantls[ls][::-1] # reverse to make slicing stuff easier
    test[ls] = len(giantls[ls])


s = sys.stdin.readline()
s = sys.stdin.readline() # eat 2 buffers

for i in range(501):
    # number of input lines

    s = sys.stdin.readline().strip()
    # move [a] from [b] to [c]

    a = 0
    if len(s) > 18:
        # extra chars
        a = 10*int(s[5]) + int(s[6])
    else:
        a = int(s[5])
    
    b = int(s[-6])
    c = int(s[-1])
    test[b-1] = test[b-1] - a
    test[c-1] = test[c-1] + a

    # take back a things then move them from b to c

    # reverse the slicing here

    giantls[c-1] = giantls[c-1] + giantls[b-1][-a:][::-1]
    giantls[b-1] = giantls[b-1][:len(giantls[b-1])-a]

print(giantls)
print(test)
print('exec complete:')
for some_list in range(9):
    if len(giantls[some_list]) == 0:
        print(' ', end = '')
        continue
    print(giantls[some_list][-1], end = '')
