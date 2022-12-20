# finally an easy one

import sys
s = sys.stdin.readline().strip()

c = -1

for i in range(3, len(s)):
    if len(set([s[i-3], s[i-2], s[i-1], s[i]])) == 4:
        c = i+1
        break

print(c)