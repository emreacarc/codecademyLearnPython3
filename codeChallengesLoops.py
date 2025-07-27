### Dvisible By Ten

#Write your function here
def divisible_by_ten(nums):
  counter = 0
  for index in nums:
    if index % 10 == 0:
      counter += 1
  return counter

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


### Greeting List
#Write your function here
def add_greetings(names):
  greeting_list = []
  for i in names:
    greeting_list.append("Hello, " + i)
  return greeting_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

### Delete Starting Even Numbers
#Write your function here
def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


### Odd Indices List
#Write your function here
def odd_indices(my_list):
  odd_indices_list = []
  for i in my_list:
    if my_list.index(i) % 2 == 1:
      odd_indices_list.append(i)
  return odd_indices_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


### Exponents
#Write your function here
def exponents(bases, powers):
  powered_list = []
  for i in bases:
    for z in powers:
      powered = i ** z
      powered_list.append(powered)
  return powered_list
      
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))



