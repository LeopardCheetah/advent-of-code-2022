import sys

counter = 0

for i in range(1000):
    # input length is 1000
    x, y = sys.stdin.readline().strip().split(',')
    a, b = map(int, x.split('-'))
    c, d = map(int, y.split('-'))
    
    # a, b, c, d
    # c, d, a, b
    # is there a math way to figure this out?
    
    if b < c or d < a:
        continue
    counter += 1


print('exec end', counter)