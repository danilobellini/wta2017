from inspect import stack

def a(): return b()
def b(): return c()
def c(): return d()
def d(): return e()
def e(): return stack()

print([finfo.function for finfo in a()])
