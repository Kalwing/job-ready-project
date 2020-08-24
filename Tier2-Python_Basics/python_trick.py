# %% Python Tricks

# %% Context manager


class Indenter:
    def __init__(self):
        self.indent_lvl = 0

    def print(self, string: str):
        print('\t'*self.indent_lvl + string)

    def __enter__(self):
        self.indent_lvl += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_lvl -= 1


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
