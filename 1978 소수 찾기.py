N = int(input())
dcmValue = 0
num = list(map(int, input().split()))
for i in num:
    count = 0
    if i ==1:
        continue

    for j in range(2, i+1):
        if i%j == 0:
            count += 1

    if count == 1:
        dcmValue += 1

print(dcmValue)