### Larger Sum
#Write your function here
def larger_sum(lst1, lst2):
  lst1_total = 0
  lst2_total = 0
  for i in lst1:
    lst1_total += i
  for i in lst2:
    lst2_total += i
  if lst1_total < lst2_total:
    return lst2
  else:
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

### Over 9000
#Write your function here
def over_nine_thousand(lst):
  lst_sum = 0
  if len(lst) == 0:
    return 0
  else:
    for i in lst:
      lst_sum += i
      if lst_sum > 9000:
        break 
    return lst_sum
    
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([]))
print(over_nine_thousand([3, 1000]))


### Max Num
#Write your function here
def max_num(nums):
  return max(nums)

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))


### Same Values
#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
  
 #Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


### Reversed List
#Write your function here
def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


