ls = []
s = 0
flag = True
while flag:
    try:
        n = input()
        if n == '':
            ls.append(s)
            s = 0
            continue
        s += int(n)
    except:
        flag = not flag

s = 0
s = max(ls)
ls.remove(max(ls))
s += max(ls)
ls.remove(max(ls))
s += max(ls)
print(s)