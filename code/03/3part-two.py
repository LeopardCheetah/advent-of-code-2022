import sys

s = 0

for a in range(100):
    # 300 lines of input => 3 at a time
    x = sys.stdin.readline().strip()
    y = sys.stdin.readline().strip()
    z = sys.stdin.readline().strip()

    # has to be common with all
    for char in x:
        if y.count(char)*z.count(char) > 0:
            if char.lower() == char:
                s += ord(char) - ord('a') + 1
            else:
                s += ord(char) - ord('A') + 26 + 1
            break

print('exec terminated')
print(s)

# O(n^3 now or smth)