# Question 1
s = input("Enter your string: ")
c = input("Enter the character that you want to find: ") 
print(s.count(c)) 

# output 1
Enter your string: hey hey hello hey hi 
Enter the character that you want to find: hey
3



# Question 2 
day = int(input("Day: "))
month = int(input("Month: ")) 
year = int(input("Year: ")) 

if year % 400 == 0:
    leap_year = True 
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else: 
        month_length = 28

else:
    month_length = 30 

if day < month:
    day += 1
else: 
    day = 1
    if month == 12:
        month = 1
        year += 1 
    else: 
        month += 1 

print("{}/{}/{}".format(day, month, year)) 

# Output 2 
Day: 28
Month: 2
Year: 1999
1/3/1999



# Question 3
li = [3, 9, 10] 
ans = [] 

for i in li:
    a = i*i 
    b = (i, a)
    ans.append(b) 

print(ans) 

# Output 3
[(3, 9), (9, 81), (10, 100)]



# Question 4
g = int(input("Enter your grade: "))

if g == 10:
    p = "Outstanding" 
    l = "A+" 
elif g == 9:
    p = "Excellent"
    l ="A" 
elif g == 8:
    p = "Very Good" 
    l = "B+" 
elif g == 7:
    p = "Good" 
    l = "B" 
elif g == 6:
    p = "Average" 
    l = "C+" 
elif g == 5:
    p = "Below Average" 
    l = "C" 
elif g == 4:
    p = "Poor" 
    l = "D" 

print("Your Grade is", l, "and", p, "Performance.")  

# Output 4
Enter your grade: 9
Your Grade is A and Excellent Performance.



# Question 5
s = "ABCDEFGHIJK"
j = 0
while len(s) - j*2 >= 1:
    print(" "*j + s[0 : len(s) - j*2])
    j += 1 

# output 5
ABCDEFGHIJK
 ABCDEFGHI
  ABCDEFG
   ABCDE
    ABC
     A
     



# Question 6
dict1 = {}
while True:                                                                                                        
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? ")
        if more_data in ("N","n","No","no","NO"):
            more_data = 0
            break
        elif more_data in ("Y","y","Yes","yes","YES"):
            more_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if more_data == 0:
        break
print("\na. Student Details:")                                                                                
for i in dict1:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                               
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                               
for i in dict2:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                           
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                
for i in dict3:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict3[i],i))
print("\nd. ", end="")                                                                                   
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is \033[1m%s\033[0m" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue
        
         


# Question 7
n = int(input("Enter the number of terms: ")) 
num1 = 0 
num2 = 1
series = 0
li = []

for i in range(n):
    print(series, end = ' ')
    li.append(series) 
    num1 = num2 
    num2 = series
    series = num1 + num2 

print()

a = sum(li) / len(li) 
print("Average of your fibannaci sequence is", a)

# Output 7
Enter the number of terms: 10
0 1 1 2 3 5 8 13 21 34 
Average of your fibannaci sequence is 8.8



# Question 8
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)

# Ouptut 
a. Set of all elements that are in Set1 and Set2 but not both: {1, 3, 5, 6, 8}
b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3: {17, 3, 6, 8, 9, 13}
c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3: {1, 2, 4, 5}
d. Set of all integers in the range 1 to 10 that are not in Set1: {6, 7, 8, 9, 10}
e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3: {10, 7}
