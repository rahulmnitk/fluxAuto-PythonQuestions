# Program to find number(s) in a list
# that do not repeat

#!/usr/bin/python

l = input("Enter a list of numbers: ")
rList = list(l)

# print(conList)
sing = []
repeat = []

for i in range(len(rList)):
    found = False
    if rList[i] not in repeat:
        for j in range(i+1, len(rList)):
            if rList[i] == rList[j]:
                found = True
                repeat.append(rList[i])
                break
        if found:
            continue
        else:
            sing.append(rList[i])

print(rList)
print(sing)
print(repeat)
