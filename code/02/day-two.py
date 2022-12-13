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
    
    s += ord(r) - ord('x') + 1
    # - 23

    r = chr(ord(r) - 23)

    if ord(r) == ord(n):
        s += 3
        continue
    
    if ord(n) < ord(r) and (r != 'c' or n != 'a'):
        s += 6
        continue
    
    if r == 'a' and n == 'c':
        s += 6

print(s)