def add(context):
    a, b = context["a"], context["b"]
    return a + b

def call():
    a, b = 2, 5
    return add(locals())

call()
