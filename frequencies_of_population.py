# this dictionary stores the frequency of each digit
# note that initially digits_freq["1"] = 1 since 0! = 1
digits_freq = {"1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

# you could change the value of n depending on your choice
# just note that as n gets bigger, your code takes a lot of time for execution!
n = 16

factorial = 1
for x in range(1, n):
    factorial *= x

    # after computing factorial, we convert it into a string and get its first element
    # then we use it to access the dictionary and increment the corresponding value
    digits_freq[str(factorial)[0]] += 1


# here n = 16, so the printed dictionary will be exactly the table in the introduction
print(digits_freq)
