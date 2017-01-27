In [1]: import ast

In [2]: source = """
   ...: a = 7
   ...: a *= 6
   ...: b = a + 5
   ...: """

In [3]: tree = ast.parse(source)

In [4]: # Mantém apenas as atribuições
   ...: tree.body = [node for node in tree.body if isinstance(node, ast.Assign)]

In [5]: code = compile(tree, "<ast>", "exec")

In [6]: ns = {}

In [7]: exec(code, {}, ns)

In [8]: ns
Out[8]: {'a': 7, 'b': 12}

In [9]: # Subtrai 1 em todos os números
   ...: class Sub1(ast.NodeTransformer):
   ...:     def visit_Num(self, node):
   ...:         return ast.copy_location(ast.Num(node.n - 1), node)

In [10]: tree = Sub1().visit(tree)

In [11]: code = compile(tree, "<ast>", "exec")

In [12]: exec(code, {}, ns)

In [13]: ns
Out[13]: {'a': 6, 'b': 10}

In [14]: # Obtém todos os identificadores do código (com repetição)
    ...: [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
Out[14]: ['a', 'b', 'a']
