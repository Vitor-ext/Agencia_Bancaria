class Cliente:
    def __init__(self, nome, fone):
        self._nome = nome
        self._telefone = fone

# Metodo Get
    def get_nome(self):
        return self._nome

# Metodo Set
    def get_nome(self, nome):
        self._nome = nome