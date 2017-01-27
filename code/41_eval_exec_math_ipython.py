In [1]: import math

In [2]: eval("sin(pi / 2)", vars(math))
Out[2]: 1.0

In [3]: ns = {}

In [4]: exec("result = log2(4096)", vars(math), ns)

In [5]: ns
Out[5]: {'result': 12.0}
