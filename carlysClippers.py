hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price
number_of_prices = len(prices)
average_price = total_price / number_of_prices
print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

i = range(len(hairstyles))
for index in i:
  revenue = prices[index] * last_week[index]
  total_revenue += revenue
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
