In [1]: def add(context):
   ...:     a, b = context["a"], context["b"]
   ...:     return a + b

In [2]: def call():
   ...:     a, b = 2, 5
   ...:     return add(locals())

In [3]: call()
Out[3]: 7
