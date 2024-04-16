import os 

class Carro: 
    carros = []
    def __init__(self, marca, modelo, ano, usuario):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.usuario = usuario
        Carro.carros.append(self)

    def __str__(self):
        return f"{self.marca} | {self.modelo} | {self.ano}"

    def apresentarCarro():
        for carro in Carro.carros:
            print(f"Marca: {carro.marca} | Modelo: {carro.modelo} | Ano: {carro.ano} | Usuário: {carro.usuario.nomeUser}")

class User:
    def __init__(self, nomeUser, email, telefoneContato):
        self.nomeUser = nomeUser
        self.email = email
        self.telefoneContato = telefoneContato
        self.carros = []

    def __str__(self):
        return f"{self.nomeUser} | {self.email} | {self.telefoneContato}"

    def adicionarCarro(self, marca, modelo, ano):
        novoCarro = Carro(marca, modelo, ano, self)
        self.carros.append(novoCarro)

    def listarCarros(self):
        for carro in self.carros:
            print(carro)

class Servico:
    def __init__(self, nomeServico, preco, idServico):
        self.nomeServico = nomeServico
        self.preco = preco 
        self.idServico = idServico
        self.status = "Disponível"

    def __str__(self):
        return f"{self.nomeServico} | {self.preco} | {self.idServico} | {self.status}"


class SistemaDeEncomendas:
    
    servicosDisponiveis = []
    servicosEncomendados = []

    def adicionarServicoDisponivel(self, nomeServico, preco, idServico):
        novoServico = Servico(nomeServico, preco, idServico)
        SistemaDeEncomendas.servicosDisponiveis.append(novoServico)
        print("Serviço adicionado com sucesso")

    def encomendarServico(self, idServico, usuario):
        servico_encomendado = None
        for servico in SistemaDeEncomendas.servicosDisponiveis:
            if servico.idServico == idServico:
                servico.status = "Encomendado"
                servico_encomendado = servico
                break
        if servico_encomendado:
            SistemaDeEncomendas.servicosEncomendados.append((servico_encomendado, usuario))
            print("Serviço encomendado com sucesso")
            return True
        else:
            print("Serviço não encontrado")
            return False

    def listarServicosEncomendados(self, usuario):
        print("Serviços Encomendados:")
        for servico, user in SistemaDeEncomendas.servicosEncomendados:
            if user == usuario:
                print(servico)
  

## Funções
def cadastrarCarro(usuario):
    marca = input("Digite a Marca: ")
    modelo = input("Digite o Modelo: ")
    ano = int(input("Digite o Ano: "))
    usuario.adicionarCarro(marca, modelo, ano)

def loginUser():
    novoUser = User(input("Digite seu nome completo: "), input("Digite seu e-mail: "), input("Digite seu telefone para contato: "))
    return novoUser

def manutencaoPreventiva(usuario):
    sistema = SistemaDeEncomendas()
    sistema.adicionarServicoDisponivel("Troca de Farol", 200, 1)
    sistema.adicionarServicoDisponivel("Troca de Óleo", 100, 2)
    sistema.adicionarServicoDisponivel("Revisão de Freios", 150, 3)
    sistema.adicionarServicoDisponivel("Alinhamento e Balanceamento", 80, 4)
    sistema.adicionarServicoDisponivel("Troca de Bateria", 150, 5)
    
    while True:
        print("Escolha o tipo de serviço que será executado: \n")
        print("1. Troca de Farol")
        print("2. Troca de Óleo")
        print("3. Revisão de Freios")
        print("4. Alinhamento e Balanceamento")
        print("5. Troca de Bateria")
        print("6. Sair")

        opcaoPreventiva = input("Selecione a opção: ")

        match opcaoPreventiva:
            case "1":
                sistema.encomendarServico(1, usuario)
                print("Marcando troca de farol")
                break
            case "2":
                sistema.encomendarServico(2, usuario)
                print("Marcando troca de óleo")
                break
            case "3":
                sistema.encomendarServico(3, usuario)
                print("Marcando revisão de freios")
                break
            case "4":
                sistema.encomendarServico(4, usuario)
                print("Marcando alinhamento e balanceamento")
                break
            case "5":
                sistema.encomendarServico(5, usuario)
                print("Marcando troca de bateria")
                break
            case "6":
                print("Saindo")
                break
            case _:
                print("Opção inválida")
        idServico = int(opcaoPreventiva)
        sistema.encomendarServico(idServico, usuario)
def verServicosEncomendados(usuario):
    sistema = SistemaDeEncomendas()
    sistema.listarServicosEncomendados(usuario)

def pagarServico(usuario):
    sistema = SistemaDeEncomendas()
    sistema.listarServicosEncomendados(usuario)
    resposta = input("Deseja pagar pelos serviços listados? (s/n): ")

    if resposta.lower() == "s":
        sistema.servicosEncomendados = []
        print("Pagamento efetuado com sucesso!")
    else:
        print("Pagamento cancelado.")

# Função para listar usuários
def listarUsuarios():
    print("Lista de Usuários:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. {usuario}")

# Função para obter o usuário selecionado
def obterUsuario():
    listarUsuarios()
    while True:
        usuario_index = int(input("Selecione o número do usuário: ")) -1
        if 0 <= usuario_index < len(usuarios):
            return usuarios[usuario_index]
        else:
            print("Por favor, selecione um número de usuário válido.")

## Menu Principal
usuarios = []

while True: 
    print("\n==== Menu ====")
    print("1. Cadastro de Usuário")
    print("2. Cadastrar Carro")
    print("3. Manutenção Preventiva")
    print("4. Pagamento de Serviços")
    print("5. Serviços Agendados")
    print("6. Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        novoUser = loginUser()
        usuarios.append(novoUser)
        print("Usuário cadastrado com sucesso!")
    elif opcao == "2":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            usuario = obterUsuario()
            cadastrarCarro(usuario)
    elif opcao == "3":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            usuario = obterUsuario()
            manutencaoPreventiva(usuario)
    elif opcao == "4":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            usuario = obterUsuario()
            pagarServico(usuario)
    elif opcao == "5":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            usuario = obterUsuario()
               
            print(SistemaDeEncomendas.servicosEncomendados)  
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
