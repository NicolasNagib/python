from modelos.banco import Banco

class conta_poupanca(Banco):
    def __init__(self, titular, saldo, tipo_conta):
        super().__init__(titular, saldo, tipo_conta)
        self._taxa_juros = 0.05

    def render(self):
        self._saldo += self._saldo* self._taxa_juros