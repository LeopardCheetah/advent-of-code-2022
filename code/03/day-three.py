import sys

s = 0

for a in range(300):
    # 300 lines of input
    try:
        x = sys.stdin.readline().strip()
        
        y = x[:(len(x)//2)]
        z = x[(len(x)//2):]

        for char in y:
            if z.count(char) > 0:
                if char.lower() == char:
                    s += ord(char) - ord('a') + 1
                else:
                    s += ord(char) - ord('A') + 27
                break
        continue
    except:
        break

print('exec terminated')
print(s)

# O(n^2)