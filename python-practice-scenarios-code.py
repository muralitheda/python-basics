# Python Programming

#########################################
## 🎯 Variables
#########################################

#1. Create two variables `x = 100` and `y = 10`, find their multiplication and division, and store the results in variables `z` and `z1`.
x = 100
y = 10
z = x * y
z1 = x / y
print("type(z):",type(z), "z:",z)
print("type(z1):", type(z1), "z1:", z1)

"""
type(z): <class 'int'> z: 1000
type(z1): <class 'float'> z1: 10.0
"""

#2. Create a variable `a = 2000`, divide `a` by `y` (from step 1), and reassign `a` with the divided result.
print()

a = 2000
a = a / y
print("type(a):",type(a),"a:",a)

"""
type(a): <class 'float'> a: 200.0
"""

#3. Prove Python is dynamically typed by creating `x: int = 100`, then assigning `y = str(x)` and printing the types of `x` and `y`.
print()

x: int = 100
y = str(x)
print("type(x):",type(x))
print("type(y):",type(y))

"""
type(x): <class 'int'>
type(y): <class 'str'>
"""

#4. Demonstrate Python’s dynamic inference feature with an example showing automatic datatype detection.
print()

code = 100
print("code=",code)
print("type(code)=",type(code))

code = "Hundred"
print("code=",code)
print("type(code)=",type(code))

code = 100/100
print("code=",code)
print("type(code)=",type(code))

code = [1,2,3,4]
print("code=",code)
print("type(code)=",type(code))

code = (1,2,3,4)
print("code=",code)
print("type(code)=",type(code))

code = {1,2,3,4}
print("code=",code)
print("type(code)=",type(code))

code = {"empid":1,"name":"jack"}
print("code=",code)
print("type(code)=",type(code))

code = True
print("code=",code)
print("type(code)=",type(code))

"""
code= 100
type(code)= <class 'int'>

code= Hundred
type(code)= <class 'str'>

code= 1.0
type(code)= <class 'float'>

code= [1, 2, 3, 4]
type(code)= <class 'list'>

code= (1, 2, 3, 4)
type(code)= <class 'tuple'>

code= {1, 2, 3, 4}
type(code)= <class 'set'>

code= {'empid': 1, 'name': 'jack'}
type(code)= <class 'dict'>

code= True
type(code)= <class 'bool'>
"""

#5. Prove Python is a strongly typed language using incompatible type operations.
print()

name = "Alan Harpor"
age = 40

print("name=",name,"type(name)=",type(name))
print("age=",age,"type(age)=",type(age))

#concatenate string + number is not possible
#concate_name_age = name + age # strongly typed

"""
name= Alan Harpor type(name)= <class 'str'>
age= 40 type(age)= <class 'int'>
TypeError: can only concatenate str (not "int") to str
"""

#6. Create variables `a, b, c, d` assigned with values `10, 20, 30, 40` respectively.
print()

a = 10
b = 20
c = 30
d = 40
print(f"a={a} b={b} c={c} d={d}")

# OR

a,b,c,d = 10,20,30,40
print(f"a={a} b={b} c={c} d={d}")

#7. Prove that Python variable names are case-sensitive.
print()

name = "Alan Harpor"
Name = "alan harpor"
print(f"name={name} | Name={Name}")

"""
name=Alan Harpor Name=alan harpor
"""

#8. Demonstrate that variable names cannot start with numbers or contain special characters (except `_`).
print()

_number = 100  # valid
number_ = 100  # valid
"""
1number = 100  # not valid
$number = 100  # not valid
num$ber = 100  # not valid
"""

#9. Show examples of using single, double, and triple quotes in Python.
print()

name = 'I cant wait'
print(name)
name = "I can't wait"
print(name)
name = """I 
can't 
wait
"""
print(name)

"""
I cant wait
I can't wait
I 
can't 
wait
"""

#10. Demonstrate examples using arithmetic, assignment, comparison, relational, and logical operators.
print()

a = 3
b = 2
c = 1

