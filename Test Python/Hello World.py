import random

print(random.randrange(1,10))

number = 123
number2 = 234
strnumber = '%d is not equal to %d' % (number, number2)

print(strnumber)

fruits = ['banana', 'orange', 'apple']
a, b, c = fruits

print(a,b,c)

for i in range(len(fruits)):
	print("fruits:", fruits[i])



complex1 = 1+5j

print(complex1)

helloStr = "Hello1, Hello2, Hello3!"
print("helloStr is", "Hello1" in helloStr)
print("Slice helloStr is:", helloStr[0:len(helloStr)-10])
print("Split helloStr is:", type(helloStr.split()), helloStr.split())

print("try join function", helloStr.join("Abc"))
print("try join function", "+".join(helloStr))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 80))

tuple1 = tuple(('banana',))
print("tuple 1", tuple1, type(tuple1))