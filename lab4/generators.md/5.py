def generator(n):
    result = []
    for i in range(n):
        k = n - i
        result.append(k)

    return result

n = int(input("n = "))
k = generator(n)

for i in k:
    print(i)