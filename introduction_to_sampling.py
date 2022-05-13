# NOTE that this code takes on average a minute to finish execution
import numpy as np

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

# here we chose the value of n
# which is the number of random values drawn in each time
n = 10

# here we'll be drawing 5 samples, each sample of size n
# and for each sample, we're calculating some basic statistics
for i in range(1, 6):
    sample = np.random.choice(population_data, size=n, replace=True)
    print("sample " + str(i) + ":", sample, np.mean(sample),
          np.median(sample), np.var(sample, ddof=1), sep="\t\t")
