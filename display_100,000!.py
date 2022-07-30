factorial = 1
for i in range(1, 100001):
    factorial *= i

# this print statement will print 100,000! which is a huge number!!
print(f"{factorial:,}")
