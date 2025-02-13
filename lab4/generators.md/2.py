def even_generator(n):
    result = []
    for i in range(n):
        if(i % 2 == 0):
            result.append(i)
    
    return result

n = int(input("n = "))
evennumbers = even_generator(n)

print(evennumbers)

