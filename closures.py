## Closures without parameters

def outer():
    print('I am outer function. ')

    def inner():
        print('I am inner function. ')

    # return but not executing the function
    return inner


var = outer()
## print(var) --> Output: <function outer.<locals>.wrapper at 0x000001B95D26B280>
## variable become the function wrapper
var()