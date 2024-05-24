import os 
import re
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        for servico, usuario, horario_marcado in self.servicosMarcados:
            print(f"{servico} ")

    def limparServicosMarcados(self):
        #Limpa a lista de serviços marcados pelo usuário.
        self.servicosMarcados.clear
        self.servicosMarcados = {}

    def agendarServico(self):
        # Este método agenda os serviços marcados pelo usuário.
        
        # Itera sobre cada serviço marcado na lista de serviços marcados do carro.
        for servico, _, horario_marcado in self.servicosMarcados:
            # Adiciona o serviço marcado à lista de serviços agendados do carro.
            self.servicosAgendados.append(servico)
            # Adiciona o serviço marcado ao histórico de manutenção do carro.
            self.historicoManutencao.append(servico)
    
        # Após agendar os serviços, limpa a lista de serviços marcados do carro.
        self.limparServicosMarcados()

    def adicionarReparoAoHistorico(self):
        # Este método permite ao usuário adicionar um reparo ao histórico de manutenção do carro.
        
        # Verifica se o histórico de manutenção está vazio.
        if len(self.historicoManutencao) == 0:
            print("O registro de manutenções está vazio")
            # Solicita ao usuário se deseja adicionar um reparo ao histórico.
            respostaHistorico = input("Gostaria de adicionar uma manutenção ao histórico? (s/n) ")
        else:
            # Se o histórico não estiver vazio, lista os reparos previamente registrados.
            print("Histórico de Manutenções:")
            for servico in self.historicoManutencao:
                print(servico)
            # Solicita ao usuário se deseja adicionar um reparo ao histórico.
            respostaHistorico = input("Gostaria de adicionar uma manutenção ao histórico? (s/n) ")
        
        # Se a resposta do usuário for afirmativa, solicita detalhes do reparo.
        if respostaHistorico.lower() == "s":
            servico = adicionarServico(self)
            # Adiciona o reparo ao histórico de manutenção.
            self.historicoManutencao.append(servico)
            print("Serviço adicionado")
        else: 
            print("Voltando ao menu principal")


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
        

    
class Servico:
    def __init__(self, nomeServico, preco, idServico):
        #Inicializa um objeto Servico com os atributos especificados.
        self.nomeServico = nomeServico
        self.preco = preco 
        self.idServico = idServico
        self.status = "Disponível"
        self.horario_marcado = None

    def __str__(self):
        #Retorna uma representação em string do objeto Servico.
        return f"Serviço: {self.nomeServico} | R${self.preco} |ID: {self.idServico} | Status:{self.status} | Horário: {self.horario_marcado} "

