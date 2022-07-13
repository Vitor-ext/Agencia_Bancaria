class Conta:
    def __init__(self, titular, numero, saldo):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular

    @property
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
