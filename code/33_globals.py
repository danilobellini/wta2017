import builtins

builtins.a = builtins.b = 0

def func():
    globals()["a"] = 2

func()

"b" in globals()

print(a, b)
