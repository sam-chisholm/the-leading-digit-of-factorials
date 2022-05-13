# NOTE: this code takes roughly 1 minute to finish execution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

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

# here we calculate the population's parameters
population_mean = np.mean(population_data)
population_variance = np.var(population_data)

# this line of code is made just to make sure that we get the same samples
np.random.seed(0)

# we execute this for n = 100
n = 100

# here we'll be drawing 5000 samples, each sample of size n
# and for each sample, we're calculating its mean
# note that we're storing the sample means in this array
sample_means = np.array([])
for i in range(5000):
    sample = np.random.choice(population_data, size=n, replace=True)

    sample_means = np.append(sample_means, np.mean(sample))

# here we compute the mean and variance of resulting distribution
sampling_distribution_mean = np.mean(sample_means)
sampling_distribution_variance = np.var(sample_means)

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))

# now we simply plot the histogram that represents
# the sampling distribution of the sample mean
# note that density=True means that the sum of
# area under histogram is integrated to 1
plt.hist(sample_means, bins="auto", density=True, color="#0504aa", edgecolor="black",
         linewidth=2)

# In the same time we draw the normal curve on top of the histogram
x = np.arange(np.amin(sample_means), np.amax(sample_means), 0.001)
plt.plot(x, norm.pdf(x, sampling_distribution_mean, np.sqrt(sampling_distribution_variance)),
         color="red", linewidth=5)

# setting the x label of the graph
plt.xlabel("\ncomputed sample means")

# setting the plot's title
title = "A histogram showing the sampling distribution\n"
title += "of the sample mean for samples of size = " + str(n) + "\n"
plt.title(title, color="blue")

# first we fill text with the values of all observed parameters
text = "$\\mu_{\\overline{X}}$ = " + str(sampling_distribution_mean)
text += "\n$\\sigma^2_{\\overline{X}}$ = " + str(sampling_distribution_variance)

# then we display it on the graph
plt.text(2.5, 1.25, text, color="blue")

# then we fill text again with the theoretical values
text = "$\\mu$ = " + str(population_mean)
text += "\n$\\frac{\\sigma^2}{n}$ = " + str(population_variance / n)

# then we display it on the graph
plt.text(3.75, 1.25, text)

plt.show()
