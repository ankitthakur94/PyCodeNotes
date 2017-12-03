########################################################
## Objective : ##
########################################################
# Explore magic / dunder methods
#       __str__             < str()
#       __repr__            < repr ()
#       __add__             < +
#       __len__             < len ()

########################################################


########################################################
# Theory :
########################################################
# Magic methods are special methods which are called by standard python methods.
# Syntax : __<name>__
# Ex : __init__
########################################################




########################################################
# 1.) __repr__ : representation
#       Should show a representation of the python class instance.
#       Should return a string which when copied exactly will re-create the same class instance on which __repr__ is called.
#       More for the developer's purpose.
#       If __str__ is not implemented in a python class calling print() on any of the class instance will print the string returned by __repr__
#       Can be externally called via print (repr(<class_instance_name>))

# 2.) __str__ : string
#       Should return a string which helps the end user get some information about the class instance.
#       when print(<instance_variable> ) is called, internally __str__ function will be executed
#       Can be externally called via print ( str (<class_instance_name> ))


class Employee:

    raise_percent = 5

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name (self):
        return '{} {}'.format (self.name)

    # Apply raise to specific employee instance
    def apply_raise(self):
        self.salary = self.salary * (1 + self.raise_percent)


    def __repr__ (self):
        repr_string = "Employee ( '{}' , {} )".format (self.name, self.salary )
        return repr_string

    def __str__(self):
        str_string = "Employee '{}' , Salary :  {}".format (self.name, self.salary )
        return str_string


emp1 = Employee('Employee 1', 100)

print (str(emp1))           # More like a help manual of class instance for end user.
# Same as : emp1.__str__ ()
print (repr(emp1))          # String which can be used to re-create emp1
# Same as : emp1.__repr__ ()


## OUTPUT :
# Employee 'Employee 1' , Salary :  100
# Employee ( 'Employee 1' , 100 )





#### To implement '+' operator to add 2 / more instances of a class implement the method __add__
# Similarly for __sub__  etc.









