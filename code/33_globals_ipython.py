In [1]: import builtins

In [2]: builtins.a = builtins.b = 0

In [3]: def func():
   ...:     globals()["a"] = 2

In [4]: func()

In [5]: "b" in globals()
Out[5]: False

In [6]: print(a, b)
2 0
