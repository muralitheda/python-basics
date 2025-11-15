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



#########################################
## 🎯 Conditional Structures
#########################################
#11. Write a program to find the greatest of three numbers.
#12. Write a single program to check if a number is even or negative and print the result as:
"""
* “Even but not negative”
* “Not even but negative”
* “Neither even nor negative”
"""
#13. Write a nested `if-else` structure to print course fees:
"""
* Big Data → 25000
* Spark → 15000
* Data Science →

  * Machine Learning → 25000
  * Deep Learning → 45000
  * Both → 50000
"""
#14. Check whether a given string is a palindrome using a reverse function.
#15. Check whether `x = 100` is an integer or a string using functions like `isinstance()` or `type()`.

#########################################
## 🎯 Control Statements
#########################################
#16. Using a `for` loop, print even and odd numbers in the range `[5–20]`.
#17. Write a `while` loop to print multiples of 3 up to 21 and store the results in a list.
#18. Write a loop to calculate the cube of 4 using repeated multiplication (4 * 4 * 4 = 64).
#19. Given `sal_lst = [10000,20000,30000,10000,15000]`, add a bonus of 1000 to each salary, store it in `sal_bonus_lst`, and create another list for salaries above 11000.
#20. Write a `do-while` equivalent loop to print “Inceptez Technologies” `n` times, ensuring it prints at least once.
#21. Given `lst1 = [[10,20],[30,40,50],[60,70,80]]`, calculate the total sum, minimum, and maximum values using nested loops.
#22. Create a looping construct to print the multiplication table for 3 up to 10.

##################################################
## 🎯 Collections: List, Dictionary, Tuple, and Set
##################################################
#23. Create a list of numbers from 2 to 11. Demonstrate mutability by updating the 3rd element and resizability by inserting 100 at the 5th position.
#24. Create a tuple `("Inceptez", "Technologies", "Pvt", "Ltd")`, prove immutability and non-resizability, and access the 2nd and 4th elements to form another tuple.
#25. Convert `[("Inceptez","Technologies"),("Apple","Incorporation")]` into `[{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]`, and demonstrate the difference between `dict[key]` and `dict.get(key)`.
#26. Create a list of tuples with duplicates and remove the duplicates.
#27. Append a new tuple `("Intel", "Corp")` to the de-duplicated list.
#28. Convert `lst_dict = [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]` to `["Inceptez","Apple"]` using keys and list functions.
#29. Given `lst = [10,20,40,30,20]`, perform:
"""
    * Retrieve first and last values
    * Sort ascending & descending
    * Print min, max, and sum
    * Remove 30 and 20
"""
#30. Perform the same operations from step 29 on a tuple `(10,20,40,30,20)`.
#31. Convert the string `"Inceptez Technologies Pvt Ltd"` to a list `['Inceptez', 'Technologies', 'Pvt', 'Ltd']`.
#32. Given
"""
    ```python
    emplstlst = [["1", ("Arun","Kumar"), "10000"], ["2", ("Bala","Mohan"), "12000"]]
    ```

    Perform:
    a. Convert the first sublist to a tuple.
    b. Reverse the first and last name of the second element.
    c. Convert the entire list into tuples of tuples.
    d. Calculate the total salary.
"""

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


