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


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

### String Methods
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title, poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author, poem_author_fixed)

line_one = "The sky has given over"
line_one_words = line_one.split()

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())
print(love_maybe_lines_stripped)
love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)


toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)


god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

def poem_title_card(title, poet):
  return "The poem {} is written by {}".format(title, poet)

print (poem_title_card("I Hear America Singing", "Walt Whitman"))














