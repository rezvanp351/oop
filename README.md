# USAGE GUIDE

This document explains **how to create classes and use objects** in this project.
It provides short, practical examples based on the existing files:

- `father.py`
- `mother.py`
- `boy.py`
- `women.py`
- `oop.py`

---

## ✅ 1. How to create a class
A class defines:
- attributes (data)
- methods (behavior)

Example:
```python
class Father:
    def __init__(self, name="Hamed", age=45, job="Engineer"):
        self.name = name
        self.age = age
        self.job = job

    def info(self):
        return f"Father: {self.name}, Age: {self.age}, Job: {self.job}"
```

✅ `__init__` runs when the object is created
✅ `self` refers to the object itself

---

## ✅ 2. How to create an object (instance)
```python
from father import Father

dad = Father("Karim", 50, "Teacher")
```

### Access attributes:
```python
print(dad.name)
print(dad.age)
```

### Call methods:
```python
print(dad.info())
```

---

## ✅ 3. Inheritance
Use inheritance to reuse code:
```python
from father import Father

class Girl(Father):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby
```

Now `Girl` has:
- name
- age
- info()
from `Father`

---

## ✅ 4. Polymorphism (method overriding)
```python
class Boy(Father):
    def info(self):
        return f"Boy: {self.name}, Age: {self.age}"
```

Calling:
```python
b = Boy("Aref", 17)
print(b.info())
```
Outputs boy-specific text.

---

## ✅ 5. Using Boy and Woman classes
```python
from boy import Boy
from women import Woman

b = Boy("Aref", 17, "Programming")
w = Woman("Mina", 20, "Painting")

print(b.playing_football())
print(w.put_makeup())
```

---

## ✅ 6. Running the project
Run from terminal:
```
python oop.py
```

Or choose mode:
```
python oop.py boy
python oop.py girl
python oop.py woman
python oop.py father
python oop.py assign
```

---

## ✅ 7. Dynamic calling
Check if a method exists:
```python
if hasattr(b, "coding_javaScript"):
    print(b.coding_javaScript())
```

---

## ✅ 8. Adding a new class
Steps:
1. Create a new file (e.g., `teacher.py`)
2. Define a class with `__init__`
3. Add methods
4. Import and use it in `oop.py`

Example:
```python
class Teacher(Father):
    def teach(self):
        return "Teaching students"
```

---

✅ You now know how to:
- define classes
- create objects
- inherit
- override methods
- run the project

---
## 📎 Author
👩‍💻 **Created by: ❤️ by **Muhammad Aref Rezvan Panah**
📅 **Year:** 2025  
💬 **Language:** Python 3.10  
🎯 **Purpose:** Teaching Python functions in a clear and beginner-friendly way.

---

## 💖 Support & Feedback
If this repository helped you, please consider:
- ⭐ **Starring** the repo  
- 🗨️ **Commenting** your thoughts  
- 📢 **Sharing** it with others learning Python  

Your feedback motivates more free educational content!

