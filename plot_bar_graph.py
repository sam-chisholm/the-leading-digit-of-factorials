# make sure to install the following libraries before importing them!
import matplotlib.pyplot as plt
import numpy as np

# this dictionary stores the frequency of each digit
# note that initially digits_freq["1"] = 1 since 0! = 1
digits_freq = {"1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

# don't forget to change the value of n here later to 20000 !!!
n = 10000

factorial = 1
for x in range(1, n):
    factorial *= x

    # after computing factorial, we convert it into a string and get its first element
    # then we use it to access the dictionary and increment the corresponding value
    digits_freq[str(factorial)[0]] += 1

# now we simply create 2 "arrays" to compute all parameters needed
# and to plot our population distribution
leading_digit = np.array(range(1, 10))
frequency_values = np.array(list(digits_freq.values()))

# now to compute the mean we first multiply the 2 previous "arrays" element by element
# then we sum all values of resulting "array" and divide by n
# since the total values computed from 0!, 1!, ... and up to (n - 1)! is exactly n
mean = np.sum(leading_digit * frequency_values) / n

# now to calculate the variance we subtract the mean from leading_digit values
# then we square each element of resulting "array"
# then we multiply by frequency_values, sum all values of resulting "array"
# and finally divide by n
variance = np.sum(frequency_values * np.square(leading_digit - mean)) / n

# since we are interested in n = 10000, 20000, and 50000 which are all even
# the median will be the average of the 2 values at positions n / 2 and (n + 2) / 2
# this is not true if n is odd
cumulative_freq = median = 0
for i, freq in enumerate(frequency_values, 1):
    cumulative_freq += freq
    if cumulative_freq == n / 2:
        median = (i + i + 1) / 2
        break
    elif cumulative_freq > n / 2:
        median = i
        break

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))

# plot the bar graph
plt.bar(leading_digit, frequency_values, color="crimson", width=0.75)

# if you don't use this line of code, not all digits will be printed on the x-axis
plt.xticks(leading_digit)

# setting the x and y label of the graph
plt.xlabel("\nLeading digit of factorial")
plt.ylabel("Frequency\n")

# setting the plot's title
title = "A bar graph showing the distribution of leading digit\n"
title += "of computed factorials for n = " + str(n) + "\n"
plt.title(title, color="blue")

# first we fill text with the values of all computed parameters
text = "$\\mu $= " + str(mean)
text += "\n$\\sigma^2$= " + str(variance)
text += "\nmedian = " + str(median)

# then we display it on the graph
plt.text(6, 0.25 * n, text)

# here we calculate the percentage of each digit then we display it on top of each bar
for i, freq in enumerate(frequency_values, 1):
    plt.text(i - 0.25, freq + 0.005 * n, str(freq * 100 / n) + "%", color="blue")

plt.show()
