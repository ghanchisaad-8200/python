# 👨‍💼 Employee Management System

## 📌 Project Description

This is a **Python Object-Oriented Programming (OOP)** project called **Employee Management System**.

The project demonstrates important OOP concepts such as **classes, objects, inheritance, encapsulation, method overriding, and polymorphism**.

The system allows users to create and manage different types of people and employees, including **Person, Employee, Manager, and Developer**.

---

## ✨ Features

The Employee Management System provides the following operations:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show People and Employee Details
6. Update Employee Salary
7. Remove an Employee
8. Exit the System

The available menu options are implemented directly in the Python program.

---

## 🧱 Classes Used

### 1. Person

The `Person` class stores basic information such as:

* Name
* Age

It also contains a `display()` method to show the person's information.

### 2. Employee

The `Employee` class inherits from the `Person` class.

It adds:

* Employee ID
* Salary

The employee ID and salary are stored using private attributes. The project also provides getter and setter methods for these values.

### 3. Manager

The `Manager` class inherits from `Employee`.

In addition to employee information, a Manager has:

* Department

It also overrides the `display()` method to show manager-specific information.

### 4. Developer

The `Developer` class also inherits from `Employee`.

It adds:

* Primary Programming Language

The class overrides the `display()` method to display developer-specific information.

---

## 🧠 OOP Concepts Demonstrated

### Inheritance

`Employee` inherits from `Person`, while `Manager` and `Developer` inherit from `Employee`.

```text
Person
  ↓
Employee
  ↓
Manager
Developer
```

### Encapsulation

Employee ID and salary are stored as private attributes:

```python
self.__employee_id
self.__salary
```

Getter and setter methods are used to access and update these values.

### Method Overriding

`Person`, `Employee`, `Manager`, and `Developer` have their own `display()` methods.

This allows each class to display information according to its own type.

### Polymorphism

The system stores different employee types together and calls their `display()` methods, allowing each object to provide its own implementation.

---

## ⚙️ Employee Management Operations

The `EmployeeManagementSystem` class maintains separate collections for people and employees.

It provides methods to:

* Add a person
* Add an employee
* Update an employee's salary
* Remove an employee
* Find an employee by ID

The salary update and employee removal operations search for the employee using the Employee ID.

---

## 🛡️ Input Validation

The project includes separate functions for taking integer and floating-point input.

If the user enters an invalid number, the program displays an error message and asks again.

Examples:

```python
input_int()
input_float()
```

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Open the Project Folder

Open the project folder in **VS Code** or another Python editor.

### Step 3: Run the Program

Open the terminal and run:

```bash
python employee_management_system.py
```

---

## 💻 Example Menu

```text
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Update Employee Salary
7. Remove Employee
8. Exit
```

---

## 📂 Project Structure

```text
project-4/
│
├── employee_management_system.py
└── README.md
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

* Python Classes and Objects
* Constructors
* Inheritance
* Encapsulation
* Method Overriding
* Polymorphism
* Private Attributes
* Getter and Setter Methods
* Lists
* Loops
* Conditional Statements
* Exception Handling
* User Input
* Menu-Driven Programs

---

## 👨‍💻 Author

**Saad Ghanchi**

GitHub: https://github.com/ghanchisaad-8200

---

## 📜 License

This project is created for **learning and educational purposes**.
