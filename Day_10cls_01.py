## Defining class, using list, doc string creating manager object
class EmployeeManager:
    def __init__(self):
        self.employees = []  

    def add_employee(self, emp_id, name, salary):
        """Adds a new employee."""
        self.employees.append({"id": emp_id, "name": name, "salary": salary})
        print(f"Employee {name} added.")

    def get_employee(self, emp_id):
        """Fetch employee details by ID."""
        for employee in self.employees:
            if employee["id"] == emp_id:
                return employee
        return f"No employee found with ID {emp_id}"

    def get_high_salary_employees(self, min_salary):
        """Filter employees with a salary above the threshold."""
        return [emp for emp in self.employees if emp["salary"] > min_salary]


manager = EmployeeManager()
manager.add_employee(101, "Alice", 70000)
manager.add_employee(102, "Raj", 65000)
manager.add_employee(103, "Durga", 49000)

print(manager.get_employee(102)) 
high_salary = manager.get_high_salary_employees(45000)
print(high_salary) 

