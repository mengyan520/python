count = 0
sum = 0
# 0-100累加
while count <= 100:
    sum += count
    count += 1
    print(sum)
# 偶数求和
sum = 0
count = 0
while count <= 100:
    if count % 2 == 0:
        # print(count)
        sum += count
        print(sum)
    count += 1
# break
i = 0
while i <10:
    if i == 5:
        print("i = %d" % i)
        break
    i += 1
# continue
i = 0
while i < 10 :
    i += 1
    if i == 5:
        continue
    print("i = %d" % i)