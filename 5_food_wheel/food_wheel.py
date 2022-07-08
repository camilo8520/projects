import pandas as pd
import matplotlib as plt


restaurants = pd.read_csv("5_food_wheel\restaurants.csv")
print(restaurants.head())

#cuisine_options_count = restaurants.cuisine.nunique()

#cuisine_counts = restaurants.groupby("cuisine").id.count().reset_index()

#print(cuisine_counts)