>>> obj = type("SomeClass", # Nome da classe
...            (object,),   # Bases (herança)
...            {c: i for i, c in
...             enumerate("Σ𝚺𝛴𝜮𝝨𝞢")} # Namespace
... )()
>>> obj.𝞢 == getattr(obj, "𝞢")
False
>>> obj.Σ == getattr(obj, "Σ")
True
>>> dir(obj)
[..., 'Σ', '𝚺', '𝛴', '𝜮', '𝝨', '𝞢']
