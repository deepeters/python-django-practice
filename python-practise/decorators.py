#functional programming pradigm where functions can both be input or output of other functions

def announce(f):
    def wrapper():
        print ("About to run the function...")
        f()
        print("Done with the function.")


@announce
def hello():
    print("Hello, World!")

hello()