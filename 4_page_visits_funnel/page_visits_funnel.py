from numpy import NaN
import pandas as pd

visits = pd.read_csv("4_page_visits_funnel/visits.csv")
cart = pd.read_csv("4_page_visits_funnel/cart.csv")
checkout = pd.read_csv("4_page_visits_funnel/checkout.csv")
purchase = pd.read_csv("4_page_visits_funnel/purchase.csv")


#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

#Combine visits and cart
visits_cart = pd.merge(visits, cart, how="left")

#total users
visits_cart_rows = len(visits_cart)

#Users that did not add items to cart
null_cart_time = len(visits_cart[visits_cart.cart_time.isnull()])

#percentage of user that did not add anything in the cart
print(null_cart_time / visits_cart_rows)



#Combine cart and checkout
cart_checkout = pd.merge(cart, checkout, how="left")

#Users that did not checkout
null_checkout_time = len(cart_checkout[cart_checkout.checkout_time.isnull()])

#total users that added to cart
cart_checkout_rows = len(cart_checkout)

#percentage of user that add to the cart but not checkout
print(null_checkout_time / cart_checkout_rows)



#Combine checkout and purchase
checkout_purchase = pd.merge(checkout, purchase, how="left")

#Users that did not purchase
null_purchase_time = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])

#total users that checkout
checkout_purchase_rows = len(checkout_purchase)

#percentage of user who made it to checkout but did not purchase
print(null_purchase_time / checkout_purchase_rows)



all_data = visits.merge(cart, how="left").merge(checkout, how="left").merge(purchase, how="left")

#all_data["total_time"] = all_data.purchase_time - all_data.visit_time


