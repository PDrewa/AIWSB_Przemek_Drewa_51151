import math
import pandas
import sklearn
import numpy
import matplotlib

print("Hello world!")
print(1 + 2 * 3)
a = 12
b = 4
c = a / b
print(int(c))
print("Result: ", c)
text = "Result: " + str(c)
print(text)

if c > 2:
    print("Bigger C")
    print("!!!!")
elif c == 2:
    print("equals 2")
else:
    print("Smaller C")
print("End")

for i in range(10):
    print(i)

for i in range(5, 10, 2):
    print(i)

# sum 1+2+3...+20
suma = 0
for i in range(21):
    suma = suma + i

print(suma)

# lists
x = [2, 3, 4, 10, 5]
y = [0, -2, 10, 1, 2]

z = []
for i in range(5):
    z.append(x[i] + y[i])
print(z)


# functions
def summ(f, g):
    s = f + g
    return s

h = summ(15,20)
print(h)

def maxInList(l):
    max = l[0]
    for i in l:
        if i>max:
            max = i
    return max

print(maxInList([3,-2,5,6,1,0]))

a = math.sin[0]