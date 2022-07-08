import pandas as pd

df = pd.read_csv("6_getting_familiar_with_farmburg\clicks.csv")

df["is_purchase"] = df.click_day.apply(lambda x: "Purchase" if pd.notnull(x) else "No Purchase")

purchase_counts = df.groupby(["group", "is_purchase"])["user_id"].count().reset_index()

#print(purchase_counts)

contingency = [[316, 1350],
               [183, 1483],
               [83, 1583]]

               
               
num_visits = len(df)
print(num_visits)

p_clicks_099 = ((1000/0.99))/num_visits

p_clicks_199 = ((1000/1.99))/num_visits

p_clicks_499 = ((1000/4.99))/num_visits


