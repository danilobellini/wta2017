import ast, cmath

source = "exp(1j * pi).real"

tree = ast.parse(source, "<source>", "eval")

print(ast.dump(tree, False, False))

code = compile(tree, "<ast>", "eval")

eval(code, vars(cmath))
