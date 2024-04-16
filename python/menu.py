import os 
os.system("cls")

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
        self.servicosMarcados = []
        self.servicosAgendados = []

    def __str__(self):
        return f"{self.nomeUser} | {self.email} | {self.telefoneContato}"
    
    def adicionarCarro(self, marca, modelo, ano):
        novoCarro = Carro(marca, modelo, ano, self)
        self.carros.append(novoCarro)

    def listarCarros(self):
        for carro in self.carros:
            print(carro)

    def listarServicosAgendados(self):
        print("Serviços Agendados:")
        for servico, _ in self.servicosAgendados:
            print(servico)

    def limparServicosAgendados(self):
        self.servicosAgendados.clear
        self.servicosAgendados = {}


    def listarServicosMarcados(self):
        print("Serviços Marcados:")
        for servico, _ in self.servicosMarcados:
            print(servico)

    def limparServicosMarcados(self):
        self.servicosMarcados.clear
        self.servicosMarcados = {}
   

class Servico:
    def __init__(self, nomeServico, preco, idServico):
        self.nomeServico = nomeServico
        self.preco = preco 
        self.idServico = idServico
        self.status = "Disponível"

    def __str__(self):
        return f"Serviço: {self.nomeServico} | R${self.preco} |ID: {self.idServico} | Status:{self.status}"


class SistemaDeEncomendas:
    
    servicosDisponiveis = []
    servicosAgendados = []

    def adicionarServicoDisponivel(self, nomeServico, preco, idServico):
        novoServico = Servico(nomeServico, preco, idServico)
        SistemaDeEncomendas.servicosDisponiveis.append(novoServico)
        
    def pegarIDServico():
       idServico = usuario.servicosMarcados[-1][0].idServico
       return idServico

    def marcarServico(self,idServico, usuario):
        servico_marcado = None
        for servico in SistemaDeEncomendas.servicosDisponiveis:
            if servico.idServico == idServico:
                servico_marcado = servico
                servico.status = "Marcado"
                break
        if servico_marcado:
            usuario.servicosMarcados.append((servico_marcado, usuario))
            print("Serviço marcado com sucesso")
            return True
        else:
            print("Serviço não encontrado")
            return False

  

## Funções
def cadastrarCarro(usuario):
    marca = input("Digite a Marca: ")
    modelo = input("Digite o Modelo: ")
    ano = int(input("Digite o Ano: "))
    usuario.adicionarCarro(marca, modelo, ano)

def loginUser():
    while True: 
        novoUser = User(str(input("Digite seu nome completo: ")), str(input("Digite seu e-mail: ")), str(input("Digite seu telefone para contato: ")))
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
                sistema.marcarServico(1, usuario)
                print("Marcando troca de farol")
                break
            case "2":
                sistema.marcarServico(2, usuario)
                print("Marcando troca de óleo")
                break
            case "3":
                sistema.marcarServico(3, usuario)
                print("Marcando revisão de freios")
                break
            case "4":
                sistema.marcarServico(4, usuario)
                print("Marcando alinhamento e balanceamento")
                break
            case "5":
                sistema.marcarServico(5, usuario)
                print("Marcando troca de bateria")
                break
            case "6":
                print("Saindo")
                break
            case _:
                print("Opção inválida")
        idServico = int(opcaoPreventiva)
        sistema.marcarServico(idServico, usuario)

def pagarServico(usuario):
    
    if usuario.servicosMarcados == []:
        print("Não há serviços marcados.")
    else:
        User.listarServicosMarcados(usuario)
        resposta = input("Deseja pagar pelos serviços listados? (s/n): ")
        if resposta.lower() == "s":
            for servico in usuario.servicosMarcados:
                usuario.servicosAgendados.append(servico)
            User.limparServicosMarcados(usuario)
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
    print("5. Serviços Marcados")
    print("6. Serviços Agendados")
    print("7. Sair")

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
            if not usuario.servicosMarcados :
                print ("Nenhum serviço marcado")
            else:
                User.listarServicosMarcados(usuario)
                print("Seu serviço está marcado, prossiga para o pagamento do serviço para confirma-lo")
    elif opcao == "6":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            usuario = obterUsuario()
            if not usuario.servicosMarcados :
                print ("Nenhum serviço Agendado")
            else:
                User.listarServicosAgendados(usuario)
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
