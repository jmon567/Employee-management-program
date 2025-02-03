from decimal import Decimal  # Import Decimal from the decimal module

# Base class for all employees
class Employee:
    # Initialization method for employee attributes
    def __init__(self, role, name, id):
        self.role = role  # Employee role (full-time or part-time)
        self.name = name  # Employee name
        self.id = id      # Employee ID number

    # Method to get employee details
    def get_employee_details(self):
        return f"Role: {self.role}, Name: {self.name}, ID: {self.id}"


# Derived class for full-time employees
class FullTimeEmployee(Employee):
    # Initialization method for full-time employee attributes
    def __init__(self, role, name, id, salary, benefits, tax_rate):
        super().__init__(role, name, id)  # Initialize base class attributes
        self.salary = Decimal(salary)  # Full-time employee salary as Decimal
        self.benefits = Decimal(benefits)  # Full-time employee benefits amount as Decimal
        self.tax_rate = Decimal(tax_rate)  # Full-time employee tax rate as Decimal

    # Method to get salary details
    def get_salary(self):
        return f"Salary: {self.salary:,.2f}, Benefits: {self.benefits}, Tax Rate: {self.tax_rate}"

    # Method to calculate weekly pay for full-time employee after deductions
    def calculate_weekly_pay(self):
        weekly_gross_pay = (self.salary / 52) - self.benefits  # Assuming salary is annual
        weekly_net_pay = weekly_gross_pay * (1 - self.tax_rate / 100)  # Calculate net pay after tax
        return f"Weekly Gross Pay: {weekly_gross_pay:,.2f}, Weekly Net Pay: {weekly_net_pay:,.2f}"

    # Method to update employee details
    def update_details(self, salary=None, benefits=None, tax_rate=None):
        if salary:
            self.salary = Decimal(salary)
        if benefits:
            self.benefits = Decimal(benefits)
        if tax_rate:
            self.tax_rate = Decimal(tax_rate)


# Derived class for part-time employees
class PartTimeEmployee(Employee):
    # Initialization method for part-time employee attributes
    def __init__(self, role, name, id, hourly_rate, hours_worked, tax_rate):
        super().__init__(role, name, id)  # Initialize base class attributes
        self.hourly_rate = Decimal(hourly_rate)  # Part-time employee hourly rate as Decimal
        self.hours_worked = Decimal(hours_worked)  # Part-time employee hours worked as Decimal
        self.tax_rate = Decimal(tax_rate)  # Part-time employee tax rate as Decimal

    # Method to calculate total pay for part-time employee after deductions
    def calculate_pay(self):
        gross_pay = self.hourly_rate * self.hours_worked
        net_pay = gross_pay * (1 - self.tax_rate / 100)  # Calculate net pay after tax
        return f"Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}, Gross Pay: {gross_pay}, Net Pay: {net_pay:,.2f}"

    # Method to update employee details
    def update_details(self, hourly_rate=None, hours_worked=None, tax_rate=None):
        if hourly_rate:
            self.hourly_rate = Decimal(hourly_rate)
        if hours_worked:
            self.hours_worked = Decimal(hours_worked)
        if tax_rate:
            self.tax_rate = Decimal(tax_rate)


# List to store employee objects
employees = []

# Function to add a new employee
def add_employee():
    # Prompt user for employee role
    role = input("Enter role (full-time/part-time): ")
    # Prompt user for employee name
    name = input("Enter name: ")
    # Prompt user for employee ID
    id = input("Enter ID: ")
    
    # Check if the role is full-time
    if role.lower() == "full-time":
        # Prompt user for salary
        salary = input("Enter salary: ").replace(",", "")
        # Prompt user for benefits amount
        benefits = input("Enter benefits amount to be subtracted weekly: ").replace(",", "")
        # Prompt user for tax rate
        tax_rate = input("Enter tax rate (%): ").replace(",", "")
        # Create FullTimeEmployee object and add to the employees list
        employee = FullTimeEmployee(role, name, id, Decimal(salary), Decimal(benefits), Decimal(tax_rate))
    # Check if the role is part-time
    elif role.lower() == "part-time":
        # Prompt user for hourly rate
        hourly_rate = input("Enter hourly rate: ").replace(",", "")
        # Prompt user for hours worked
        hours_worked = input("Enter hours worked: ").replace(",", "")
        # Prompt user for tax rate
        tax_rate = input("Enter tax rate (%): ").replace(",", "")
        # Create PartTimeEmployee object and add to the employees list
        employee = PartTimeEmployee(role, name, id, Decimal(hourly_rate), Decimal(hours_worked), Decimal(tax_rate))
    else:
        # Invalid role entered
        print("Invalid role!")
        return
    
    # Add employee to the employees list
    employees.append(employee)
    # Confirm employee has been added successfully
    print("Employee added successfully!")


# Function to update an existing employee's information
def update_employee():
    id = input("Enter the ID of the employee to update: ")
    for emp in employees:
        if emp.id == id:
            if isinstance(emp, FullTimeEmployee):
                salary = input("Enter new salary (leave blank to keep current): ").replace(",", "")
                benefits = input("Enter new benefits amount (leave blank to keep current): ").replace(",", "")
                tax_rate = input("Enter new tax rate (%) (leave blank to keep current): ").replace(",", "")
                emp.update_details(salary=salary or emp.salary, benefits=benefits or emp.benefits, tax_rate=tax_rate or emp.tax_rate)
            elif isinstance(emp, PartTimeEmployee):
                hourly_rate = input("Enter new hourly rate (leave blank to keep current): ").replace(",", "")
                hours_worked = input("Enter new hours worked (leave blank to keep current): ").replace(",", "")
                tax_rate = input("Enter new tax rate (%) (leave blank to keep current): ").replace(",", "")
                emp.update_details(hourly_rate=hourly_rate or emp.hourly_rate, hours_worked=hours_worked or emp.hours_worked, tax_rate=tax_rate or emp.tax_rate)
            print("Employee information updated successfully!")
            return
    print("Employee not found!")


# Function to display current employees
def display_employees():
    # Check if there are no employees
    if not employees:
        print("No current employees.")
    else:
        # Iterate through the list of employees
        for emp in employees:
            # Print employee details
            print("-----------------------------")
            print(emp.get_employee_details())
            # Check if employee is a full-time employee
            if isinstance(emp, FullTimeEmployee):
                # Print full-time employee salary details
                print(emp.get_salary())
                # Print full-time employee weekly pay details
                print(emp.calculate_weekly_pay())
            # Check if employee is a part-time employee
            elif isinstance(emp, PartTimeEmployee):
                # Print part-time employee pay details
                print(emp.calculate_pay())


# Main menu function
def main_menu():
    # Infinite loop for the menu
    while True:
        # Prompt user for action
        choice = input("Enter 'add' to add an employee, 'update' to update employee information, 'display' to display current employee information, or 'exit' to quit: ")
        # Check if user wants to add an employee
        if choice.lower() == 'add':
            print("-----------------------------")
            add_employee()
        # Check if user wants to update an employee
        elif choice.lower() == 'update':
            print("-----------------------------")
            update_employee()
        # Check if user wants to display employee information
        elif choice.lower() == 'display':
            print("-----------------------------")
            display_employees()
        # Check if user wants to exit the program
        elif choice.lower() == 'exit':
            print("-----------------------------")
            print("Exiting program. Goodbye!")
            break
        else:
            # Invalid choice entered
            print("Invalid choice!")

# Start the menu
main_menu()
