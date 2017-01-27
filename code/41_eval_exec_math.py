import math

eval("sin(pi / 2)", vars(math))

ns = {}

exec("result = log2(4096)", vars(math), ns)

ns
