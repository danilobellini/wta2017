a = 7

def f():
    exec('a = 3')
    print(locals())
    return a

f()
