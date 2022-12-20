import sys

ls = []
lst = []
counter = 0

for i in range(1000):
    # input length is 1000
    x, y = sys.stdin.readline().strip().split(',')
    a, b = map(int, x.split('-'))
    c, d = map(int, y.split('-'))
    
    # a, c, d, b
    # c, a, b, d
    if (a <= c and d <= b) or (c <= a and b <= d):
        counter += 1

print('exec end', counter)