n = int(input()) #be dard nakhor
zavaya = [float(m) for m in input().split()]
zavaya = sorted(zavaya) #sort bara float va str
list1 = []
for i in range(n):
    if i == n - 1:
        list1.append((360.0 - zavaya[i]) + zavaya[0])
    else:
        list1.append(zavaya[i + 1] - zavaya[i])
list1 = sorted(list1)
print(list1[-1] / 3.6)