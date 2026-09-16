from __future__ import annotations


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self) -> None:
        print(f"Person created with name: {self.name} and age: {self.age}.")


class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str = None, salary: float = 0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self) -> str:
        return self.__employee_id

    def set_employee_id(self, employee_id: str) -> None:
        self.__employee_id = employee_id

    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, salary: float) -> None:
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = salary

    def display(self) -> None:
        print(
            f"Employee created with name: {self.name}, age: {self.age}, "
            f"ID: {self.__employee_id}, and salary: ${self.__salary}."
        )

    def __str__(self):
        return f"[Employee] {self.name} (ID: {self.get_employee_id()})"


class Manager(Employee):
    def __init__(self, name: str, age: int, employee_id: str, salary: float, department: str):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self) -> None:
        print(
            f"Manager created with name: {self.name}, age: {self.age}, "
            f"ID: {self.get_employee_id()}, salary: ${self.get_salary()}, "
            f"and department: {self.department}."
        )

    def __str__(self):
        return f"[Manager] {self.name} (ID: {self.get_employee_id()}, Dept: {self.department})"


class Developer(Employee):
    def __init__(self, name: str, age: int, employee_id: str, salary: float, programming_language: str):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self) -> None:
        print(
            f"Developer created with name: {self.name}, age: {self.age}, "
            f"ID: {self.get_employee_id()}, salary: ${self.get_salary()}, "
            f"and primary language: {self.programming_language}."
        )

    def __str__(self):
        return f"[Developer] {self.name} (ID: {self.get_employee_id()}, Lang: {self.programming_language})"


def describe_relationship(cls) -> None:
    print(f"  -> issubclass({cls.__name__}, Employee) = {issubclass(cls, Employee)}")
    print(f"  -> issubclass({cls.__name__}, Person)   = {issubclass(cls, Person)}")


class EmployeeManagementSystem:
    def __init__(self):
        self.people: list[Person] = []
        self.employees: list[Employee] = []

    def add_person(self, person: Person) -> None:
        self.people.append(person)

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def update_employee_salary(self, employee_id: str, new_salary: float) -> bool:
        for emp in self.employees:
            if emp.get_employee_id() == employee_id:
                emp.set_salary(new_salary)
                return True
        return False

    def remove_employee(self, employee_id: str) -> bool:
        for emp in self.employees:
            if emp.get_employee_id() == employee_id:
                self.employees.remove(emp)
                return True
        return False

    def find_employee(self, employee_id: str) -> Employee | None:
        for emp in self.employees:
            if emp.get_employee_id() == employee_id:
                return emp
        return None


def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    system = EmployeeManagementSystem()

    menu = """
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
"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()
        print()

        if choice == "1":
            name = input("Enter Name: ")
            age = input_int("Enter Age: ")
            person = Person(name, age)
            person.display()
            system.add_person(person)

        elif choice == "2":
            name = input("Enter Name: ")
            age = input_int("Enter Age: ")
            emp_id = input("Enter Employee ID: ")
            salary = input_float("Enter Salary: ")
            employee = Employee(name, age, emp_id, salary)
            employee.display()
            system.add_employee(employee)

        elif choice == "3":
            name = input("Enter Name: ")
            age = input_int("Enter Age: ")
            emp_id = input("Enter Employee ID: ")
            salary = input_float("Enter Salary: ")
            department = input("Enter Department: ")
            manager = Manager(name, age, emp_id, salary, department)
            manager.display()
            system.add_employee(manager)

        elif choice == "4":
            name = input("Enter Name: ")
            age = input_int("Enter Age: ")
            emp_id = input("Enter Employee ID: ")
            salary = input_float("Enter Salary: ")
            language = input("Enter Primary Programming Language: ")
            developer = Developer(name, age, emp_id, salary, language)
            developer.display()
            system.add_employee(developer)

        elif choice == "5":
            print("Choose details to show:")
            print("1. All People")
            print("2. All Employees / Managers / Developers")
            sub = input("Enter your choice: ").strip()
            print()
            if sub == "1":
                if not system.people:
                    print("No people created yet.")
                for p in system.people:
                    p.display()
            elif sub == "2":
                if not system.employees:
                    print("No employees created yet.")
                for e in system.employees:
                    e.display()
            else:
                print("Invalid choice.")

        elif choice == "6":
            emp_id = input("Enter Employee ID to update: ")
            new_salary = input_float("Enter new salary: ")
            if system.update_employee_salary(emp_id, new_salary):
                print(f"Salary updated successfully for Employee ID: {emp_id}.")
            else:
                print(f"No employee found with ID: {emp_id}.")

        elif choice == "7":
            emp_id = input("Enter Employee ID to remove: ")
            if system.remove_employee(emp_id):
                print(f"Employee with ID: {emp_id} has been removed.")
            else:
                print(f"No employee found with ID: {emp_id}.")

        elif choice == "8":
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-8).")


if __name__ == "__main__":
    print("Class relationship check:")
    describe_relationship(Manager)
    describe_relationship(Developer)
    print()

    main()
