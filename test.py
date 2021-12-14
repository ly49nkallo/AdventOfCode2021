def wrapper(function):
    return function

@wrapper
def function():
    print('hello there!')

if __name__ == "__main__":
    function()