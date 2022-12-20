# finally an easy one
# but now its the second part

import sys
s = sys.stdin.readline().strip()

c = -1

for i in range(3, len(s)):
    ls = [s[i-t] for t in range(14)]
    if len(set(ls)) == 14:
        c = i+1
        break

print(c)