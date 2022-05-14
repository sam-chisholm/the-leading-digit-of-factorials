# NOTE: this code takes roughly 1 minute to finish execution
import numpy as np
import matplotlib.pyplot as plt

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

# this line of code is made just to make sure that we get the same samples
np.random.seed(0)

# we execute this for n = 30 and n = 55
n = 30

# here we'll be drawing 5000 samples, each sample of size n
# and for each sample, we're calculating its median
# note that we're storing the sample medians in this array
sample_medians = np.array([])
for i in range(5000):
    sample = np.random.choice(population_data, size=n, replace=True)

    # then we append the median in the array
    sample_medians = np.append(sample_medians, np.median(sample))

# here we compute the mean and variance of resulting distribution
sampling_distribution_mean = np.mean(sample_medians)
sampling_distribution_variance = np.var(sample_medians)

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))

# we plot the histogram of the sampling
# distribution of the sample median
plt.hist(sample_medians, bins="auto", density=True, color="#0504aa",
         edgecolor="black", linewidth=2)

# setting the x label of the graph
plt.xlabel("\ncomputed sample medians")

# setting the plot's title
title = "A histogram showing the sampling distribution\n"
title += "of the sample median for samples of size = " + str(n) + "\n"
plt.title(title, color="blue")

# first we fill text with the values of all observed parameters
text = "$\\mu_{M}$ = " + str(sampling_distribution_mean)
text += "\n$\\sigma^2_{M}$ = " + str(sampling_distribution_variance)

# then we display it on the graph
plt.text(3.5, 2, text, color="blue")

# then we fill text again with the theoretical values
text = "population_median = 3"
text += "\n$\\frac{1}{4 \\times 0.1276^2 \\times n}$ = "
text += str(1 / (4 * n * 0.1276 ** 2))

# then we display it on the graph
plt.text(3.5, 2.75, text)

plt.show()
