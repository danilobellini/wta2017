a = b = c = 0

def outer():
    a = b = c = 1
    def inner():
        global a
        nonlocal b
        a = b = c = 2
    inner()
    print(a, b, c)

outer()

print(a, b, c)
