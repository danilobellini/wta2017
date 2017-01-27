In [1]: import ast, cmath

In [2]: source = "exp(1j * pi).real"

In [3]: tree = ast.parse(source, "<source>", "eval")

In [4]: print(ast.dump(tree, False, False))
Expression(Attribute(Call(Name('exp', Load()), [BinOp(Num(1j), Mult(), Name('pi', Load()))], []), 'real', Load()))

In [5]: code = compile(tree, "<ast>", "eval")

In [6]: eval(code, vars(cmath))
Out[6]: -1.0
