def initalfunction():
    print("I'm developed initally Fresh")


def decorators(func):

    def inner():
        print("I'm changed without even notice")
        
    return inner

function_changing = decorators(initalfunction)

function_changing()

#######################################################
def routes(a,b):

    print(a+b)

def authenticate(func):
    
    def login(*args):
        log = False
        if log :
            return func(*args)
        else :
            return 'failes.please login'
        
    return login

deco = authenticate(routes)
deco('mysore','sarja')
print(deco)

