#1
x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))

#2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#5
myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar["color"]

#6
myset = {'apple', 'banana', 'cherry'}
for x in myset:
    print(x)

#7
a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])

#8

