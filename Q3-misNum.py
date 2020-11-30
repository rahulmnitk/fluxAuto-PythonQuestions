iList = [1, 3, 4, 6, 99]
refList = list(range(0, int(iList[-1]) + 1))

misNum = []
for i in range(len(refList)):
    found = False
    for j in range(len(iList)):
        if iList[j] == refList[i]:
            found = True
            break
    if not found:
        misNum.append(refList[i])
    else:
        continue

print(misNum)
