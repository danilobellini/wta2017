In [1]: add2tox = compile("x + 2", "<string>", "eval")

In [2]: eval(add2tox, {"x": 3})
Out[2]: 5

In [3]: from timeit import timeit

In [4]: timeit('exec("k = 1e3", {})')
Out[4]: 10.071980122000241

In [5]: timeit(stmt='exec(code, {})',
   ...:        setup='code = compile("k = 1e3", "<string>", "exec")')
Out[5]: 0.3254070729999512
