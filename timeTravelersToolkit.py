from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module
from custom_module import generate_time_travel_message

current_time = dt.now()
print(dt.strftime(current_time, "%d %b, %Y"))
possible_destinations = ["Budapest", "Prague", "Dublin", "Edinburgh", "Antalya"]
target_destination = choice(possible_destinations)
target_year = randint(1993,2015)
multiplier_by_year = 275
base_cost = Decimal("550")
delta_year = current_time.year - target_year
final_cost = base_cost + (delta_year * multiplier_by_year)

message = generate_time_travel_message(target_year, target_destination, final_cost)
print(message)
