import ast

source = """
a = 7
a *= 6
b = a + 5
"""

tree = ast.parse(source)

# Mantém apenas as atribuições
tree.body = [node for node in tree.body if isinstance(node, ast.Assign)]

code = compile(tree, "<ast>", "exec")

ns = {}

exec(code, {}, ns)

ns


# Subtrai 1 em todos os números
class Sub1(ast.NodeTransformer):
    def visit_Num(self, node):
        return ast.copy_location(ast.Num(node.n - 1), node)

tree = Sub1().visit(tree)

code = compile(tree, "<ast>", "exec")

exec(code, {}, ns)

ns


# Obtém todos os identificadores do código (com repetição)
[node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
