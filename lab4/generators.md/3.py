def number_generator(n):
    result = []
    for i in range(n):
        if(i % 3 == 0 and i % 4 == 0):
            result.append(i)

    return result

n = int(input("n = "))
k = number_generator(n)
for i in k:
    print(i)