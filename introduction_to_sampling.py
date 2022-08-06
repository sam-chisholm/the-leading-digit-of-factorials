import numpy as np

# first, we create 2 arrays to store our population
leading_digit = np.arange(1, 10)
relative_frequencies = [0.2957, 0.1788, 0.1276, 0.0963, 0.0794, 0.0715, 0.0571, 0.0510, 0.0426]

# this line of code is made just to make sure that we get the same samples
np.random.seed(0)

# here we chose the value of n
# which is the number of random values drawn in each time
n = 10

# here we'll be drawing 5 samples, each sample of size n
# and for each sample, we're calculating some basic statistics
for i in range(1, 6):
    sample = np.random.choice(leading_digit, size=n, replace=True, p=relative_frequencies)
    print("sample " + str(i) + ":", sample, np.mean(sample),
          np.median(sample), np.var(sample, ddof=1), sep="\t\t")
