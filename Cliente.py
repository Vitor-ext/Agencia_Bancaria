class Cliente:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

# Metodo Get
    def get_nome(self):
        return self._nome

# Metodo Set
    def get_nome(self, nome):
        self._nome = nome