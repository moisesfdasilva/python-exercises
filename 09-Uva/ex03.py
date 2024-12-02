
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    def aumentar_salario(self, porcentagem):
        self._salario *= (porcentagem / 100 + 1)

    def exibir_informacao(self):
        return f"Nome: {self.nome} e salário: R$ {self._salario}."


joao = Funcionario("Joao", 2000)
joao.aumentar_salario(10)
print(joao.exibir_informacao())
