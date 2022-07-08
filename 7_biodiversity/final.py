from itertools import groupby
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

species = pd.read_csv("7_biodiversity\species_info.csv")

#replace `None` with `No Intervention`
species.fillna('No Intervention', inplace=True)

#Inspect each DataFrame
#print(species.head())

#How many different species are in the `species` DataFrame?
#print(species.scientific_name.nunique())

#What are the different values of `category` in `species`?
#print(species.category.unique())

#What are the different values of `conservation_status`?
#print(species.conservation_status.unique())

#How many species meet each conservation_status
species.groupby("conservation_status").scientific_name.nunique().reset_index()

#columns sorted by how many species are in each categories
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')

#bar chart: Conservation Status by Species
plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)), protection_counts.scientific_name.values)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel("Number od Species")
plt.title("Conservation Status by Species")
#plt.show()

#New column with the types of species more likely to be endangered
species["is_protected"] = species.conservation_status != 'No Intervention'

#Group the `species` data frame by the `category` and `is_protected` columns and count the unique "scientific_name" in each group.
category_counts = species.groupby(["category", "is_protected"])["scientific_name"].count().reset_index()

#pivot category_counts
category_pivot = category_counts.pivot(columns="is_protected", index="category", values="scientific_name").reset_index()

#Rename the categories
category_pivot.rename(columns={False: "not_protected", True: "protected"}, inplace=True)

#New column of `category_pivot` called `percent_protected`
category_pivot["percent_protected"] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)
#print(category_pivot)


#It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`
#chi squared test, create a contingency table.
contingency =   [[38, 176], [79, 442]]


from scipy.stats import chi2_contingency

chi2_contingency(contingency)
#The difference isn't significant because pval > 0.05

#Testing the difference between `Reptile` and `Mammal`
contingency =   [[38, 176], 
[5, 74]]
chi2_contingency(contingency)
#There is a significant difference between `Reptile` and `Mammal`, pval<0.05



#Conservationists have been recording sightings of different species at several national parks for the past 7 days. They've saved sent you their observations in a file called `observations.csv`.
observations = pd.read_csv("7_biodiversity\observations.csv")
print(observations.head())



#create a new column in `species` called `is_sheep`
species["is_sheep"] = species.common_names.apply(lambda x: "Sheep" in x)
species.head()


#Select the rows of `species` where `is_sheep` is `True`
species[species.is_sheep == True]

#Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`
sheep_species = species[(species.is_sheep == True) & (species.category == "Mammal")]
print(sheep_species)


# merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.
sheep_observations = pd.merge(observations, sheep_species)
print(sheep_observations.head())

#How many total sheep observations (across all three species) were made at each national park?
obs_by_park = sheep_observations.groupby("park_name").observations.sum().reset_index()
print(obs_by_park)

#bar chart showing the different number of observations per week at each park
plt.figure(figsize=(16, 4)) 
ax = plt.subplot()
plt.bar(range(len(obs_by_park.observations)), obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park.observations.values)))
ax.set_xticklabels(obs_by_park.park_name)
plt.ylabel("Number of Observations")
plt.title("Observations of Sheep per Week")
plt.show()


