import numpy as np
from matplotlib import pyplot as plt

small_survey = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = 0
for item in small_survey:
    if item == 'Ceballos':
        total_ceballos += 1
print(total_ceballos)
# out of 70, 33 people voted for Ceballos

# small_survey_lenght = 70
small_survey_lenght = len(small_survey)
percentage_ceballos_from_small = total_ceballos / small_survey_lenght
print(percentage_ceballos_from_small)
# 47% of the votes on the survey are for Ceballos

small_survey_binomial = np.random.binomial(small_survey_lenght, 0.54, size=10000) / small_survey_lenght


# ceballos_loss_small = Percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote from small survey
ceballos_loss_small = len(small_survey_binomial[small_survey_binomial < 0.5]) / 10000
# There is about a 20% change to get the wrong prediction, there are less chances of failure with a larger sample size.
print(ceballos_loss_small)

large_survey_length = 7000
large_survey_binomial = np.random.binomial(large_survey_length, 0.54, size=10000) / large_survey_length

ceballos_loss_large = len(large_survey_binomial[large_survey_binomial < 0.5]) / 10000
print(ceballos_loss_large)
# There is about a 0% change to get the wrong prediction

# Difference between a sample size of 70 and 7000, the larger survey is more concentrated in 54% and is much less likely to the 47% that I got from the smaller survey
plt.hist(small_survey_binomial, bins=20, range=(0, 1))
plt.hist(large_survey_binomial, alpha=0.5, bins=20, range=(0, 1))
plt.show()