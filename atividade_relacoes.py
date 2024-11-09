class Loja:
    def __init__(self, loc, funcionarios=None, estoque=None, loja_proxima=None):
        self.loc = loc
        self.funcionarios = funcionarios if funcionarios else []
        self.estoque = estoque if estoque else []
        self.loja_proxima = loja_proxima  # Loja mais próxima

    def change_func(self, funcionario, delete=False):
        if delete:
            if funcionario in self.funcionarios:
                self.funcionarios.remove(funcionario)
        else:
            self.funcionarios.append(funcionario)

    def change_estoque(self, instrumento, delete=False):
        if delete:
            if instrumento in self.estoque:
                self.estoque.remove(instrumento)
        else:
            self.estoque.append(instrumento)

    def consult_estoque(self):
        contagem = {"Guitarra": 0, "Baixo": 0, "Violao": 0}
        for instrumento in self.estoque:
            if isinstance(instrumento, Guitarra):
                contagem["Guitarra"] += 1
            elif isinstance(instrumento, Baixo):
                contagem["Baixo"] += 1
            elif isinstance(instrumento, Violao):
                contagem["Violao"] += 1
        return contagem

    def consult_funcionarios(self):
        """Conta a quantidade de funcionários por cargo."""
        contagem = {}
        for funcionario in self.funcionarios:
            if funcionario.cargo in contagem:
                contagem[funcionario.cargo] += 1
            else:
                contagem[funcionario.cargo] = 1
        return contagem

    def definir_loja_proxima(self, loja):
        self.loja_proxima = loja


class Funcionario:
    def __init__(self, nome, cpf, salario, cargo, loja=None):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
        self.loja = loja


class Instrumento:
    def __init__(self, marca, modelo, preco, n_corda):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.n_corda = n_corda


class Guitarra(Instrumento):
    def __init__(self, marca, modelo, preco, n_corda,):
        super().__init__(marca, modelo, preco, n_corda)


class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, n_corda):
        super().__init__(marca, modelo, preco, n_corda)

class Violao(Instrumento):
    def __init__(self, marca, modelo, preco, n_corda):
        super().__init__(marca, modelo, preco, n_corda)

#Relações possíveis:
#associação entre a loja e a loja mais próxima
#agragação entre a loja e seus funcionarios
#composição entre a loja e seu estoque 
#composição entre os instrumentos e seus tipos de instrumento

#Drivercode

guitarra1 = Guitarra("EMAP", "JoãoCocudo", 1500, 6)
baixo1 = Baixo("AlexJunio", "BrunoFerreira", 1200, 4)
violao1 = Violao("Marhias", "Tokar", 300, 6)

func1 = Funcionario("Pinho", "12345678901", 2000, "Vendedor")
func2 = Funcionario("Everton", "09876543210", 2500, "Gerente")

loja1 = Loja("São Paulo")
loja2 = Loja("Rio de Janeiro")

loja1.change_func(func1)
loja1.change_func(func2)

print("Funcionários após adições:", loja1.consult_funcionarios())

loja1.change_func(func1, delete=True)
print("Funcionários após remoção do Pinho:", loja1.consult_funcionarios())

loja1.change_estoque(guitarra1)
loja1.change_estoque(baixo1)
loja1.change_estoque(violao1)

print("Estoque após adições:", loja1.consult_estoque())

loja1.definir_loja_proxima(loja2)
print("Loja mais próxima de loja1:", loja1.loja_proxima.loc)