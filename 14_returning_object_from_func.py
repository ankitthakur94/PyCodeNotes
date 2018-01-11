


def print_something():
    str = "Hello world"
    print (str)
    print ( " ID in function {} ".format(id(str)))
    return str;

def get_random_list():
    new_list = [1,2,3,4,5]
    print ( " ID in function {} ".format(id(new_list)))
    return new_list

str2 = print_something()
print ( " ID outside function {} ".format(id(str2)))


list2 = get_random_list()
print ( " ID outside function {} ".format(id(list2)))






# There is no concept of variable in python.
# There are objects, which are stored in memory.
    # Memory for them is created when they are created.
# And there are names (which look like variables). Names are references to objects.

# Ex :
x = 100
y = 100
    # Here 100 is the object
    # x, y are names which refer to the same object 100. So id(x) and id(y) will be the same.
y = 200
    # Now a new object 200 is created
    # y now refers to 200.
    # ref count of 100 is decreased by 1 and ref count of 200 is +1


# If Id() of 2  names is the same, then they both point / refer to the same object.

## Every object in python has 3 things :
# <type , value , ref_count>

## Ways to decrease reference count :
# del (<name>)
    # This does not delete the object, but removes that name as a reference to that object.

# name going out of scope

# Assigning name to other object
    # Ref count of original object decreases by 1 and ref count of new object increases by 1.



## Objects in global namespace :
    # Their ref count may never decrease (or go down to 0)
    # So avoid many variables in global namespace.




## Garbage Collection
    # A kind of memory recycler.

# Types of garbage collection :
    # 1.) Reference counting.
    # 2.) Tracing

# 1.) Ref counting Garbage collection.
    # When ref count = 0 for an object. We can free the memory for that object.

    # Good :
        # Easy to implement.
        # when ref count = 0, object is immediately deleted.

    # Bad :
        # Memory overhead to store reference count for every object.
        # Runtime overhead, every time the ref_count has to be increased or decreased (un-necessary operation)
        # Not thread safe ( Big issue )
        # Doesn't detect cyclical reference

            # Cyclical reference :
                # 2 objects refer to each other.
                #  on calling del on both of the names of the objects, reference count decreases by 1, but not goes to 0.
                    # coz they had 2 references (one their name, and one the other object)
                # So ideally ref_count for both should had gone to 0, but it is 1.
                # Common in graphs / doubly linked list.

    # So ref-count based alone can't ensure complete garbage collection as it misses out on cyclical reference.


# 2.) Tracing

    # Algo :
        # Uses Mark and Sweep algorithm
        # This is triggered when number of objects in memory > threshold.
        # Start from a root object, traverse on connected objects like a tree and mark all.
        # The ones which could not be marked are deleted from memory
        # Takes care of cyclic references.

# Python uses :
    # Reference Counting + Generational ( A type of Tracing algo)
    # When reference count reaches 0, we get immediate clean-up (THis is via reference counting)
    # But in case of Cyclic reference, Generation GC will run after specific intervals only then those references will be cleaned.
        # So we will not get immediate clean-up.
        # THis can slow-down the problem, so avoid such data structs.



# Some Gotchas

# 1.) __del__  Magic method implemented in a class.
    # __del__ is a magic method, which if implemented is called when the reference count for the object of that class type is 0.
    # i.e it is called when reference count = 0 and the object is to be deleted.
    # It is not called if the python method del () is called on an object. del () just decereases the ref count by 1.


# 2.) __slots__ (Used to improve memory usage for a class)
class Point () :
    __slots__ = ('x', 'y')

p1 = Point()            # create a new Point
p1.x = 10               # assign x
p1.y = 20               # assign y

#p1.name                # ERROR !!

# we will only be able to define only those attributes (class data members) for a class, which have been specified in __slots__
# This disallows user from creating <class_instance>.name method.












