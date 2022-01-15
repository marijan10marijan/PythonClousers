## Closures with parameters

def outer(num):
    
    def wrapper():
        print(num)

    return wrapper

var = outer(33)
var2 = outer(56)
var()
var2()
