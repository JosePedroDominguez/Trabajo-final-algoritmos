class fuera_de_op(Exception):
    def __init__(self,op):
        self.op = op
    def __str__(self):
        return str (self.op)




