class Conta:
    def __init__(self, titular, numero, saldo):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular

    @property    # Não é padrão a utilização logo após um metodo.
    def saldo(self):
        return self._saldo

    def titular(self):
        return self._titular

    def numero(self):
        return self._numero

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("Saldo não poder ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque de", valor, "realizado com sucesso !")
            print("Querido:", self._titular, "Seu Saldo Atual é:", self._saldo)
        else:
            print("Saldo insuficiente")


    def deposita (self, valor):
        self.saldo += valor
        print("Deposito de", valor,"realizado com sucesso !")
        print("Querido:", self._titular, "Seu Saldo Atual é:", self._saldo)


    def extrato (self):
        print("Cliente:", self._titular, "Saldo Atual:", self._saldo)

