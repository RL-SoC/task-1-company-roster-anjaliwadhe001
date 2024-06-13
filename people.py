"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : str
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        if self.city==new_city: 
            return False
        else:
     # Return true if city change, successful, return false if city same as old city
            self.city = new_city
            return True
        pass

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        if len(self.branches) !=1:
            return False
        self.branches[0]=new_code
        return True
        pass

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary += increment_amt
        pass

class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        valid_positions=["Junior","Senior","Team Lead", "Director"]
        # Only then set the position. 
        if position is valid_positions:
            self.position=position
        else:
            raise ValueError("Invalid position. Must be one of: Junior, Senior, Team Lead, Director") 
        # Only then set the position. 

    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        bonus=amt*0.10
        super().increament(amt+bonus)
        pass
        
    def promote(self, position:str) -> bool:
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.

        valid_positions = ["Junior", "Senior", "Team Lead", "Director"]
        current_index = valid_positions.index(self.position)
        new_index = valid_positions.index(position)

        if new_index<= current_index:
            return False  # Return false for a demotion or an invalid promotion
        
        amt=self.salary*0.30
        self.increment(amt)
        self.position = position
        pass


class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self, employee_id: int, name: str, salary: int, position: str, superior: int = None):  # Complete all this! Add arguments
        super().__init__(employee_id, name, salary, position)
        self.superior = superior
        pass

    # def increment 
    def increment(self, amt: int) -> None:
        bonus = amt * 0.05
        super().increment(amt + bonus)

    # def promote 
    def promote(self, position: str) -> bool:
        valid_positions = ["Rep", "Manager", "Head"]
        current_index = valid_positions.index(self.position)
        new_index = valid_positions.index(position)

        if new_index <= current_index:
            return False  # demotion or same position, return False
        
        amt = self.salary * 0.05
        self.increment(amt)
        self.position = position
        return True

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior:
            return self.superior.ID, self.superior.name
        else:
            return None, None
        pass

    def add_superior(self) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
         if superior:
            self.superior = superior
            return True
         else:
            return False
         pass


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        self.branch_codes.append(new_code)
        return True
        pass

    





    
    