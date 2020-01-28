source = [12, 4, 67, 2, 34, 11, 89, 45, 76, 29]

num = len(source)
k = 1
while 1:

    for i in range(num-k):
        if source[i] > source[i+1]:
            temp = source[i]
            source[i] = source[i+1]
            source[i+1] = temp
    k += 1
    print(source)
    if k == num - 1:
        break