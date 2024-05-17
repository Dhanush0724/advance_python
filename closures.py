### normal functions 
numbers = []
def add(x):
    numbers.append(x)
    print(numbers)
add(1)
add(2)
add(3)

def outer_function(x):
    numbers = []
    def inner_function(x):
        numbers.append(x)
        print(numbers)
    return inner_function()

outer_function(4)
outer_function(4)
outer_function(4)
outer_function(4)
