#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1.TO ADD NEW ELEMENTS TO THE END OF THE LIST
my_list = [1,2,3]
new_element = 4
my_list.append(new_element)
print(my_list)


# In[3]:


# 2. reverse the elements 
my_list =[1,2,3,4]
my_list.reverse()
print(my_list)


# In[5]:


# 3.same list multiple times display
my_list =[1,2,3]
num_times =4 # number of times to display 
for i in range (num_times):
    print(my_list)


# In[7]:


# 4.concatenate the list
list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2
print(concatenated_list)


# In[8]:


# 5.sort elements in ascending order 
my_list = [1,4,3,9,6]
my_list.sort()
print(my_list)


# In[12]:


# 2.2 to add new elements to end the tuples
my_tuple =(1,2,3)
new_element = 4
new_tuple = my_tuple+(new_element,)
print(new_tuple)


# In[31]:


#2.3 reverse elements in tuple 
my_tuple =(1,2,3,4)
t=my_tuple[::-1]
print(t)


# In[32]:


# 2.4 same tuple multiple times display
my_tuple =(1,2,3)
num_times =4 # number of times to display 
for i in range (num_times):
    print(my_tuple)


# In[15]:


# 4.concatenate the tuple
tuple1 = (1,2,3)
tuple2 = (4,5,6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)


# In[16]:


# 5.sort elements in ascending order 
my_tuple = (1,4,3,9,6)
my_tuple.sort()
print(my_tuple)


# In[17]:


# 3 .1 list with integers
my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list)


# In[18]:


# 3 .2 last number displaying 
my_list=[1,2,3,4,5,6,7,8,9,10]
last_number = my_list[-1]
print(last_number)


# In[19]:


# 3.3 command for displaying values in the list 
my_list=[1,2,3,4,5,6,7,8,9,10]
subset=my_list[0:4]
print(subset)


# In[20]:


# 3.4 command for displaying values in the list 
my_list=[1,2,3,4,5,6,7,8,9,10]
subset=my_list[2:]
print(subset) 


# In[21]:


# 3.5 command for displaying values in the list 
my_list=[1,2,3,4,5,6,7,8,9,10]
subset=my_list[:6]
print(subset)


# In[23]:


#4.1 to display elements 10 and 50 
tuple1 =(10,50,20,40,30)
element1 = tuple1[0]
print(element1)
element2 = tuple1[1]
print(element2)


# In[24]:


#4.2 length of tuple 
my_tuple =(10,50,20,40,30)
print(len(my_tuple))


# In[26]:


#4.3  max of tuple 
my_tuple =(10,50,20,40,30)
print(max(my_tuple))


# In[27]:


#4.4 adding of tuple 
my_tuple =(10,50,20,40,30)
print(sum(my_tuple))


# In[33]:


# 4.5 same tuple multiple times display
my_tuple =(10,50,20,40,30)
num_times =4 # number of times to display 
for i in range (num_times):
    print(my_tuple)


# In[34]:


#5.1 calculating length of string 
my_string=" hello world"
print(len(my_string))


# In[35]:


#5.2 reverse words in strings
my_string="hello world"
words = my_string.split()
reversed_words = words[::-1]
reversed_string =''.join(reversed_words)
print(reversed_string)


# In[36]:


# 5.4 concatenation of strings  
string1 = "hello"
string2="world"
concatenated_string=string1+string2
print(concatenated_string)


# In[39]:


# 5.5 slicing to display  
str1 = "south india"
India_part = str1[6:]
print(India_part)


# In[40]:


#5.3 same string multiple times
my_string = "hello world!"
num_times=3
repeated_string = my_string*num_times
print(repeated_string)


# In[42]:


#6.1 creating dictnoary
my_dict ={
    "name":"john",
    "age":30,
    "city":"new york"
}


# In[43]:


#6.2 accesing values and keys  
keys = my_dict.keys()
print("keys:",keys)
values = my_dict.values()
print("values:",values)
for key,value in my_dict.items():
    print("Key:",key,"value:",value)


# In[44]:


# 6.3 update the dict using function 
   def update_dict(my_dict):
   my_dict["new_key"] = "new_value"  # Add or update a key-value pair
   return my_dict

my_dict = {
   "name": "John",
   "age": 30,
   "city": "New York"
}


updated_dict = update_dict(my_dict)

print(updated_dict)


# In[45]:


#6.4 clear and delete dict 
del my_dict["age"]
my_dict.clear()


# In[46]:


# 7 insert to number to any position 
my_list = [1, 2, 3, 4, 5]
element_to_insert = 99
position_to_insert = 2  
my_list.insert(position_to_insert, element_to_insert)
print(my_list)


# In[47]:


# 8 program to delete an from a list 
my_list = [1, 2, 3, 4, 5]
index_to_delete = 2  
del my_list[index_to_delete]
print(my_list)


# In[48]:


#9 displaying 1 to 100 
for number in range(1, 101):
    print(number)


# In[49]:


#10.sum of all times in a tuple 
my_tuple = (1, 2, 3, 4, 5)
sum_of_elements = sum(my_tuple)
print("Sum of elements:", sum_of_elements)


# In[3]:


#11
function_dict = {
   "Square": lambda x: x ** 2,
   "Cube": lambda x: x ** 3,
   "Squareroot": lambda x: x ** 0.5
}


x = float(input("Enter a number: "))

total = 0
for function_name, func in function_dict.items():
   result = func(x)
   total += result
   print(f"{function_name}({x}) = {result}")
print("Sum of outputs:", total)


# In[5]:


#12 find the words from the list that are second character in upper case  
words = ['hello', 'Dear', 'how', 'ARe', 'You']
result_words = []
for word in words:
   if len(word) >= 2 and word[1].isupper():
       result_words.append(word)
