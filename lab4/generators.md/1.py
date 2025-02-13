def generator(n):
    result = []
    for i in range(n):
        k = (i + 1) ** 2
        result.append(k)
    return result

n = int(input("n = "))
squares = generator(n)

for x in squares:
    print(x)