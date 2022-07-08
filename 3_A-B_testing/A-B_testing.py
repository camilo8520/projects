import pandas as pd

ad_clicks = pd.read_csv('3_A-B_testing/ad_clicks.csv')

#how many view came from each utm_source
#print(ad_clicks.groupby("utm_source").user_id.count().reset_index())

#True is someone actually clicked on the add
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()

#percent od people who clickedon adds from utm_source
#first, group utm_source and is_click
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"])["user_id"].count().reset_index
#second, pivot the table so is_click are columns, utm_spurce are index and user:id are values
clicks_pivot = clicks_by_source().pivot(columns="is_click", index="utm_source", values="user_id")
#third, create new column called percent_clicked which is equal to the percent of users who clicked on the add from each utm_source
clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot)

experimentalAB = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
#print(experimentalAB)

#amount of users that clicked on add A or add B
a_vs_b = ad_clicks.groupby(["experimental_group", "is_click"])["user_id"].count().reset_index
a_vs_b_pivot= a_vs_b().pivot(columns="is_click", index="experimental_group", values="user_id").reset_index()
#print(a_vs_b_pivot)

#compare experimental grups by day of the week
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]


#calculate the percentage of user who clicked on the add on a specific day

a_percentage = a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()
#print(a_percentage)
a_per_pivot = a_percentage.pivot(columns="is_click", index="day", values="user_id").reset_index()
#print(a_per_pivot)
a_per_pivot["percent_clicked"] = a_per_pivot[True] / (a_per_pivot[True] + a_per_pivot[False])
#print(a_per_pivot)



b_percentage = b_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()
#print(b_percentage)
b_per_pivot = b_percentage.pivot(columns="is_click", index="day", values="user_id").reset_index()
#print(b_per_pivot)
b_per_pivot["percent_clicked"] = b_per_pivot[True] / (b_per_pivot[True] + b_per_pivot[False])
#print(b_per_pivot)