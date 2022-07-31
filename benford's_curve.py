# make sure to install the following libraries before importing them!
import matplotlib.pyplot as plt
import numpy as np

# this dictionary stores the frequency of each digit
# note that initially digits_freq["1"] = 1 since 0! = 1
digits_freq = {"1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}


# I' m only testing this code segment for n = 50000
# but, you could use it as well for the 2 previous values of n
n = 50000

factorial = 1
for x in range(1, n):
    factorial *= x

    # after computing factorial, we convert it into a string and get its first element
    # then we use it to access the dictionary and increment the corresponding value
    digits_freq[str(factorial)[0]] += 1

# now we simply create 2 "arrays" to compute all parameters needed
# and to plot our population distribution
leading_digit = np.arange(1, 10)
frequency_values = np.array(list(digits_freq.values()))

# here we compute the real observed parameters of the population
# in the same way we did in the previous code segment
mean = np.sum(leading_digit * frequency_values) / n
variance = np.sum(frequency_values * np.square(leading_digit - mean)) / n

cumulative_freq = median = 0
for i, freq in enumerate(frequency_values, 1):
    cumulative_freq += freq
    if cumulative_freq == n / 2:
        median = (i + i + 1) / 2
        break
    elif cumulative_freq > n / 2:
        median = i
        break

# now we calculate the theoretical parameters based on Benford's law
# the theoretical median = 3
benford_freq = np.log10(1 + 1 / leading_digit)
benford_mean = np.sum(benford_freq * leading_digit)
benford_variance = np.sum(benford_freq * np.square(leading_digit - benford_mean))

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))
plt.box(False)

# plot the bar graph
plt.bar(leading_digit, frequency_values, color="#3185fc", edgecolor="black", linewidth=2)

# setting the x-coordinates of the curve
x = np.arange(1, 9.5, 0.1)
# setting the corresponding y-coordinates
y = np.log10(1 + 1 / x) * n

# plotting Benford's curve
# note that the yellow X in Benford's curve corresponds to leading_digit values
plt.plot(x, y, color="blue", linewidth=3, markevery=(leading_digit - 1) * 10, marker="X",
         markerfacecolor="yellow", markersize=10)

# if you don't use this line of code, not all digits will be printed on the x-axis
plt.xticks(leading_digit)

# setting the x and y label of the graph
plt.xlabel("\nLeading digit of factorial")
plt.ylabel("Frequency\n")

# setting the plot's title
title = "A bar graph showing the distribution of leading digit\n"
title += "of computed factorials for n = " + str(n) + "\n"
plt.title(title)

# first we fill text with the values of all calculated parameters
text = "$\\mu$ = " + str(mean)
text += "\n$\\sigma^2$ = " + str(variance)
text += "\nmedian = " + str(median)

# then we display it on the graph
plt.text(3, 0.25 * n, text)

# now we fill text1 with the theoretical values based on Benford's law
text1 = "$\\mu_{ben}$ = " + str(benford_mean)
text1 += "\n$\\sigma_{ben}^2$ = " + str(benford_variance)
text1 += "\n$median_{ben}$ = 3"

# then we display it on the graph
plt.text(6, 0.25 * n, text1, color="blue")

# here we calculate the percentage of each digit then we display it inside each bar
for i, freq in enumerate(frequency_values, 1):
    plt.text(i - 0.25, freq - 0.03 * n, str(freq * 100 / n) + "%")

# here we display the theoretical percentages based on Benford's law
for i, freq in enumerate(benford_freq, 1):
    plt.text(i - 0.25, (freq + 0.02) * n, str(round(freq * 100, 3)) + "%", color="blue")


plt.text(4.8, 0.15 * n, "the real observed values are in black")
plt.text(4.8, 0.13 * n, "the theoretical values based on Benford's law are in blue",
         color="blue")

plt.show()
