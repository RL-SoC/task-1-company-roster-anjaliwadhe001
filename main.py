"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes = [int(code) for code in branchcodes.split(",")]
            salary = int(input("Salary: "))
            # Create a new Engineer with given details.
            engineer = Engineer(name,ID, city, branchcodes,salary)
            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson

            name=input("Name:")
            ID=input("ID:")
            city=input("City:")
            region=input("Region:")
            sales=float(input("Sales:"))

            salesperson = Salesperson(name, ID, city, region, sales)

            # Then add them to the roster
            engineer_roster.append(salesperson)
            pass

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: 
                print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = [branch.name for branch in found_employee.branches]
                ## ???? what comes here??
                print(f"Branches: {', '.join(branch_names)}" )
                
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID=int(input("ID:"))
            new_branch_name = input("New Branch: ")

            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee: 
                print("No such employee")
            else:
                found_employee.add_branch(new_branch_name)
                print("Branch updated successfully")
            pass
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            # promote employee to next position
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee: 
                print("No such employee")
            else:
                found_employee.promote()
                print("Employee promoted successfully")

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            found_employee = None
            # Increment salary of employee.
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee: 
                print("No such employee")
            else:
                increment_amount = float(input("Enter increment amount: "))
                found_employee.increment_salary(increment_amount)
                print("Salary incremented successfully")
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            # Print superior of the sales employee.
            found_employee = None
            for employee in sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee: 
                print("No such employee")
            else:
                superior = found_employee.get_superior()
                if superior:
                    print(f"Superior: {superior.name} with ID {superior.ID}")
                else:
                    print("No superior found")
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales employee
            employee = None
            superior = None
            for emp in sales_roster:
                if emp.ID == ID_E:
                    employee = emp
                elif emp.ID == ID_S:
                    superior = emp
                    
            if not employee or not superior: 
                print("No such employee or superior")
            else:
                employee.set_superior(superior)
                print("Superior added successfully")

        else:
            raise ValueError("No such query number defined")

        


        






