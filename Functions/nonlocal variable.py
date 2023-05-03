# outside function
def outer():
    message = 'local'

    # nested function
    def inner():
        # declare nonlocal variable
        nonlocal message

        message = 'non local'
        print("inner :", message)

    inner()
    print("outer :", message)


outer()
