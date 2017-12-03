###################################################################
## Objective :
# Explore Inheritance in python
##      Calling constructor of base class in constructor of derived class.
#   isinstance
#   issubclass
###################################################################


###################################################################
## Theory ##
# Inheritance by default copies everything the base class has, into derived class (class variables erc.)
###################################################################

class Employee:

    # Class variable
    raise_percent = 5

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name (self):
        return '{} {}'.format (self.name)

    # Apply raise to specific employee instance
    def apply_raise(self):
        self.salary = self.salary * (1 + self.raise_percent)

# A derived class
class Developer (Employee):

    # For a developer we can have a different raise amount
    # Override raise amount
    raise_percent =  10

class Manager (Employee):

    # Again override the deffault raise amount of Employee class which was 4%
    raise_percent = 2

emp1 = Employee ('Employee 1', 200)
dev1 = Developer ('Ankit Thakur', 100)
mngr1 = Manager ('Manager 1', 500)

emp1.apply_raise()
dev1.apply_raise()
mngr1.apply_raise()

print ( 'Salary for Employee 1 :', emp1.salary)
print ( 'Salary for Developer 1 :', dev1.salary)
print ( 'Salary for Manager 1 :', mngr1.salary)

## OUTPUT :
# Salary for Employee 1 : 1200
# Salary for Developer 1 : 1100
# Salary for Manager 1 : 1500
############## So we can see that we get all functions of base class (Employee) directly for free to Derived class (Developer and Manager)
# And overriding raise_percent in derived classes does not effect that variable in base class.


###################################################################
#### Method Resolution Order ####
###################################################################
# The order in which python searches for variables / functions in a class hierarchy
# Starts from the last derived class and goes upwards till it finds in base class.
# For the above example, if we create a new Developer, it will search for __init__ in Developer class
# Since not present, then will search in Employee class and there it finds.
# In python all classes are derived from a generic base class : 'builtin.object'

# This methods resolution order can be seen by command : print (help (<class_name>) )
# This shows everything inherited from base class also.
###################################################################




###################################################################
## Passing extra info while creating derived class
##      Calling constructor of base class in constructor of derived class.
###################################################################

# Say we want to pass another argument (programming language) while creating a developer
# So we will have to write the constructor separately for Developer



class Developer (Employee):

    raise_percent =  10

    def __init__ (self, name, salary, prog_language):

        # name , salary are the same arguments as were required in Employee constructor also.
        # so instead of writing self.name = name here, we will not duplicate the code
        # Instead we will re-use the code of base class constructor.

        # 2 ways of doing this >
        # super().__init__(name, salary)              # Way 1.    # Lets keep this one.
        # Employee.__init__(self, name, salary)       # Way 2.

        # Base class constructor handling name and salary
        super().__init__(name, salary)

        # Now take care of the extra argument
        self.prog_language = prog_language


    def display_details (self):
        print ( ' Name : {} , Salary : {} , Prog Language : {}'.format(self.name, self.salary, self.prog_language) )



dev1 = Developer ('Developer 1', 100, 'C++')
dev1.display_details()

dev2 = Developer ('Developer 2', 200, 'All')
dev2.display_details()




class Manager (Employee):

    raise_percent = 2

    # Take list of employees this is managing as another argument
    def __init__(self, name, salary, employees_list = None) :       # Concept of 'Do no pass mutable defaults to a method'

        # Base class constructor handling name and salary
        super().__init__(name, salary)

        # Derived class constructor handling the rest
        if employees_list is None :
            self.employees = []
        else:
            self.employees = employees_list

    def add_emp (self, emp):
        if emp not in self.employees :
            self.employees.append(emp)

    def remove_emp (self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees (self):
        print ( ' List of Employees under :', self.name )
        [print(i.name) for i in self.employees]


mgr1 = Manager ('Manager 1', 1000)
mgr1.add_emp(dev1)
mgr1.add_emp(dev2)

mgr1.print_employees()




###################################################################
# Some helpful methods for class inheritance
###################################################################


# 1.) isinstance (<instance_name>, <Class_name> )
#   TO check if a variable is an instance of a class or not

print ( isinstance(mgr1, Manager))          # True
print ( isinstance(mgr1, Developer))        # False
print ( isinstance(mgr1, Employee))         # True
# Since manager is derived from employee, it is an instance of employee also.


# 2.) issubclass (<class_name_1> , <class_name_2>)
# Is class_name_1 derived from class_name_2  ?
print ( issubclass(Manager, Employee))        # True
print ( issubclass(Manager, Developer))         # False









###################################################################
## CONCLUSION ##
###################################################################
# 1.) A derived class copies all code of the base class by default
# 2.) We can over ride the variables / methods we want in derived class
# 3.) Method resolution order can be used to see how python searches for functions in class hierarchy
#       This can be given by print ( help (<class_name>) )

# 4.) Do not pass default mutable arguments in methods
# 5.) Leverage the base class constructor to initialize the variables common to base and derived class
#       super().__init__(<>)
#       or
#       Employee.__init__ (self, <>)
###################################################################
















