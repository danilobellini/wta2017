In [1]: a = 7

In [2]: def f():
   ...:     exec('a = 3')
   ...:     print(locals())
   ...:     return a

In [3]: f()
{'a': 3}
Out[3]: 7
