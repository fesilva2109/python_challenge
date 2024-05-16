import os 
os.system("cls")  # Limpa a tela do console (funciona apenas no Windows)

class Carro: 
    def __init__(self, marca, modelo, ano, usuario):
        #Inicializa um objeto Carro com os atributos especificados.
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.usuario = usuario
        self.servicosMarcados = []  
        self.servicosAgendados = [] 
        self.historicoManutencao = []
        

    def __str__(self):
        #Retorna uma representação em string do objeto Carro.
        return f" Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}"

    def apresentarCarro():
        #Apresenta todos os carros criados até o momento.
        for carro in Carro.carros:
            print(f"Marca: {carro.marca} | Modelo: {carro.modelo} | Ano: {carro.ano} | Usuário: {carro.usuario.nomeUser}")


    def listarServicosAgendados(self):
        #Lista todos os serviços agendados pelo usuário.
        print("Serviços Agendados:")
        for servico in self.servicosAgendados:
            servico.status = "Agendado"
            print(servico)

    def limparServicosAgendados(self):
        #Limpa a lista de serviços agendados do usuário.
        self.servicosAgendados.clear
        self.servicosAgendados = {}

    def listarServicosMarcados(self):
        #Lista todos os serviços marcados pelo usuário.
        print("Serviços Marcados:")
        for servico, _ in self.servicosMarcados:
            print(servico)

    def limparServicosMarcados(self):
        #Limpa a lista de serviços marcados pelo usuário.
        self.servicosMarcados.clear
        self.servicosMarcados = {}

    def agendarServico(self,usuario):
        self.listarServicosMarcados()
        for servico, _ in self.servicosMarcados:
                print(servico)
                self.servicosAgendados.append(servico)
                
        self.limparServicosMarcados()       

class User:
    def __init__(self, nomeUser, email, telefoneContato):
        #Inicializa um objeto User com os atributos especificados.
        self.nomeUser = nomeUser
        self.email = email
        self.telefoneContato = telefoneContato
        self.carros = []  # Lista para armazenar os carros do usuário
        self.servicosMarcados = []  # Lista para armazenar os serviços marcados pelo usuário
        self.servicosAgendados = []  # Lista para armazenar os serviços agendados pelo usuário

    def __str__(self):
        #Retorna uma representação em string do objeto User.
        return f"{self.nomeUser} | {self.email} | {self.telefoneContato}"
    
    def adicionarCarro(self, marca, modelo, ano):
        #Adiciona um novo carro à lista de carros do usuário.
        novoCarro = Carro(marca, modelo, ano, self)
        self.carros.append(novoCarro)

    def listarCarros(self):
        #Lista todos os carros associados ao usuário.
        for i, carro in enumerate(self.carros):
            print(f"{i+1}. {carro}")
        

    def listarServicosAgendados(self):
        #Lista todos os serviços agendados pelo usuário.
        print("Serviços Agendados:")
        for servico in self.servicosAgendados:
            servico.status = "Agendado"
            print(servico)

    def limparServicosAgendados(self):
        #Limpa a lista de serviços agendados do usuário.
        self.servicosAgendados.clear
        self.servicosAgendados = {}

    def listarServicosMarcados(self):
        #Lista todos os serviços marcados pelo usuário.
        print("Serviços Marcados:")
        for servico, _  in self.servicosMarcados:
            print(servico)

    def limparServicosMarcados(self):
        #Limpa a lista de serviços marcados pelo usuário.
        self.servicosMarcados.clear
        self.servicosMarcados = {}
   

class Servico:
    def __init__(self, nomeServico, preco, idServico):
        #Inicializa um objeto Servico com os atributos especificados.
        self.nomeServico = nomeServico
        self.preco = preco 
        self.idServico = idServico
        self.status = "Disponível"

    def __str__(self):
        #Retorna uma representação em string do objeto Servico.
        return f"Serviço: {self.nomeServico} | R${self.preco} |ID: {self.idServico} | Status:{self.status}"


class SistemaDeEncomendas:
    servicosDisponiveis = []  # Lista para armazenar os serviços disponíveis
    servicosAgendados = []  # Lista para armazenar os serviços agendados

    def adicionarServicoDisponivel(self, nomeServico, preco, idServico):
        #Adiciona um novo serviço à lista de serviços disponíveis.
        novoServico = Servico(nomeServico, preco, idServico)
        SistemaDeEncomendas.servicosDisponiveis.append(novoServico)
        
    def pegarIDServico():
        #Retorna o ID do último serviço marcado pelo usuário.
        idServico = usuario.servicosMarcados[-1][0].idServico
        return idServico

    def marcarServico(self, idServico, usuario,carro):
        #Marca um serviço para o usuário.
        servico_marcado = None
        for servico in SistemaDeEncomendas.servicosDisponiveis:
            if servico.idServico == idServico:
                servico_marcado = servico
                servico.status = "Marcado"
                break
        if servico_marcado:
            carro.servicosMarcados.append((servico_marcado, usuario))
            print("Serviço marcado com sucesso")
            return True
        else:
            print("Serviço não encontrado")
            return False
 

