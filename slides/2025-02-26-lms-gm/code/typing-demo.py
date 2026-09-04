
class MyCoolClassTyped:
    def __init__(self, first_arg: str, second_arg: int) -> None:
        self.first_arg: str = first_arg
        self.second_arg: int = second_arg

    def add_my_attributes(self) -> int:
        return self.first_arg + self.second_arg

# ❯ mypy 2025-02-26-lms-gm/code/typing-demo.py
# 2025-02-26-lms-gm/code/typing-demo.py:8: error: Unsupported operand types for + ("str" and "int")  [operator]
# Found 1 error in 1 file (checked 1 source file)












class MyCoolClassUntyped:
    def __init__(self, first_arg, second_arg):
        self.first_arg = first_arg
        self.second_arg = second_arg

    def add_my_attributes(self):
        return self.first_arg + self.second_arg

mycoolclassuntyped = MyCoolClassUntyped(first_arg='1', second_arg=2)
mycoolclassuntyped.add_my_attributes()

#Traceback (most recent call last):
# ...
#     return self.first_arg + self.second_arg
# TypeError: can only concatenate str (not "int") to str