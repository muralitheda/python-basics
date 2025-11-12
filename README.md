# 🐍 Python Overview

## 📜 Python History

- **Who?**  
  Invented in the **Netherlands** by **Guido van Rossum**.

- **When?**  
  Python was conceived in the **late 1980s**, and its implementation was started in **December 1989**.

- **How Named?**  
  Guido van Rossum is a fan of *“Monty Python’s Flying Circus”*, a famous TV show in the Netherlands — hence the name **Python**.

- **Open Source?**  
  From the very beginning, Python has been **open source**.


## 💡 Why Python?

| Feature                                                 | Reason / Explanation                                                                                           |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Built-in types and library utilities**                | Provides ready-to-use data types (list, dict, tuple, etc.) and a rich standard library for faster development. |
| **Dynamic typing**                                      | You don’t need to declare variable types; Python automatically detects the data type at runtime.               |
| **Strong typing**                                       | Prevents mixing incompatible data types (e.g., can’t add string and integer directly), ensuring safer code.    |
| **Third-party utilities (e.g., Numeric, NumPy, SciPy)** | Large ecosystem of external libraries makes complex tasks like math, data analysis, and AI easier.             |
| **Automatic memory management**                         | Python automatically allocates and frees memory using garbage collection — no manual memory handling needed.   |



## 🧠 What is Python?

Python is:  
1. **Interpreter-based**  
2. **Indentation-based**  
3. **High-level**  
4. **General-purpose / Universal**  
5. **Scripting-based**  
6. **Function-based**  
7. **Object-oriented** programming language  

![img.png](files/img.png)

### 1. Python is an Interpreter or Complier Language?

![img.png](files/img2.png)

### 2. How Python Code Gets Executed?

1. Python source code (.py) is first **compiled into bytecode** (.pyc) automatically.
2. The **Python Virtual Machine (PVM)** then **interprets and executes** this bytecode line by line.
3. Only the code is compiled/interpreted — variable values and runtime data are handled in **PVM memory** (similar to JVM’s garbage collection).
4. **.pyi files** can be used to avoid recompiling the same workload repeatedly.
5. **PySpark Case:**
   * Spark uses **JVM**, Python uses **PVM**.
   * When using PySpark, the **PVM runs inside the JVM** to execute Python code and interact with the Spark engine.
   * Note: **JVM cannot run inside PVM.**
![img.png](files/img3.png)

### 3. Python is Indent Based language. Why?

* Python uses **indentation (spaces or tabs)** to define code blocks instead of braces `{}` or keywords like `BEGIN...END`.
* This enforces **clean formatting**, **readability**, and **structured coding** — making programs easier to read, understand, and maintain.
* Other languages like **SQL**, **Scala**, **Java**, **PL/SQL**, and **Linux Shell scripting** follow a **block-based programming model**, not indentation-based.
* In Python, indentation is part of the **syntax** — missing or incorrect indentation causes errors.
* Standard practice: use **4 spaces** (recommended by PEP 8) or **a single TAB** for indentation.