## Funções
def cadastrarCarro(usuario):
    #Permite que o usuário cadastre um novo carro.
    marca = input("Digite a Marca: ")
    modelo = input("Digite o Modelo: ")
    ano = int(input("Digite o Ano: "))
    usuario.adicionarCarro(marca, modelo, ano)
    
    
def loginUser():
    #Cadastra um novo usuário e retorna o objeto User correspondente.
    while True: 
        novoUser = User(str(input("Digite seu nome completo: ")), str(input("Digite seu e-mail: ")), str(input("Digite seu telefone para contato: ")))
        return novoUser

def manutencaoPreventiva(usuario,carro):
    #Permite que o usuário agende serviços de manutenção preventiva.
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
                sistema.marcarServico(1, usuario,carro)
                print("Marcando troca de farol")
                break
            case "2":
                sistema.marcarServico(2, usuario,carro)
                print("Marcando troca de óleo")
                break
            case "3":
                sistema.marcarServico(3, usuario,carro)
                print("Marcando revisão de freios")
                break
            case "4":
                sistema.marcarServico(4, usuario,carro)
                print("Marcando alinhamento e balanceamento")
                break
            case "5":
                sistema.marcarServico(5, usuario,carro)
                print("Marcando troca de bateria")
                break
            case "6":
                print("Saindo")
                break
            case _:
                print("Opção inválida")
        idServico = int(opcaoPreventiva)
        sistema.marcarServico(idServico, usuario,carro)

def pagarServico(carro):
    #Permite que o usuário pague pelos serviços marcados.
    if carro.servicosMarcados == []:
        print("Não há serviços marcados.")
    else:
        carro.listarServicosMarcados()

        if len(carro.servicosMarcados) == 1:
            resposta = input("Deseja pagar pelo serviço listado? (s/n): ")
        else: 
            resposta = input("Deseja pagar pelos serviços listados? (s/n): ")

        if resposta.lower() == "s":
            carro.agendarServico(usuario)
            print("Pagamento efetuado com sucesso!")
        else:
            print("Pagamento cancelado.")

# Função para listar usuários
def listarUsuarios():
    #Lista todos os usuários cadastrados.
    print("Lista de Usuários:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. {usuario}")

# Função para obter o usuário selecionado
def obterUsuario():
    #Permite que o usuário selecione um usuário da lista.
    listarUsuarios()
    while True:
        usuario_index = int(input("Selecione o número do usuário: ")) -1
        if 0 <= usuario_index < len(usuarios):
            return usuarios[usuario_index]
        else:
            print("Por favor, selecione um número de usuário válido.")

def obterCarro():
    #Permite que o usuário selecione um usuário da lista.
    usuario.listarCarros()
    while True:
        carro_index = int(input("Selecione o número do carro: ")) -1
        if 0 <= carro_index < len(usuario.carros):
           
            return usuario.carros[carro_index]
        else:
            print("Por favor, selecione um número de carro válido.")

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
        os.system("cls")
        novoUser = loginUser()
        usuarios.append(novoUser)
        print("Usuário cadastrado com sucesso!")
    elif opcao == "2":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            os.system("cls")
            usuario = obterUsuario()
            os.system("cls")
            novoCarro = cadastrarCarro(usuario)
    elif opcao == "3":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            os.system("cls")
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                os.system("cls")
                
                carro = obterCarro()
                print(carro)
                
                manutencaoPreventiva(usuario,carro)
    elif opcao == "4":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            os.system("cls")
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                os.system("cls")
                carro = obterCarro()
                os.system("cls")
                pagarServico(carro)
    elif opcao == "5":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            os.system("cls")
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                carro = obterCarro()
                if not carro.servicosMarcados :
                    print ("Nenhum serviço marcado")
                else:
                    os.system("cls")
                    carro.listarServicosMarcados()
                    print("Seu serviço está marcado, prossiga para o pagamento do serviço para confirma-lo")
    elif opcao == "6":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            os.system("cls")
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                os.system("cls")
                obterCarro()
                if not carro.servicosAgendados :
                    print ("Nenhum serviço Agendado")
                else:
                    os.system("cls")
                    carro.listarServicosAgendados()
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
