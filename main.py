# 1
for i in range(1, 10):
    print(i, end="")
print()
# 2
for i in range(9, 0, -1):
    print(i, end="")
print()
# 3
for i in range(5, 14, 2):
    print(i, end="")
print()
# 4
sum = 0
while True:
    x = int(input("Number to add = "))
    if x == 0:
        break
    sum += x
print("Sum of numbers is: ", sum)
# 5
x = int(input("Number to reverse: "))
rev = 0
while x > 0:
    rev *= 10
    rev += x % 10
    x = int(x // 10)
print(rev)
# 6
ToFac = int(input("Factorial: "))
Fac = 1
for i in range(1, ToFac+1):
    Fac *= i
print(f"Factorial of {ToFac} equals {Fac}")
