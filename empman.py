from decimal import Decimal, InvalidOperation  # Import Decimal and InvalidOperation classes from the decimal module
import datetime  # Import the datetime module

# Base class for all employees
class Employee:
    def __init__(self, role, name, id):
        self.role = role  # Employee role (full-time or part-time)
        self.name = name  # Employee name
        self.id = id      # Employee ID number

    def get_employee_details(self):
        return f"Role: {self.role}, Name: {self.name}, ID: {self.id}"  # Return a formatted string with employee details

# Derived class for full-time employees
class FullTimeEmployee(Employee):
    def __init__(self, role, name, id, salary, benefits, tax_rate):
        super().__init__(role, name, id)  # Call the constructor of the base class Employee
        self.salary = Decimal(salary)  # Set salary as a Decimal object
        self.benefits = Decimal(benefits)  # Set benefits as a Decimal object
        self.tax_rate = Decimal(tax_rate)  # Set tax rate as a Decimal object

    def get_salary(self):
        return f"Salary: {self.salary:,.2f}, Benefits: {self.benefits}, Tax Rate: {self.tax_rate}"  # Return a formatted string with salary, benefits, and tax rate

    def calculate_weekly_pay(self):
        weekly_gross_pay = (self.salary / 52) - self.benefits  # Calculate weekly gross pay
        weekly_net_pay = weekly_gross_pay * (1 - self.tax_rate / 100)  # Calculate weekly net pay after tax
        return f"Weekly Gross Pay: {weekly_gross_pay:,.2f}, Weekly Net Pay: {weekly_net_pay:,.2f}"  # Return a formatted string with weekly gross and net pay

    def update_details(self, salary=None, benefits=None, tax_rate=None):
        if salary:
            self.salary = Decimal(salary)  # Update salary if a new value is provided
        if benefits:
            self.benefits = Decimal(benefits)  # Update benefits if a new value is provided
        if tax_rate:
            self.tax_rate = Decimal(tax_rate)  # Update tax rate if a new value is provided

# Derived class for part-time employees
class PartTimeEmployee(Employee):
    def __init__(self, role, name, id, hourly_rate, hours_worked, tax_rate):
        super().__init__(role, name, id)  # Call the constructor of the base class Employee
        self.hourly_rate = Decimal(hourly_rate)  # Set hourly rate as a Decimal object
        self.hours_worked = Decimal(hours_worked)  # Set hours worked as a Decimal object
        self.tax_rate = Decimal(tax_rate)  # Set tax rate as a Decimal object

    def calculate_pay(self):
        gross_pay = self.hourly_rate * self.hours_worked  # Calculate gross pay
        net_pay = gross_pay * (1 - self.tax_rate / 100)  # Calculate net pay after tax
        return f"Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}, Gross Pay: {gross_pay}, Net Pay: {net_pay:,.2f}"  # Return a formatted string with hourly rate, hours worked, gross pay, and net pay

    def update_details(self, hourly_rate=None, hours_worked=None, tax_rate=None):
        if hourly_rate:
            self.hourly_rate = Decimal(hourly_rate)  # Update hourly rate if a new value is provided
        if hours_worked:
            self.hours_worked = Decimal(hours_worked)  # Update hours worked if a new value is provided
        if tax_rate:
            self.tax_rate = Decimal(tax_rate)  # Update tax rate if a new value is provided

# List to store employee objects
employees = []

def log_action(action, emp):
    with open("employee_log.txt", "a") as log_file:  # Open log file in append mode
        log_file.write(f"{datetime.datetime.now()} - {action} - {emp.get_employee_details()}\n")  # Write action and employee details with timestamp to the log file

# Function to validate numeric inputs and handle errors
def get_decimal_input(prompt):
    while True:
        value = input(prompt).replace(",", "").lstrip("0")  # Prompt user for input and clean the input string
        try:
            return Decimal(value)  # Convert cleaned input to a Decimal object
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")  # Handle invalid input and prompt the user again

