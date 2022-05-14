# NOTE: this code takes roughly 1 minute to finish execution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# first, we'll store our population set in one single array
# note that the first element of the array is 1 since 0! = 1
population_data = np.array([1])

factorial = 1
for x in range(1, 10000):
    factorial *= x

    # after computing factorial we convert it into a string
    # get that first element and converting that again into an integer
    # then append that in our array
    population_data = np.append(population_data, int(str(factorial)[0]))

# here we compute the value of m
m = np.sum((population_data - np.mean(population_data)) ** 4) / 10000

# this line of code is made just to make sure that we get the same samples
np.random.seed(0)

# we execute this for n = 5 and later on for n = 40
n = 5

# here we'll be drawing 5000 samples, each sample of size n
# and for each sample, we're calculating its variance
# note that we're storing the sample variances in this array
sample_variances = np.array([])
for i in range(5000):
    sample = np.random.choice(population_data, size=n, replace=True)

    # then we append the variance in the array
    sample_variances = np.append(sample_variances, np.var(sample, ddof=1))

# here we compute the mean and variance of resulting distribution
sampling_distribution_mean = np.mean(sample_variances)
sampling_distribution_variance = np.var(sample_variances)

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))

# REMEMBER we're plotting (n - 1) * S^2 / sigma^2
# note that density=True means that the sum of
# area under histogram is integrated to 1
plt.hist(sample_variances * (n - 1) / np.var(population_data), bins="auto", density=True, color="#0504aa",
         edgecolor="black", linewidth=2)

# In the same time we draw the chi-squared curve on top of the histogram
x = np.arange(np.amin(sample_variances) * (n - 1) / np.var(population_data),
              np.amax(sample_variances) * (n - 1) / np.var(population_data), 0.001)
plt.plot(x, chi2.pdf(x, df=n - 1), color="red", linewidth=5)

# setting the x label of the graph
plt.xlabel("\ncomputed sample variances")

# setting the plot's title
title = "A histogram showing the sampling distribution\n"
title += "of the sample variance for samples of size = " + str(n) + "\n"
plt.title(title, color="blue")

# first we fill text with the values of all observed parameters
text = "$\\mu_{S^2}$ = " + str(sampling_distribution_mean)
text += "\n$\\sigma^2_{S^2}$ = " + str(sampling_distribution_variance)

# then we display it on the graph
plt.text(8, 0.175, text, color="blue")
# USE THIS LINE OF CODE WHEN n = 40 INSTEAD of the previous one
# plt.text(15, 0.035, text, color="blue")

# then we fill text again with the theoretical values
text = "$\\sigma^2$ = " + str(np.var(population_data))
text += "\n$\\frac{m \\times (n - 1) - (n - 3) \\times \\sigma^4}{n \\times (n - 1)}$ = "
text += str((m * (n - 1) - (n - 3) * np.var(population_data) ** 2) / (n ** 2 - n))

# then we display it on the graph
plt.text(8, 0.125, text)
# USE THIS LINE OF CODE WHEN n = 40 INSTEAD of the previous one
# plt.text(15, 0.05, text)

plt.show()
