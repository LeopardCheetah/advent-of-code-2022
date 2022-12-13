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

print(max(ls))