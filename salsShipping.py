weight = 41.5

# Ground Shipping
if weight <= 2.0:
  cost = weight * 1.50 + 20
elif weight <= 6.0:
  cost = weight * 3 + 20
elif weight <= 10.0:
  cost = weight * 4 + 20
elif weight > 10.0:
  cost = weight * 4.75 + 20

cost_ground_premium = cost + 125

print("Cost for Ground Shipping: " + str(cost))
print("Cost for Ground Shipping Premium: " + str(cost_ground_premium))

# Drone Shipping
if weight <= 2.0:
  cost = weight * 4.50
elif weight <= 6.0:
  cost = weight * 9
elif weight <= 10.0:
  cost = weight * 12
elif weight > 10.0:
  cost = weight * 14.25

print("Cost for Drone Shipping: " + str(cost))
