import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# first, we create 2 arrays to store our population
leading_digit = np.arange(1, 10)
relative_frequencies = [.2957, .1788, .1276, .0963, .0794, .0715, .0571, .0510, .0426]

# here we compute the population parameters and the value of m
population_mean = np.sum(leading_digit * relative_frequencies)
population_variance = np.sum(relative_frequencies * (leading_digit - population_mean) ** 2)
m = np.sum(relative_frequencies * (leading_digit - population_mean) ** 4)

# this line of code is made just to make sure that we get the same samples
np.random.seed(0)

# we execute this for n = 5 and later on for n = 70

n = 5

# here we'll be drawing 5000 samples, each sample of size n
# and for each sample, we're calculating its variance
# note that we're storing the sample variances in this array
sample_variances = np.empty(5000)
for i in range(5000):
    sample = np.random.choice(leading_digit, size=n, replace=True, p=relative_frequencies)

    # then we append the variance in the array
    sample_variances[i] = np.var(sample, ddof=1)

# here we compute the mean and variance of resulting distribution
sampling_distribution_mean = np.mean(sample_variances)
sampling_distribution_variance = np.var(sample_variances)

# Set general font size of the graph
plt.rcParams.update({"font.size": 15})

# Set width and height of the plot's window
plt.figure(figsize=(15, 8))
plt.box(False)

# REMEMBER we're plotting (n - 1) * S^2 / sigma^2
# note that density=True means that the sum of
# area under histogram is integrated to 1
plt.hist(sample_variances * (n - 1) / population_variance, bins="auto", density=True, color="#0504aa",
         edgecolor="black", linewidth=2)

# In the same time we draw the chi-squared curve on top of the histogram
x = np.arange(np.amin(sample_variances) * (n - 1) / population_variance,
              np.amax(sample_variances) * (n - 1) / population_variance, 0.001)
plt.plot(x, chi2.pdf(x, df=n - 1), color="red", linewidth=5)

# setting the x and label of the graph
plt.xlabel("\nScaled sample variances")
plt.ylabel("Probability density\n")

# setting the plot's title
title = "A histogram showing the sampling distribution\n"
title += "of the scaled sample variance for samples of size = " + str(n) + "\n"
plt.title(title, color="blue")

# first we fill text with the values of all observed parameters
text = "$\\mu_{S^2}$ = " + str(sampling_distribution_mean)
text += "\n$\\sigma^2_{S^2}$ = " + str(sampling_distribution_variance)

# then we display it on the graph
plt.text(8, 0.175, text, color="blue")

# USE THIS LINE OF CODE WHEN n = 70 INSTEAD of the previous one
# plt.text(85, 0.035, text, color="blue")

# then we fill text again with the theoretical values
text = "$\\sigma^2$ = " + str(population_variance)
text += "\n$\\frac{m \\times (n - 1) - (n - 3) \\times \\sigma^4}{n \\times (n - 1)}$ = "
text += str((m * (n - 1) - (n - 3) * population_variance ** 2) / (n ** 2 - n))

# then we display it on the graph
plt.text(8, 0.125, text)

# USE THIS LINE OF CODE WHEN n = 70 INSTEAD of the previous one
# plt.text(85, 0.025, text)
plt.show()