print("Words with a second uppercase character:", result_words)


# In[3]:


#13 weight on the moon finding 
WeightOnEarth = {'John': 45, 'Shelly': 65, 'Marry': 35}
GMoon = 1.622
GEarth = 9.81
WeightOnMoon = map(lambda weight: (weight * GMoon) / GEarth, WeightOnEarth.values())
WeightOnMoonDict = dict(zip(WeightOnEarth.keys(), WeightOnMoon))
for name, weight in WeightOnMoonDict.items():
    print(f"{name}'s weight on the Moon: {weight} kg")


# # control structures
# 

# In[7]:


# 1 FIRST N PRIME NUMBERS 
def Prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)  
  
N=int(input("Enter N:"))  
i=2 
lst=[] 
while(1):  
    if(Prime(i)):  
        lst.append(i) 
        if(len(lst)==N): 
            break 
    i+=1 
print("First "+str(N)+" Prime numbers are:",end="") 
print(*lst)


# In[4]:


#2.salary of an employee
basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
ta = float(input("Enter TA: "))
da = float(input("Enter DA: "))
gross_salary = basic_salary + hra + ta + da
tax = 0.10 * gross_salary
net_salary = gross_salary - tax
print(f"Gross Salary: {gross_salary}")
print(f"Tax: {tax}")
print(f"Net Salary: {net_salary}")


# In[5]:


#3 search string in the list 
l = [1, 2.0, 'have', 'a', 'geeky', 'day']
s = 'geeky' 
if s in l:
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')


# In[6]:


#4 calculation of upper case and lower case 
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# In[9]:


#5 sum of add numbers and even numbers
sum_odd = 0
sum_even = 0

for number in range (12,38):
    if number%2== 0:
        sum_even+= number
    else:
        sum_odd+= number
print ("sum of even numbers ",sum_even)
print("sum of odd numbers",sum_odd)


# In[10]:


#6 print  a table for any number 
number = int(input ("Enter the number of which the user wants to print the multiplication table: "))          
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)


# In[13]:


#7 sum of first 10 prime numbers 
last_number = 10
print ("We will find the sum of prime numbers in python upto", last_number)
sum = 0
for number in range(2, last_number+1):
    i = 2
    for i in range(2, number):
        if (int(number % i) == 0):
            i = number
            break;
#Only if the number is a prime number, continue to add it.
    if i is not number:
        sum = sum + number
print("\nThe sum of prime numbers in python from 1 to ", last_number, " is :", sum)


# In[14]:


#8 arthamatic using nested if 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the arithmetic operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':

    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero is not allowed"
else:
    result = "Invalid operation"

print(f"Result: {result}")


# In[15]:


# 9 Python Program to convert temperature in celsius to fahrenheit

celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# In[16]:


#10.max and min number
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))


# In[17]:


#11.number of seconds in 30 day month 30 days 24 hrs
days_per_month = 30
hours_per_day = 24
minutes_per_hour = 60
seconds_per_minute = 60
total_seconds = days_per_month * hours_per_day * minutes_per_hour * seconds_per_minute
print(f"Number of seconds in a 30-day month: {total_seconds} seconds")


# In[18]:


#12.Python program to print the Number of seconds in Year
days=365
hours=24
minutes=60
seconds=60
print("Number of seconds in a year : ",days*hours*minutes*seconds)


# In[19]:


#13.Average speed of the train 

average_speed_mph = 150  
distance_miles = 414    


time_hours = distance_miles / average_speed_mph


print(f"It will take {time_hours:.2f} hours for the train to travel from London to Glasgow.")


# In[20]:


#14.days in each school year
days_in_each_school_year = 192
school_years = range(7, 12)
total_hours_in_school = 0
for year in school_years:
    total_hours_in_school += year * days_in_each_school_year * 6
print(f"Total hours spent in school from year 7 to year 11: {total_hours_in_school} hours")


# In[21]:


#15 youngest age of ram sam khan

ram_age = int(input("Enter Ram's age: "))
sam_age = int(input("Enter Sam's age: "))
khan_age = int(input("Enter Khan's age: "))


if ram_age >= sam_age and ram_age >= khan_age:
    eldest = "Ram"
    if sam_age <= khan_age:
        youngest = "Sam"
    else:
        youngest = "Khan"
elif sam_age >= ram_age and sam_age >= khan_age:
    eldest = "Sam"
    if ram_age <= khan_age:
        youngest = "Ram"
    else:
        youngest = "Khan"
else:
    eldest = "Khan"
    if ram_age <= sam_age:
        youngest = "Ram"
    else:
        youngest = "Sam"


print(f"The eldest among Ram, Sam, and Khan is {eldest}.")
print(f"The youngest among Ram, Sam, and Khan is {youngest}.")


# In[32]:


#16 rotate a list by right n times
n = 3

list_1 = [1, 2, 3, 4, 5, 6]
list_1 = (list_1[len(list_1) - n:len(list_1)] + list_1[0:len(list_1) - n])
print(list_1)


# In[26]:


#17.1 pattern factorial 
from math import factorial
n = 7
for i in range(n):
    for j in range(n-i+1): 
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    
    print()


# In[28]:


#17.2 pattern python 
str="PYTHON"
for i in range(0,6):
    print()
    for j in range(0,i+1):
        print(str[j], end=' ')


# In[29]:


#17.3 pattern 5 star
for i in range(1,6):
        print()
        for j in range(i):
             print("*", end= ' ')


# In[1]:


# 17.4 6 star pattern 
def triangle(n):
     
    
    k = n - 1
 
    
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = 5
triangle(n)


# In[ ]:




