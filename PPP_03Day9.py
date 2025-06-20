## Implement a class with attributes like emp_id, name, salary, department, and method to calculate overtime pay
class Emp:
    def __init__(self, employeeid, name, salary, department ):
        self.empid = employeeid
        self.name = name
        self.salary = salary
        self.dept = department

    def overtime(self, hours, rate_per_hour):
        return rate_per_hour * hours
    
a = Emp(101, 'Raj', 25000, 'IT')
b = Emp(102, 'Alice', 30000, 'HR')
c = Emp(103, 'Vikas', 35000, 'Management')

print(f"The overtime payment of {a.name}is, {a.overtime(3, 2500)}")
print(f"The overtime payment of {b.name}is, {b.overtime(4, 2000)}")
print(f"The overtime payment of {c.name}is, {c.overtime(2, 3000)}")

        
