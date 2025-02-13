def squares(a, b):
    result = []
    for i in range(a, b):
        k = i ** 2
        result.append(k)

    return result

a = int(input("a = "))
b = int(input("b = "))
k = squares(a, b)

for square in k:
    print(square)

