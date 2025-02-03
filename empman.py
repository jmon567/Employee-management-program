from decimal import Decimal
import datetime

# Base class for all employees
class Employee:
    def __init__(self, role, name, id):
        self.role = role  # Employee role (full-time or part-time)
        self.name = name  # Employee name
        self.id = id      # Employee ID number

    def get_employee_details(self):
        return f"Role: {self.role}, Name: {self.name}, ID: {self.id}"

# Derived class for full-time employees
class FullTimeEmployee(Employee):
    def __init__(self, role, name, id, salary, benefits, tax_rate):
        super().__init__(role, name, id)
        self.salary = Decimal(salary)
        self.benefits = Decimal(benefits)
        self.tax_rate = Decimal(tax_rate)

    def get_salary(self):
        return f"Salary: {self.salary:,.2f}, Benefits: {self.benefits}, Tax Rate: {self.tax_rate}"

    def calculate_weekly_pay(self):
        weekly_gross_pay = (self.salary / 52) - self.benefits
        weekly_net_pay = weekly_gross_pay * (1 - self.tax_rate / 100)
        return f"Weekly Gross Pay: {weekly_gross_pay:,.2f}, Weekly Net Pay: {weekly_net_pay:,.2f}"

    def update_details(self, salary=None, benefits=None, tax_rate=None):
        if salary:
            self.salary = Decimal(salary)
        if benefits:
            self.benefits = Decimal(benefits)
        if tax_rate:
            self.tax_rate = Decimal(tax_rate)

# Derived class for part-time employees
class PartTimeEmployee(Employee):
    def __init__(self, role, name, id, hourly_rate, hours_worked, tax_rate):
        super().__init__(role, name, id)
        self.hourly_rate = Decimal(hourly_rate)
        self.hours_worked = Decimal(hours_worked)
        self.tax_rate = Decimal(tax_rate)

    def calculate_pay(self):
        gross_pay = self.hourly_rate * self.hours_worked
        net_pay = gross_pay * (1 - self.tax_rate / 100)
        return f"Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}, Gross Pay: {gross_pay}, Net Pay: {net_pay:,.2f}"

    def update_details(self, hourly_rate=None, hours_worked=None, tax_rate=None):
        if hourly_rate:
            self.hourly_rate = Decimal(hourly_rate)
        if hours_worked:
            self.hours_worked = Decimal(hours_worked)
        if tax_rate:
            self.tax_rate = Decimal(tax_rate)

# List to store employee objects
employees = []

def log_action(action, emp):
    with open("employee_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {action} - {emp.get_employee_details()}\n")

# Function to add a new employee
def add_employee():
    role = input("Enter role (full-time/part-time): ")
    name = input("Enter name: ")
    id = input("Enter ID: ")
    
    if role.lower() == "full-time":
        salary = input("Enter salary: ").replace(",", "").lstrip("0")
        benefits = input("Enter benefits amount to be subtracted weekly: ").replace(",", "").lstrip("0")
        tax_rate = input("Enter tax rate (%): ").replace(",", "").lstrip("0")
        employee = FullTimeEmployee(role, name, id, Decimal(salary), Decimal(benefits), Decimal(tax_rate))
    elif role.lower() == "part-time":
        hourly_rate = input("Enter hourly rate: ").replace(",", "").lstrip("0")
        hours_worked = input("Enter hours worked: ").replace(",", "").lstrip("0")
        tax_rate = input("Enter tax rate (%): ").replace(",", "").lstrip("0")
        employee = PartTimeEmployee(role, name, id, Decimal(hourly_rate), Decimal(hours_worked), Decimal(tax_rate))
    else:
        print("Invalid role!")
        return
    
    employees.append(employee)
    log_action("Added", employee)
    print("Employee added successfully!")

# Function to update an existing employee's information
def update_employee():
    id = input("Enter the ID of the employee to update: ")
    for emp in employees:
        if emp.id == id:
            if isinstance(emp, FullTimeEmployee):
                salary = input("Enter new salary (leave blank to keep current): ").replace(",", "").lstrip("0")
                benefits = input("Enter new benefits amount (leave blank to keep current): ").replace(",", "").lstrip("0")
                tax_rate = input("Enter new tax rate (%) (leave blank to keep current): ").replace(",", "").lstrip("0")
                emp.update_details(salary=salary or emp.salary, benefits=benefits or emp.benefits, tax_rate=tax_rate or emp.tax_rate)
            elif isinstance(emp, PartTimeEmployee):
                hourly_rate = input("Enter new hourly rate (leave blank to keep current): ").replace(",", "").lstrip("0")
                hours_worked = input("Enter new hours worked (leave blank to keep current): ").replace(",", "").lstrip("0")
                tax_rate = input("Enter new tax rate (%) (leave blank to keep current): ").replace(",", "").lstrip("0")
                emp.update_details(hourly_rate=hourly_rate or emp.hourly_rate, hours_worked=hours_worked or emp.hours_worked, tax_rate=tax_rate or emp.tax_rate)
            
            log_action("Updated", emp)
            print("Employee information updated successfully!")
            return
    print("Employee not found!")

# Function to display current employees
def display_employees():
    if not employees:
        print("No current employees.")
    else:
        for emp in employees:
            print("-----------------------------")
            print(emp.get_employee_details())
            if isinstance(emp, FullTimeEmployee):
                print(emp.get_salary())
                print(emp.calculate_weekly_pay())
            elif isinstance(emp, PartTimeEmployee):
                print(emp.calculate_pay())

# Main menu function
def main_menu():
    while True:
        choice = input("Enter 'add' to add an employee, 'update' to update employee information, 'display' to display current employee information, or 'exit' to quit: ")
        if choice.lower() == 'add':
            print("-----------------------------")
            add_employee()
        elif choice.lower() == 'update':
            print("-----------------------------")
            update_employee()
        elif choice.lower() == 'display':
            print("-----------------------------")
            display_employees()
        elif choice.lower() == 'exit':
            print("-----------------------------")
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the menu
main_menu()
