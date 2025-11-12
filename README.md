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

- Built-in types and library utilities  
- Dynamic typing  
- Strong typing  
- Third-party utilities (e.g., **Numeric**, **NumPy**, **SciPy**)  
- Automatic memory management  


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

**How Python Code Gets Executed?**

1. Python source code (.py) is first **compiled into bytecode** (.pyc) automatically.
2. The **Python Virtual Machine (PVM)** then **interprets and executes** this bytecode line by line.
3. Only the code is compiled/interpreted — variable values and runtime data are handled in **PVM memory** (similar to JVM’s garbage collection).
4. **.pyi files** can be used to avoid recompiling the same workload repeatedly.

**PySpark Case:**

* Spark uses **JVM**, Python uses **PVM**.
* When using PySpark, the **PVM runs inside the JVM** to execute Python code and interact with the Spark engine.
* Note: **JVM cannot run inside PVM.**
