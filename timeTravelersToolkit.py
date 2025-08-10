from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_time = dt.now()
print(dt.strftime(current_time, "%d %b, %Y"))

target_year = 2011
multiplier_by_year = 275
base_cost = Decimal("550")
delta_year = current_time.year - target_year
final_cost = base_cost + (delta_year * multiplier_by_year)
print(final_cost)




####
def generate_time_travel_message(year, destination, cost):
  return "Your time travel destination is {}. And the year you are going is {}. Lastly total cost you will pay: {}".format(destination, year, cost)
