# Python Programming


# 🎯 Variables:

## 1. Create two variables `x = 100` and `y = 10`, find their multiplication and division, and store the results in variables `z` and `z1`.
```python
x = 100
y = 10
z = x * y
z1 = x / y
print("type(z):",type(z), "z:",z)
print("type(z1):", type(z1), "z1:", z1)
```

```
type(z): <class 'int'> z: 1000
type(z1): <class 'float'> z1: 10.0
```


## 2. Create a variable `a = 2000`, divide `a` by `y` (from step 1), and reassign `a` with the divided result.

```python

print()

a = 2000
a = a / y
print("type(a):",type(a),"a:",a)

"""
type(a): <class 'float'> a: 200.0
"""
```

## 3. Prove Python is dynamically typed by creating `x: int = 100`, then assigning `y = str(x)` and printing the types of `x` and `y`.
```python
print()

x: int = 100
y = str(x)
print("type(x):",type(x))
print("type(y):",type(y))

"""
type(x): <class 'int'>
type(y): <class 'str'>
"""
```


## 4. Demonstrate Python’s dynamic inference feature with an example showing automatic datatype detection.
```python

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

```

## 5. Prove Python is a strongly typed language using incompatible type operations.
```python

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
```

## 6. Create variables `a, b, c, d` assigned with values `10, 20, 30, 40` respectively.
```python
print()

a = 10
b = 20
c = 30
d = 40
print(f"a={a} b={b} c={c} d={d}")

# OR

a,b,c,d = 10,20,30,40
print(f"a={a} b={b} c={c} d={d}")
```

## 7. Prove that Python variable names are case-sensitive.
```python
print()

name = "Alan Harpor"
Name = "alan harpor"
print(f"name={name} | Name={Name}")

"""
name=Alan Harpor Name=alan harpor
"""
```

## 8. Demonstrate that variable names cannot start with numbers or contain special characters (except `_`).
```python
print()

_number = 100  # valid
number_ = 100  # valid
"""
1number = 100  # not valid
$number = 100  # not valid
num$ber = 100  # not valid
"""
```

## 9. Show examples of using single, double, and triple quotes in Python.
```python
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
```

## 10. Demonstrate examples using arithmetic, assignment, comparison, relational, and logical operators.
```python
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
```

# 🎯 Conditional Structures:

# 🎯 Control Statements:

# 🎯 Collections: List, Dictionary, Tuple and Set

# 🎯 Functions:

# 🎯 Exception Handling:

# 🎯 OOPS (Object Oriented Programming):