print(f"a = {a} | b = {b} | c = {c}")

print("Arithmetic Operations Examples:")
print("1. Addition(+)        : a+b+c = ",a+b+c)
print("2. Subtraction(-)     : a-b-c = ",a-b-c)
print("3. Multiplication(*)  : a*b*c = ",a*b*c)
print("4. Division(/)        : a/b/c = ",a/b/c)
print("5. Modulus(%)         : a%b   = ",a%b)
print("6. Exponentiation(**) : a**b  = ",a**b)
print("7. Floor Division(//) : a//b  = ",a//b)

print()
print("Relational Operator Examples:")
print("1. Equal To (==)                 : a == b = ",a == b)
print("2. Not Equal To (!=)             : a != b = ",a != b)
print("3. Greater Than (>)              : a > b  = ",a > b)
print("4. Less Than (<)                 : a < b  = ",a < b)
print("5. Greater Than and Equal To (>=): a >= b = ",a >= b)
print("6. Less Than and Equal To (<=)   : a <= b = ",a <= b)

print()
print("Logical Operators Examples:")
a = True
b = False
print(f"a = {a} | b = {b}")
print("1. AND (a and b) = ",a and b)
print("2. OR (a or b) = ",a or b)
print("3. NOT (not b) = ", not b)

print()
print("Assignment Operators Examples:")
a = 5
print("1. Simple Assignment (a = 5) = ", a)
a += 5
print("2. Add and Assign (a += 5) => (a = a + 5)      = ", a)
a = 5; a -= 5
print("3. Subtract and Assign (a -= 5) => (a = a - 5) = ", a)
a = 5; a *= 5
print("4. Multiply and Assign (a *= 5) => (a = a * 5) = ", a)
a = 5; a /= 5
print("5. Division and Assign (a /= 5) => (a = a / 5) = ", a)
a = 5; a %= 5
print("6. Modulus and Assign (a %= 5) => (a = a % 5)  = ", a)
a = 5; a **= 5
print("7. Exponentiation and Assign (a **= 5) => (a = a ** 5) = ", a)
a = 5; a //= 5
print("8. Floor Division and Assign (a //= 5) => (a = a // 5) = ", a)

"""
a = 3 | b = 2 | c = 1

Arithmetic Operations Examples:
1. Addition(+)        : a+b+c =  6
2. Subtraction(-)     : a-b-c =  0
3. Multiplication(*)  : a*b*c =  6
4. Division(/)        : a/b/c =  1.5
5. Modulus(%)         : a%b   =  1
6. Exponentiation(**) : a**b  =  9
7. Floor Division(//) : a//b  =  1

Relational Operator Examples:
1. Equal To (==)                 : a == b =  False
2. Not Equal To (!=)             : a != b =  True
3. Greater Than (>)              : a > b  =  True
4. Less Than (<)                 : a < b  =  False
5. Greater Than and Equal To (>=): a >= b =  True
6. Less Than and Equal To (<=)   : a <= b =  False

Logical Operators Examples:
a = True | b = False
1. AND (a and b) =  False
2. OR (a or b) =  True
3. NOT (not b) =  True

Assignment Operators Examples:
1. Simple Assignment (a = 5) =  5
2. Add and Assign (a += 5) => (a = a + 5)      =  10
3. Subtract and Assign (a -= 5) => (a = a - 5) =  0
4. Multiply and Assign (a *= 5) => (a = a * 5) =  25
5. Division and Assign (a /= 5) => (a = a / 5) =  1.0
6. Modulus and Assign (a %= 5) => (a = a % 5)  =  0
7. Exponentiation and Assign (a **= 5) => (a = a ** 5) =  3125
8. Floor Division and Assign (a //= 5) => (a = a // 5) =  1
"""

#########################################
## 🎯 Conditional Structures
#########################################
#11. Write a program to find the greatest of three numbers.
print()

a = 1; b=2; c=3
print(f"a = {a} | b = {b} | c = {c}")
if a > b and a > c:
    print("{a} is greater than {b} and {c}")
elif b > a and b > c:
    print("{b} is greater than {a} and {c}")
elif c > a and c > b:
    print("{c} is greater than {a} and {b}")
else:
    pass

#12. Write a single program to check if a number is even or negative and print the result as: “Even but not negative”, “Not even but negative”, “Neither even nor negative”
print()

numbers = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
print(f"numbers:{numbers}")

for number in numbers:
    if number % 2 == 0 and number > 0:
        print(f"The given number {number} is even and positive.")
    elif number % 2 == 0 and number < 0:
        print(f"The given number {number} is even and negative.")
    elif number % 2 != 0 and number > 0:
        print(f"The given number {number} is odd and positive.")
    elif number % 2 != 0 and number < 0:
        print(f"The given number {number} is odd and negative.")
    else:
        print(f"The given number {number} is zero.")

#13. Write a nested `if-else` structure to print course fees:
"""
* Big Data → 25000
* Spark → 15000
* Data Science →
  * Machine Learning → 25000
  * Deep Learning → 45000
  * Both → 50000
"""

print('''
1. BigData
2. Spark
3. DataScience
  4. MachineLearning
  5. DeepLearning
  6. Both
''')
print("Enter the course name or number:")
course = input()
print("input => course = ",course)

fee = 0

# Check if the course is numeric
if course.isdigit():
    course_int = int(course)
else:
    course_int = None

# Logic
if course_int == 1 or course.lower() == "bigdata" :
    fee = 25000
    course = "Big Data"
elif course_int == 2 or course.lower() == "spark" :
    fee = 15000
    course = "Spark"
elif course_int == 3 or course.lower() == "datascience" :
    fee = 70000
    course = "Data Science"
elif course_int == 4 or course.lower() == "machinelearning" :
    fee = 25000
    course = "Machine Learning"
elif course_int == 5 or course.lower() == "deeplearning" :
    fee = 45000
    course = "Deep Learning"
elif course_int == 6 or course.lower() == "both" :
    fee = 70000
    course = "Machine Learning & Deep Learning"
else:
    pass

if fee != 0:
    print(f"Entered course '{course}' fee is Rs.{fee}.")
else:
    print("Entered the course is not available.")

"""
1. BigData
2. Spark
3. DataScience
  4. MachineLearning
  5. DeepLearning
  6. Both

Enter the course name or number:
3
input => course =  3
Entered course 'Data Science' fee is Rs.70000.
"""

#14. Check whether a given string is a palindrome using a reverse function.
print()

print("Enter the word to check whether it is a plaindrome or not:")
word = "madam"##input()

reversed_word = ""
for i in word:
    reversed_word = i + reversed_word
# OR
reversed_word = "".join(reversed(word))
print(f"reversed_word:{reversed_word}")


if word == reversed_word:
    print(f"The entered the word '{word}' is a plaindrome.")
else:
    print(f"The entered the word '{word}' is not a plaindrome.")

"""
Enter the word to check whether it is a plaindrome or not:
madam
reversed_word:madam
The entered the word 'madam' is a plaindrome.
"""

#15. Check whether `x = 100` is an integer or a string using functions like `isinstance()` or `type()`.
print()

x = 'hello'
print("Entered the value:",x)

if isinstance(x, int):
    print(f"{x} is an integer.")
elif isinstance(x, str):
    print(f"{x} is a string.")

# OR
if type(x) == int :
    print(f"{x} is an integer.")
elif type(x) == str:
    print(f"{x} is a string.")

"""
Entered the value: hello
hello is a string.
hello is a string.
"""

#########################################
## 🎯 Control Statements
#########################################
#16. Write a program using for loop to print even numbers and odd numbers in the below range of data (generate using range function) [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] output should be with even as 6,8,10,12,14,16,18,20 and odd as 5,7,9,11,13,15,17,19.
print()

numbers = list(range(5,20))
print("Numbers:",numbers)

oddNumbers = ""
evenNumbers = ""
for i in numbers:
  if i%2 != 0 :
      oddNumbers = oddNumbers + str(i) + ","
  else:
      evenNumbers = evenNumbers + str(i) + ","

print(f"oddNumbers: {oddNumbers}")
print(f"evenNumbers: {evenNumbers}")

"""
Numbers: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
oddNumbers: 5,7,9,11,13,15,17,19,
evenNumbers: 6,8,10,12,14,16,18,
"""

#17. Write a while loop to loop from 0 till 21 with the increment of 3, the result should be exactly 3,6,9,12,15,18 and store this result in a list
print()

x = 0
result = []
while x < 21 :
    if x%3 == 0 and x !=0:
        result.append(x)
    x += 1
print("result:",result)

"""
result: [3, 6, 9, 12, 15, 18]
"""

#18. Write a for or while loop to print the cube of 4, result should be 4*4*4=64 (initiate some variable outside the loop with 4 and loop through 3 times to achieve the result)
print()

number = int(input("Enter the number:"))
cubeNumber = int(input("Enter the cube number:"))
x = 1
result = 1
while x <= cubeNumber:
    result = result * number
    x += 1
print("result:",result)

"""
Enter the number:4
Enter the cube number:4
result: 256
"""

#19. Create a list as sal_lst=[10000,20000,30000,10000,15000], loop through the list and add 1000 bonus to the salary and store in another list sal_bonus_lst=[11000,21000,31000,11000,16000] then store the bonus applied salary in another list where sal>11000
print()

sal_lst=[10000,20000,30000,10000,15000]
revised_sal_lst = []
revised_sal = 0
bonus = 1000
sal_gt_11000 = []

for i in sal_lst:
    revised_sal = i + bonus
    revised_sal_lst.append(revised_sal)
    if revised_sal > 11000:
        sal_gt_11000.append(revised_sal)

print("revised_sal_lst:",revised_sal_lst)
print("sal_gt_11000:",sal_gt_11000)

"""
revised_sal_lst: [11000, 21000, 31000, 11000, 16000]
sal_gt_11000: [21000, 31000, 16000]
"""

#20. Write a do while loop to print “Inception Technologies” n number of times as per the input you get from the user. Minimum it has to be printed at least one time regardless of the user input.
print()

text = "Inception Technologies"
nooftimes = int(input("How many times you want to print? "))

x = 1
if nooftimes <= 0:
    nooftimes = 1

while x <= nooftimes:
    print(text)
    x += 1

"""
How many times you want to print? 2
Inception Technologies
Inception Technologies
"""

#21. From the given list of list of elements produce the following output using nested for loop lst1=[[10,20],[30,40,50],[60,70,80]], calculate the sum of all number, calculate the min value and the max value of all the elements in the lst1.
print()

startNumber = 10
reqlist = [2,3,4]
lst1 = []
value =0

for length in reqlist:
    x = 1
    tmpList = []
    while x <= length:
        x += 1
        value = value + 10
        tmpList.append(value)
    lst1.append(tmpList)

print("lst1: ",lst1)


allNumbers = []
for numbers in lst1:
    length = len(numbers)
    if length >1:
        x = 1
        while x <= length:
            x += 1
            for number in numbers:
                allNumbers.append(number)
    elif length ==1:
        allNumbers.append(number)
    else:
        pass

print("Sum of all numbers: ",allNumbers)
print("Min value from the list: ",min(allNumbers))
print("Max value from the list: ",max(allNumbers))

"""
lst1:  [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
Sum of all numbers:  [10, 20, 10, 20, 30, 40, 50, 30, 40, 50, 30, 40, 50, 60, 70, 80, 90, 60, 70, 80, 90, 60, 70, 80, 90, 60, 70, 80, 90]
Min value from the list:  10
Max value from the list:  90
"""

#22. Create a looping construct to print the multiplication table for 3 up to 10.
print()

tableOf=int(input("Which multiplication do you want? "))
upToMax=int(input("Evaluate up to how many numbers? "))
upToSeq=1

while upToSeq <= upToMax:
    print(f"{upToSeq} * {tableOf} = {upToSeq*tableOf}")
    upToSeq += 1

"""
Which multiplication do you want? 2
Evaluate up to how many numbers? 5
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
5 * 2 = 10
"""

##################################################
## 🎯 Collections: List, Dictionary, Tuple, and Set
##################################################
#23. Create a list with a range of 10 values starting from 2 to 11 and prove mutability by updating the 3rd element with 100 and prove resizable properties by adding 100 in the 5th position.
print()

rangeList = list(range(2,11))
print("rangeList: ",rangeList)

#Updating 3rd element with 100
rangeList[2]=100
print("updated rangeList: ",rangeList)

#Inserting a new value 100 in the 5th position
rangeList.insert(4,100)
print("resized rangeList: ",rangeList)

"""
rangeList:  [2, 3, 4, 5, 6, 7, 8, 9, 10]
updated rangeList:  [2, 3, 100, 5, 6, 7, 8, 9, 10]
resized rangeList:  [2, 3, 100, 5, 100, 6, 7, 8, 9, 10]
"""

#24. Create a tuple of 2 fields eg. ("Inception","Technologies","Pvt","Ltd"), prove immutability and non-resizable nature, access the 2nd and 4th fields and store in another tuple.
print()

namesTuple = ("Inception","Technologies","Pvt","Ltd")
# namesTuple[0]= "The" # Tuples don't support item assignment
# .append() or .insert() are not available for tuples

namesList = []
i = 0
length = len(namesTuple)

for name in namesTuple:
    if i in (1,3):
         namesList.append(name)
    i += 1
print("filteredNames: ",namesList)

"""
filteredNames:  ['Technologies', 'Ltd']
"""

#25. Convert the list of tuples [("Inception","Technologies"),("Apple","Incorporation")] to list of dictionary type, using for loop as given below [{"Inception":"Technologies"},{"Apple":"Incorporation"}] , once the list of dictionary is arrived print only "Incorporation" by passing "Apple" as a key using dict["Apple"] and dict.get("Apple") and try with dict["Apple1"] and dict.get("Apple1") then find the difference between get and using[] notation.
print()

listOfTuples = [("Inception","Technologies"),("Apple","Incorporation")]
#dictOfTuples = dict(listOfTuples)
#print("dictOfTuples: ",dictOfTuples)

dictOfTuples = {}
for list1 in listOfTuples:
    i = 0
    key = ""
    value = ""
    for element in list1:
        if i == 0:
            key = element
        elif i == 1:
            value = element
        else:
            pass
        i += 1
    dictOfTuples[key]=value

print("dictOfTuples: ",dictOfTuples)
print("dictOfTuples['Apple']: ",dictOfTuples['Apple'])
print("dictOfTuples['Inception']: ",dictOfTuples['Inception'])
#print("dictOfTuples['Apple1']: ",dictOfTuples['Apple1'])            # This will throw an error. Alternate is dictOfTuples.get('Apple1').
#print("dictOfTuples['Inception1']: ",dictOfTuples['Inception1'])    # This will throw an error. Alternate is dictOfTuples.get('Inception1').

print("dictOfTuples.get('Apple'): ",dictOfTuples.get("Apple"))
print("dictOfTuples.get('Inception'): ",dictOfTuples.get("Inception"))
print("dictOfTuples.get('Apple1'): ",dictOfTuples.get("Apple1"))
print("dictOfTuples.get('Inception1'): ",dictOfTuples.get("Inception1"))

"""
dictOfTuples:  {'Inception': 'Technologies', 'Apple': 'Incorporation'}
dictOfTuples['Apple']:  Incorporation
dictOfTuples['Inception']:  Technologies
dictOfTuples.get('Apple'):  Incorporation
dictOfTuples.get('Inception'):  Technologies
dictOfTuples.get('Apple1'):  None
dictOfTuples.get('Inception1'):  None
"""

#26. Create a list of tuple as given below and delete all duplicate tuples of the list  lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]
print()

lst=[("Inception","Technologies"),("Apple","Incorporation"),("Inception","Technologies"),("Inception","Technologies")]
print("OriginalList: ",lst)
distinct_set = set(lst)
print("distinct_set: ",distinct_set)
distinct_list = list(distinct_set)
print("distinct_list: ",distinct_list)

"""
OriginalList:  [('Inception', 'Technologies'), ('Apple', 'Incorporation'), ('Inception', 'Technologies'), ('Inception', 'Technologies')]
distinct_set:  {('Apple', 'Incorporation'), ('Inception', 'Technologies')}
distinct_list:  [('Apple', 'Incorporation'), ('Inception', 'Technologies')]
"""

#27. Append a new tuple `("Intel", "Corp")` to the de-duplicated list.
print()

distinct_list.append(("Intel", "Corp"))
print("distinct_list: ",distinct_list)

"""
distinct_list:  [('Apple', 'Incorporation'), ('Inception', 'Technologies'), ('Intel', 'Corp')]
"""

#28. Convert the lst_dict= [{"Inception":"Technologies"},{"Apple":"Incorporation"}] to lst1=["Inception","Apple"] , think about using for loop, list() function, keys function and list append functions to achieve this.
print()

lst_dict= [{"Inception":"Technologies"},{"Apple":"Incorporation"}]
final_list = []
for item in lst_dict:
    for key,value in item.items():
        final_list.append(key)
print("final_list: ",final_list)

"""
final_list:  ['Inception', 'Apple']
"""


#29. Create a list of values lst=[10,20,40,30,20], find the first, last values of the list, sort the list in ascending order, sort in descending order, print the minumum and maximum values of the descending sorted list, find the sum of all elements in the list, remove the number 30 and 20 from the list.
print()

lst = [10,20,40,30,20]
print(f"Original List: {lst}")

# 1. Find the first, last values of the list
length = len(lst)
print(f"First value: {lst[0]} Last value: {lst[length-1]}")

# 2. Sort the list in ascending order
lst.sort(reverse=False)
print(f"Sorted list ascending: ",lst)

# 3. Sort the list in decending order
lst.sort(reverse=True)
print(f"Sorted list decending: ",lst)

# 4. Minumum and maximum values of the descending sorted list
print(f"Minimum value: {min(lst)} Maximum value: {max(lst)}")

# 5. Find the sum of all elements in the list
print(f"Sum of all the elements: {sum(lst)}")

# 6. Remove the number 30 and 20 from the list
lst.remove(30)
lst.remove(20)
print(f"After remove the number 30 and 20 from the list: {lst}")

"""
Original List: [10, 20, 40, 30, 20]
First value: 10 Last value: 20
Sorted list ascending:  [10, 20, 20, 30, 40]
Sorted list decending:  [40, 30, 20, 20, 10]
Minimum value: 10 Maximum value: 40
Sum of all the elements: 120
After remove the number 30 and 20 from the list: [40, 20, 10]
"""

#30. Perform the same operations from step 29 on a tuple `(10,20,40,30,20)`.
print()

lst = (10,20,40,30,20)
print(f"Original List: {lst}")

# 1. Find the first, last values of the list
length = len(lst)
print(f"First value: {lst[0]} Last value: {lst[length-1]}")

# 2. Sort the list in ascending order
sorted_lst = sorted(lst)
print(f"sorted_lst ascending: {sorted_lst}")

# 3. Sort the list in decending order
sorted_lst = sorted(lst,reverse=True)
print(f"sorted_lst decending: {sorted_lst}")

# 4. Minumum and maximum values of the descending sorted list
print(f"Min value: {min(sorted_lst)} Max value: {max(sorted_lst)}")

# 5. Find the sum of all elements in the list
print(f"Sum of all elements: {sum(sorted_lst)}")

# 6. Remove the number 30 and 20 from the list
sorted_lst.remove(30)
sorted_lst.remove(20)
print(f"Final list: {sorted_lst}")

"""
Original List: (10, 20, 40, 30, 20)
First value: 10 Last value: 20
sorted_lst ascending: [10, 20, 20, 30, 40]
sorted_lst decending: [40, 30, 20, 20, 10]
Min value: 10 Max value: 40
Sum of all elements: 120
Final list: [40, 20, 10]
"""

#31. Convert the string `"Inception Technologies Pvt Ltd"` to a list `['Inception', 'Technologies', 'Pvt', 'Ltd']`.
print()

name = "Inception Technologies Pvt Ltd"
nameList = name.split(sep=" ")
print("name: ",name)
print("nameList: ",nameList)

#32. Given
"""
    emplstlst = [["1", ("Arun","Kumar"), "10000"], ["2", ("Bala","Mohan"), "12000"]]

    Perform:
    a. Convert the first sublist to a tuple.
    b. Reverse the first and last name of the second element.
    c. Convert the entire list into tuples of tuples.
    d. Calculate the total salary.
"""
print()

emplstlst = [["1", ("Arun","Kumar"), "10000"], ["2", ("Bala","Mohan"), "12000"]]

# a. Convert the first sublist to a tuple.
tupFirstList = tuple(emplstlst[0])
print(f"First tuple sublist: ",tupFirstList)

# b. Reverse the first and last name of the second element.
secElement = sorted(emplstlst[1][1],reverse=True)
print(f"secElement: {secElement}")

# c. Convert the entire list into tuples of tuples.
emplstlst_tuple = tuple(emplstlst)
print(f"emplstlst_tuple: {emplstlst_tuple}")

# d. Calculate the total salary.
sal = 0
for item in emplstlst:
    sal = sal + int(item[2])

print(f"Total Sal: {sal}")

#########################################
## 🎯 Functions
#########################################
#33. Create `def` functions to generalize the logic from steps 11–15 and 26–32.
#34. Call the function from step 11 using both positional and keyword arguments.
#35. Write a calculator function that takes three parameters (`int`, `int`, `str`) to perform add/sub/mul/div. Default the 3rd argument to `"add"`.
#36. Modify the calculator to return a tuple of all operations `(add, sub, mul, div)` when the 3rd argument is `"all"`.
#37. Write a function that accepts a string like `"inceptez technologies"` and returns:
"""
* Capitalized
* Uppercase
* Length
* Word count
* Ends with “s” (True/False)
* Replace ‘e’ with ‘a’
"""

#38. Create a `promo` function with three parameters: `amount`, `offer_percent`, and `offer_cap_limit`. Apply the discount logic and return the final amount.
"""
* a. Call with all parameters
* b. Call using default parameter
* c. Call using arbitrary arguments (`*args`)
* d. Call using keyword arguments (`**kwargs`)
"""
#39. Create a higher-order function `promo(amount, offer_percent, offer_cap_limit, lam)` where `lam` is a lambda function performing the discount.
#40. Recreate the function from step 38 entirely as a lambda expression.

#########################################
## 🎯 Exception Handling
#########################################
#41. Apply exception handling to the calculator (step 35):
"""
    * If either of the first two arguments are non-integer, raise an exception and re-call the function after converting them to integers.
"""
#42. In the `promo` function (step 38), raise an exception if the second argument (`offer_percent`) is negative.

#########################################
## 🎯 Object-Oriented Programming (OOP)
#########################################
#43. Create a package named `inceptez.usecases`.
#44. Inside the package, create a module called `oops`.
#45. Create two classes: `Mask` and `Endecode`.
#46. In the `Mask` class, define a variable `addhash = 100` and a method `hashMask(str)` that returns the hash of `str + addhash`.
#47. In the `Endecode` class, define `prefixstr = "aix"` and a method `revEncode(str)` that returns `prefixstr + reverse(str)`.
#48. Create another module in the same package that instantiates objects `objmask` and `objendecode` for the respective classes.
#49. Create a list `["arun", "ram kumar", "yoga murthy"]`, and use `map()` to apply `hashMask()` to all elements and print the results.
#50. Apply `revEncode()` on the same list using `map()` and print the encoded values.
#51. Add a method `revDecode()` inside the `Endecode` class to decode the values encoded in step 50.


