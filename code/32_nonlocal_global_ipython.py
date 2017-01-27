In [1]: a = b = c = 0

In [2]: def outer():
   ...:     a = b = c = 1
   ...:     def inner():
   ...:         global a
   ...:         nonlocal b
   ...:         a = b = c = 2
   ...:     inner()
   ...:     print(a, b, c)

In [3]: outer()
1 2 1

In [4]: print(a, b, c)
2 0 0
