my_name = "Emre"
first_initial = my_name[0]

first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[0:5]
temp_password = last_name[2:6]

# Concatenating
first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name):
  return first_name[0:3] + last_name[0:3]
new_account = account_generator(first_name, last_name)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]

temp_password = password_generator(first_name, last_name)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[-2:]

password = "theycallme\"crazy\"91"

def get_length(string1):
  counter = 0
  for i in string1:
    counter += 1
  return counter

def letter_check(word, letter):
  for i in word:
    if letter == i:
      return True
      break
  return False

def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False

def common_letters(string_one, string_two):
  common_list = []
  for i in string_one:
    if i in string_two and not i in common_list:
      common_list.append(i)
  return common_list













