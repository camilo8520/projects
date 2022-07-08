
import pandas as pd
import numpy as np

inventory = pd.read_csv("2_inventory/inventory.csv")

#select Staten Island location
staten_island = inventory.iloc[:10]

#products sold at Staten Island location
product_request = staten_island.product_description

#types of seed sold at the Brooklyn location
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]

#new colum = inventory, True if quantity > 0 else False
inventory["in_stock"] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)

#value of current inventory
inventory["total_value"] = inventory.apply(lambda row: row.price * row.quantity, axis=1)

#Combine product_type and product_description into a single string
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

# new colum = full_description, is the complete description of each product
inventory["full_description"] = inventory.apply(combine_lambda, axis=1)

#print(inventory.head(10))