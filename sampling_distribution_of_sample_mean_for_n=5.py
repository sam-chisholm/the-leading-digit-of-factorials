import numpy as np
import matplotlib.pyplot as plt

# first, we create 2 arrays to store our population
leading_digit = np.arange(1, 10)
relative_frequencies = [0.2957, 0.1788, 0.1276, 0.0963, 0.0794, 0.0715, 0.0571, 0.0510, 0.0426]

# this line of code is made just to make sure that we get the same samples
np.random.seed(0)

# we execute this for n = 3
n = 3

# here we'll be drawing 5000 samples, each sample of size n
# and for each sample, we're calculating its mean
# note that we're storing the sample means in this array
sample_means = np.empty(5000)
for i in range(5000):
    sample = np.random.choice(leading_digit, size=n, replace=True, p=relative_frequencies)

    sample_means[i] = np.mean(sample)

# here we compute the mean and variance of resulting distribution
sampling_distribution_mean = np.mean(sample_means)
sampling_distribution_variance = np.var(sample_means)

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))
plt.box(False)

# now we simply plot the histogram that represents
# the sampling distribution of the sample mean
# note that density=True means that the sum of
# area under histogram equals 1
plt.hist(sample_means, bins="auto", density=True, color="#0504aa", edgecolor="black", linewidth=2)

# setting the x label of the graph
plt.xlabel("\nComputed sample means")

# setting the y label of the graph
plt.ylabel("Probability density\n")

# setting the plot's title
title = "A histogram showing the sampling distribution\n"
title += "of the sample mean for samples of size = " + str(n) + "\n"
plt.title(title, color="blue")

# first we fill text with the values of all calculated parameters
text = "$\\mu_{\\overline{X}}$ = " + str(sampling_distribution_mean)
text += "\n$\\sigma^2_{\\overline{X}}$ = " + str(sampling_distribution_variance)

# then we display it on the graph
plt.text(6, 0.35, text, color="blue")

plt.show()
