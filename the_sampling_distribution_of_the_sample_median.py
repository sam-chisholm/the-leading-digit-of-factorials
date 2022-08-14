import numpy as np
import matplotlib.pyplot as plt

# first, we create 2 arrays to store our population
leading_digit = np.arange(1, 10)
relative_frequencies = [.2957, .1788, .1276, .0963, .0794, .0715, .0571, .0510, .0426]

# this line of code is made just to make sure that we get the same samples
np.random.seed(0)

# we execute this for n = 30 and n = 65
n = 65

# here we'll be drawing 5000 samples, each sample of size n
# and for each sample, we're calculating its median
# note that we're storing the sample medians in this array
sample_medians = np.empty(5000)
for i in range(5000):
    sample = np.random.choice(leading_digit, size=n, replace=True, p=relative_frequencies)

    sample_medians[i] = np.median(sample)

# here we compute the mean and variance of resulting distribution
sampling_distribution_mean = np.mean(sample_medians)
sampling_distribution_variance = np.var(sample_medians)

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))
plt.box(False)

# we plot the histogram of the sampling
# distribution of the sample median
plt.hist(sample_medians, bins="auto", density=True, color="#0504aa",
         edgecolor="black", linewidth=2)

# setting the x and y label of the graph
plt.xlabel("\ncomputed sample medians")
plt.ylabel("Probability density\n")

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
