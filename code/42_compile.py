add2tox = compile("x + 2", "<string>", "eval")

eval(add2tox, {"x": 3})

from timeit import timeit

timeit('exec("k = 1e3", {})')

timeit(stmt='exec(code, {})',
       setup='code = compile("k = 1e3", "<string>", "exec")')