class SistemaDeEncomendas:
    servicosDisponiveis = []  # Lista para armazenar os serviços disponíveis
    servicosAgendados = []  # Lista para armazenar os serviços agendados
    horarios = ["07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]
    def adicionarServicoDisponivel(self, nomeServico, preco, idServico):
        #Adiciona um novo serviço à lista de serviços disponíveis.
        novoServico = Servico(nomeServico, preco, idServico)
        SistemaDeEncomendas.servicosDisponiveis.append(novoServico)
    
    def pegarIDServico():
        #Retorna o ID do último serviço marcado pelo usuário.
        idServico = usuario.servicosMarcados[-1][0].idServico
        return idServico
    def listarHorarios(self):
        for horario in self.horarios:
            print(horario)
    def marcarHorario(self):
        while True:
                horario_marcado = input("Digite o horário que deseja marcar (ex: 07:00): ")
                if horario_marcado in self.horarios:
                    print(f"Você marcou o horário: {horario_marcado}")
                    break
                else:
                    print("Horário inválido! Por favor, escolha um dos horários disponíveis.")
        return horario_marcado
    
    def marcarServico(self, idServico, usuario,carro, horario_marcado):
        #Marca um serviço para o usuário.
        servico_marcado = None
        for servico in SistemaDeEncomendas.servicosDisponiveis:
            if servico.idServico == idServico:
                servico_marcado = servico
                servico.status = "Marcado"
                servico.horario_marcado = horario_marcado
                break
        if servico_marcado: 
            carro.servicosMarcados.append((servico_marcado, usuario, horario_marcado))
            print("Serviço marcado com sucesso")
            return True
        else:
            print("Serviço não encontrado")
            return False
 

## Funções
def adicionarServico(carro):
    # Este método solicita detalhes sobre um serviço executado e o adiciona ao histórico de manutenções do carro.
    # Solicita o tipo de serviço executado.
    servico = input("Qual tipo de serviço foi executado? ")
    # Pergunta se o evento aconteceu mais de uma vez e valida a resposta.
    evento = input("Esse evento aconteceu mais de uma vez? (s/n) ")
    while evento.lower() not in ["s", "n"]:
        print("Opção inválida!")
        evento = input("Esse evento aconteceu mais de uma vez? (s/n) ")

    # Se o evento aconteceu mais de uma vez, solicita a quantidade e adiciona ao histórico.
    if evento.lower() == "s":
        quantidade_evento = int(input("Quantas vezes? "))
        print("Adicionando serviço ao histórico de manutenções")
        return servico, quantidade_evento
    # Caso contrário, apenas adiciona o serviço ao histórico.
    else:
        print("Adicionando serviço ao histórico de manutenções")
        return servico

marcas_validas = ["Toyota","toyota" , "Ford","ford", "Chevrolet","chevrolet", "Volkswagen","volkswagen", "Honda", "honda", "BMW", "bmw"]
modelos_validos = {
    "Toyota": ["Corolla", "Camry", "Prius", "corolla", "camry", "prius"],
    "Ford": ["Fiesta", "Focus", "Mustang","fiesta", "focus", "mustang"],
    "Chevrolet": ["Cruze", "Malibu", "Impala","cruze", "malibu", "impala"],
    "Volkswagen": ["Golf", "Jetta", "Passat","golf", "jetta", "passat"],
    "Honda": ["Civic", "Accord", "Fit","civic", "accord", "fit"],
    "BMW": ["320i", "X5", "Z4"],

    "toyota": ["Corolla", "Camry", "Prius", "corolla", "camry", "prius"],
    "ford": ["Fiesta", "Focus", "Mustang","fiesta", "focus", "mustang"],
    "chevrolet": ["Cruze", "Malibu", "Impala","cruze", "malibu", "impala"],
    "volkswagen": ["Golf", "Jetta", "Passat","golf", "jetta", "passat"],
    "honda": ["Civic", "Accord", "Fit","civic", "accord", "fit"],
    "bmw": ["320i", "X5", "Z4"]
}

def validar_marca(marca):
    # Este método verifica se a marca do carro é válida.
    return marca in marcas_validas

def validar_modelo(marca, modelo):
    # Este método verifica se o modelo do carro é válido para a marca especificada.
    return modelo in modelos_validos.get(marca, [])

def validar_ano(ano):
    # Este método verifica se o ano do carro é válido.
    try:
        ano = int(ano)
        return 1886 <= ano <= 2024
    except ValueError:
        return False  

def cadastrarCarro(usuario):
    #Permite que o usuário cadastre um novo carro
    while True:
        marca = input("Digite a Marca: ")
        if not validar_marca(marca):
            print("Marca inválida. Por favor, insira uma marca válida.")
            continue

        modelo = input("Digite o Modelo: ")
        if not validar_modelo(marca, modelo):
            print("Modelo inválido para a marca especificada. Por favor, insira um modelo válido.")
            continue

        ano = input("Digite o Ano: ")
        if not validar_ano(ano):
            print("Ano inválido. Por favor, insira um ano entre 1886 e 2024.")
            continue

        usuario.adicionarCarro(marca, modelo, int(ano))
        print("Carro cadastrado!")
        break

def validar_email(email):
    # Este método verifica se o formato do email é válido.
    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao_email, email) is not None

def validar_telefone(telefone):
    # Este método verifica se o formato do número de telefone é válido.
    padrao_telefone = r"^\+?\d{9,15}$"
    return re.match(padrao_telefone, telefone) is not None

def validar_nome(nome):
    # Este método verifica se o formato do nome é válido.
    padrao_nome = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$"
    return re.match(padrao_nome, nome) is not None 

