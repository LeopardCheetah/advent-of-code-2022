# a = rock
# b = paper
# c = scissors

# x = rock
# y = paper
# z = scissors

s = 0
while True:
    try:
        k = input()
    except:
        break
    k = k.lower()

    n, r = k.split()
    
    # r => result
    # n => thing chosen

    if r == 'y':
        s += 3
        s += ord(n) - ord('a') + 1
        continue

    if r == 'z':
        s += 6
        if n == 'a':
            s += 2
            continue
        elif n == 'b':
            s += 3
            continue
        s += 1
        # yea if-statements ftw
        continue
    # to lose
    s += ord(n) - ord('a')
    if ord(n) - ord('a') == 0:
        s += 3
print(s)