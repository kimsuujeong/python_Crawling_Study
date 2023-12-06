# repeat
sum = 0
for num in range (5):
    sum += num
print("~ 4 =", sum)
sum = 0
for num in range(11):
    sum += num
print("~ 10 =", sum)

print("--------------------------")

#calcsum
def calcsum(n):
    sum = 0
    for num in range (n+1):
        sum += num
    return sum

print("~ 4 =", calcsum(4))
print("~ 10 =", calcsum(10))

#listassign