# Function to add a new employee
def add_employee():
    role = input("Enter role (full-time/part-time): ")  # Prompt user for employee role
    name = input("Enter name: ")  # Prompt user for employee name
    id = input("Enter ID: ")  # Prompt user for employee ID
    
    if role.lower() == "full-time":
        salary = get_decimal_input("Enter salary: ")  # Prompt user for salary and validate input
        benefits = get_decimal_input("Enter benefits amount to be subtracted weekly: ")  # Prompt user for benefits amount and validate input
        tax_rate = get_decimal_input("Enter tax rate (%): ")  # Prompt user for tax rate and validate input
        employee = FullTimeEmployee(role, name, id, salary, benefits, tax_rate)  # Create a FullTimeEmployee object
    elif role.lower() == "part-time":
        hourly_rate = get_decimal_input("Enter hourly rate: ")  # Prompt user for hourly rate and validate input
        hours_worked = get_decimal_input("Enter hours worked: ")  # Prompt user for hours worked and validate input
        tax_rate = get_decimal_input("Enter tax rate (%): ")  # Prompt user for tax rate and validate input
        employee = PartTimeEmployee(role, name, id, hourly_rate, hours_worked, tax_rate)  # Create a PartTimeEmployee object
    else:
        print("Invalid role!")  # Handle invalid role input
        return
    
    employees.append(employee)  # Add the new employee to the employees list
    log_action("Added", employee)  # Log the action of adding a new employee
    print("Employee added successfully!")  # Inform the user that the employee was added successfully

# Function to update an existing employee's information
# Function to update an existing employee's information
def update_employee():
    id = input("Enter the ID of the employee to update: ")  # Prompt user for the ID of the employee to update
    for emp in employees:
        if emp.id == id:
            if isinstance(emp, FullTimeEmployee):
                salary = input("Enter new salary (leave blank to keep current): ")
                if salary:
                    emp.salary = Decimal(salary)  # Update salary if a new value is provided
                benefits = input("Enter new benefits amount (leave blank to keep current): ")
                if benefits:
                    emp.benefits = Decimal(benefits)  # Update benefits if a new value is provided
                tax_rate = input("Enter new tax rate (%) (leave blank to keep current): ")
                if tax_rate:
                    emp.tax_rate = Decimal(tax_rate)  # Update tax rate if a new value is provided
            elif isinstance(emp, PartTimeEmployee):
                hourly_rate = input("Enter new hourly rate (leave blank to keep current): ")
                if hourly_rate:
                    emp.hourly_rate = Decimal(hourly_rate)  # Update hourly rate if a new value is provided
                hours_worked = input("Enter new hours worked (leave blank to keep current): ")
                if hours_worked:
                    emp.hours_worked = Decimal(hours_worked)  # Update hours worked if a new value is provided
                tax_rate = input("Enter new tax rate (%) (leave blank to keep current): ")
                if tax_rate:
                    emp.tax_rate = Decimal(tax_rate)  # Update tax rate if a new value is provided
            
            log_action("Updated", emp)  # Log the action of updating employee information
            print("Employee information updated successfully!")  # Inform the user that the employee information was updated successfully
            return
    print("Employee not found!")  # Inform the user if the employee was not found


# Function to display current employees
def display_employees():
    if not employees:
        print("No current employees.")  # Inform the user if there are no current employees
    else:
        for emp in employees:
            print("-----------------------------")  # Print a separator line
            print(emp.get_employee_details())  # Print employee details
            if isinstance(emp, FullTimeEmployee):
                print(emp.get_salary())  # Print salary details for full-time employees
                print(emp.calculate_weekly_pay())  # Print weekly pay details for full-time employees
            elif isinstance(emp, PartTimeEmployee):
                print(emp.calculate_pay())  # Print pay details for part-time employees

# Main menu function
def main_menu():
    while True:
        choice = input("Enter 'add' to add an employee, 'update' to update employee information, 'display' to display current employee information, or 'exit' to quit: ")  # Prompt user for menu choice
        if choice.lower() == 'add':
            print("-----------------------------")  # Print a separator line
            add_employee()  # Call the add_employee function
        elif choice.lower() == 'update':
            print("-----------------------------")  # Print a separator line
            update_employee()  # Call the update_employee function
        elif choice.lower() == 'display':
            print("-----------------------------")  # Print a separator line
            display_employees()  # Call the display_employees function
        elif choice.lower() == 'exit':
            print("-----------------------------")  # Print a separator line
            print("Exiting program. Goodbye!")  # Inform the user that the program is exiting
            break  # Exit the while loop and end the program
        else:
            print("Invalid choice!")  # Handle invalid menu choice input

# Start the menu
main_menu()  # Call the main_menu function to start the program