def loginUser():
    # Este método permite o cadastro de um novo usuário e retorna o objeto User correspondente.

    while True:
        # Solicita ao usuário seu nome completo e valida o formato.
        nome = str(input("Digite seu nome completo: "))
        if not validar_nome(nome):
            print("Nome inválido. Por favor, insira um nome válido composto apenas por letras e espaços.")
            continue

        # Solicita ao usuário seu e-mail e valida o formato.
        email = str(input("Digite seu e-mail: "))
        if not validar_email(email):
            print("E-mail inválido. Por favor, tente novamente.")
            continue

        # Solicita ao usuário seu número de telefone e valida o formato.
        telefone = str(input("Digite seu telefone para contato: "))
        if not validar_telefone(telefone):
            print("Número de telefone inválido. Por favor, tente novamente.")
            continue

        # Se todas as informações estiverem corretas, cria um novo objeto User e o retorna.
        novoUser = User(nome, email, telefone)
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
        clear_screen()
        print("Horários Disponíveis: \n")
        sistema.listarHorarios()
        horario_marcado = sistema.marcarHorario()
            
        match opcaoPreventiva:
            case "1":
                sistema.marcarServico(1, usuario,carro,horario_marcado)
                break
            case "2":
                sistema.marcarServico(2, usuario,carro,horario_marcado)
                break
            case "3":
                sistema.marcarServico(3, usuario,carro,horario_marcado)
                break
            case "4":
                sistema.marcarServico(4, usuario,carro,horario_marcado)
                break
            case "5":
                sistema.marcarServico(5, usuario,carro,horario_marcado)
                break
            case "6":
                print("Saindo")
                break
            case _:
                print("Opção inválida")
        idServico = int(opcaoPreventiva)
        
        sistema.marcarServico(idServico, usuario,carro,horario_marcado)

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
            carro.agendarServico()
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
        try:
            usuario_index = int(input("Selecione o número do usuário: ")) -1
            if 0 <= usuario_index < len(usuarios):
                return usuarios[usuario_index]
            else:
                print("Por favor, selecione um número de usuário válido.")
        except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
def obterCarro():
    #Permite que o usuário selecione um usuário da lista.
    usuario.listarCarros()
    while True:
        try:
            carro_index = int(input("Selecione o número do carro: ")) -1
            if 0 <= carro_index < len(usuario.carros):
                return usuario.carros[carro_index]
            else:
                print("Por favor, selecione um número de carro válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

## Menu Principal
usuarios = []

while True: 
    print("\n==== Menu ====")
    print("1. Cadastro de Usuário")
    print("2. Cadastrar Carro")
    print("3. Manutenção Preventiva")
    print("4. Histórico de Manutenções")
    print("5. Pagamento de Serviços")
    print("6. Serviços Marcados")
    print("7. Serviços Agendados")
    print("8. Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        clear_screen()
        novoUser = loginUser()
        usuarios.append(novoUser)
        print("Usuário cadastrado com sucesso!")
    elif opcao == "2":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            clear_screen()
            usuario = obterUsuario()
            clear_screen()
            novoCarro = cadastrarCarro(usuario)
    elif opcao == "3":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            clear_screen()
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                clear_screen()
                carro = obterCarro()
                clear_screen()
                manutencaoPreventiva(usuario,carro)
    elif opcao == "4":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            clear_screen()
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                clear_screen()
                carro = obterCarro()
                clear_screen()
                carro.adicionarReparoAoHistorico()


    elif opcao == "5":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            clear_screen()
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                clear_screen()
                carro = obterCarro()
                clear_screen()
                pagarServico(carro)
    elif opcao == "6":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            clear_screen()
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                clear_screen()
                carro = obterCarro()
                if not carro.servicosMarcados :
                    print ("Nenhum serviço marcado")
                else:
                    clear_screen()
                    carro.listarServicosMarcados()
                    print("Seu serviço está marcado, prossiga para o pagamento do serviço para confirma-lo")
    elif opcao == "7":
        if len(usuarios) == 0:
            print("Cadastre um usuário primeiro!")
        else:
            clear_screen()
            usuario = obterUsuario()
            if len(usuario.carros) == 0:
                print("Cadastre um carro primeiro!")
            else: 
                clear_screen()
                carro = obterCarro()
                if not carro.servicosAgendados :
                    print ("Nenhum serviço Agendado")
                else:
                    clear_screen()
                    carro.listarServicosAgendados()
    elif opcao == "8":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
