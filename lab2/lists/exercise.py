#1
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

#2
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#3
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#4
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#5
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#6
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#7
fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)

#8
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#9
fruits = ['apple', 'banana', 'cherry']
fruits.clear()

#10
mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

#11
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]

#12
