class PipeFactory:
    """
    Class representing factory of pipes
    """

    def __init__(self, type):
        parts = type.split('.')
        module = ".".join(parts[:-1])
        self.m = __import__(module)
        for comp in parts[1:]:
            self.m = getattr(self.m, comp)            


    def get_pipe(self, sides, x, y):
        return self.m(sides, x, y)