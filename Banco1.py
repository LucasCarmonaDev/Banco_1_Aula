class Titular(object):
    def __init__(self, cpf, nome, sobrenome):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome

    def get_cpf(self):
        return self.cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_sobrenome(self):
        return self.sobrenome

    def nome_completo(self):
        nome_c = self.nome + ' ' + self.sobrenome
        return nome_c


class Conta(object):
    def __init__(self, numero, obj_titular, saldo, limite):
        self.numero = numero
        self.titular = obj_titular
        self.saldo = saldo
        self.limite = limite

    def get_numero(self):
        return self.numero

    def get_obj_titular(self):
        return self.titular

    def get_saldo(self):
        return self.saldo

    def get_limite(self):
        return self.limite

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def set_limite(self, novo_limite):
        self.limite = novo_limite

    def extrato_reduzido(self):
        # Retorna uma string formatada com o número da conta e o valor do saldo
        extr_rd = f"Número Conta: {self.numero}\nValor Saldo: {str(self.saldo)}"
        return extr_rd

    def extrato_normal(self):
        # Retorna uma string formatada com informações detalhadas do titular e da conta
        extr_nm = f"Nome: {self.get_obj_titular().get_nome()}\nSobrenome: {self.get_obj_titular().get_sobrenome()}\nNúmero Conta: {self.numero}\nValor Saldo: {str(self.saldo)}"
        return extr_nm

    def deposito(self, valord):
        # Adiciona o valor do depósito ao saldo da conta
        self.saldo += valord

    def saque(self, saque):
        # Subtrai o valor do saque do saldo da conta
        self.saldo -= saque


if __name__ == '__main__':
    titular1 = Titular('171-1', 'Vini', 'Tiburcio')
    print('Nome:', titular1.get_nome())
    print('Nome completo:', titular1.nome_completo())
    conta1 = Conta("100", titular1, 200, 300)

    print(conta1.get_saldo())
    print(conta1.get_obj_titular())
    print(conta1.get_obj_titular().get_cpf())

    titular1.set_nome("Vinicius")
    print('Nome:', titular1.get_nome())
    conta1.get_obj_titular().set_nome("Leandro")
    print("Nome:", titular1.get_nome())
