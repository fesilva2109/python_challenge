
import os 

## Criando classe carro
class Carro: 
    carros = []
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Carro.carros.append(self)
    def __str__(self):
        return f" {self.marca} |{self.modelo} | {self.ano}"
    @staticmethod
    def apresentarCarro():
        for carro in Carro.carros:
            print(f"Marca: {carro.marca} | Modelo: {carro.modelo} | Ano: {carro.ano}")
    
## Criando classe usuário
class User:
    def __init__(self, nomeUser, email, telefoneContato):
        self.nomeUser = nomeUser
        self.email = email
        self.telefoneContato = telefoneContato
    def __str__(self):
        return f" {self.nomeUser} |{self.email} | {self.telefoneContato} "
    @staticmethod
    def apresentarInformacoesUser(user):
        print(f"Nome: {user.nomeUser} | E-mail: {user.email} | Telefone para contato: {user.telefoneContato}")

class Servico:
    def __init__(self, nomeServico, preco, idServico, status):
        self.nomeServico = nomeServico
        self.preco = preco 
        self.idServico = idServico
        self.status = status  
        
    def __str__(self):
        return f"{self.nomeServico}  {self.preco}  {self.idServico} {self.status} "


    
class SistemaDeEncomendas:
    servicosDisponiveis = []
    servicosEncomendados = []
    def __init__(self):
        self.servicosDisponiveis = []
        self.servicosEncomendados = []
            
    def __str__(self):
        return f"{self.servicosDisponiveis}  {self.servicosEncomendados} "
    
    def adicionarServicoDisponivel(self, nomeServico, preco, idServico, status):
        novoServico = Servico(nomeServico, preco, idServico, status)
        self.servicosDisponiveis.append(novoServico)
        print("Serviço adicionado com sucesso")

    
    

    def adicionarServico(servico):
        SistemaDeEncomendas.servicosDisponiveis.append(servico)

    def encomendarServico(idServico):
        for servico in SistemaDeEncomendas.servicosDisponiveis:
            if servico.idServico == idServico:
                servico.status = "Encomendado"
                SistemaDeEncomendas.servicosEncomendados.append(servico)
                print("Serviço encomendado com sucesso")
                return True
        print("Serviço não encontrado ")
        return False

    def listarServicosDisponiveis():
        print("Serviços Disponíveis:")
        for servico in SistemaDeEncomendas.servicosDisponiveis:
            print(f"ID: {servico.idServico} - Nome: {servico.nomeServico} - Preço: R${servico.preco}")

    def listarServicosEncomendados():
        print("Serviços Encomendados:")
        for servico in SistemaDeEncomendas.servicosEncomendados:
            print(f"ID: {servico.idServico} - Nome: {servico.nomeServico} - Preço: R${servico.preco}")

    def apresentarServico(servico):
        if servico.status == False:
            servico.status = "Não Concluído"
        print(f"Serviço: {servico.nomeServico} | Preço: {servico.preco} | ID: {servico.idServico} | Status: {servico.status}")



            
## Funções
def cadastrarCarro():
    novoCarro = Carro(input("Digite a Marca: "),input("Digite o Modelo: "),int(input("Digite o Ano: ")))
    Carro.apresentarCarro()
  
def loginUser():
    novoUser = User(input("Digite seu nome completo: "), input("Digite seu e-mail: "), input("Digite seu telefone para contato: "))
    User.apresentarInformacoesUser(novoUser)
    

  
def manutencaoPreventiva():
    sistema  = SistemaDeEncomendas()
    sistema.adicionarServicoDisponivel("Troca de Farol", 200, 1, False )
    
    while True:
        print("Escolha o tipo de serviço que será executado: \n")
        print("1. Trocar baterias")
        print("2. Trocar faróis")
        print("3. Trocar óleo")
        print("4. Sair ")
        sistema.listarServicosDisponiveis()

        opcaoPreventiva = input("Selecione a opção: ")

        match opcaoPreventiva: 
            case "1":
                sistema.encomendarServico(1)
                print("Marcando troca de baterias")
                break
            case "2":
               
                break
            case "3":     
              
                break
            case "4":
                print("Saindo")

                break
            case _:
                print("Opção inválida")

def valorTotalServicos():
        preco_servico = sum(servico.preco for servico in SistemaDeEncomendas.self.servicos)
            
        print(preco_servico)
        taxaServico = preco_servico*0.03
        total = preco_servico + taxaServico

        return total, taxaServico, preco_servico                
def pagarServico():
    
    total_com_taxa, taxa_de_servico, preco_servico = Servico.valorTotalServicos()


    print(f"""
            1- Debito
            2- Crédito
            3- Pix
            4- Dinheiro
            """)
    forma_pagamento = int(input("Escolha a forma de pagamento: "))
    if forma_pagamento > 4:
        print("Inválido! Por favor digitar uma forma de pagamento válida")

    match forma_pagamento:
        case 1:
            print("=== Débito ===\n")
            print("Valor do produto: ", preco_servico)
            print("Taxa de serviço:", taxa_de_servico)
            print("Total com taxa de serviço:", total_com_taxa)
            resposta = input("\n Deseja Proseguir com o pagamento? ")
            if resposta =="s" or "sim":
                print("Serviço encomendado com sucesso!")
                for servico in Servico.servicos:
                    servico.status = "Serviço Encomendado"
            else:
                os.system("cls")
                print("Saindo...")   
        case 2:
            print("Crédito")
            parcela = int(input("Em quantas vezes deseja parcelar: "))
            valor_final = valor / parcela
            print(valor_final)
            print(taxaServico)
        case 3:
            print("Pix")
        case 4:
            print("Dinheiro")

## Menu Principal
while True: 
    print("\n==== Menu ====")
    print("1. Cadastro de Usúario")
    print("2. Cadastrar Carro")
    print("3. Manutenção Preventiva")
    print("4. Histórico de Manutenção")
    print("5. Serviços Agendados")
    print("6. Pagamento Online")
    print("7. Sair")

    opcao = input("Selecione uma opção: ")
    match opcao: 
        case "1":
            os.system("cls")
            loginUser()
        case "2":
            os.system ("cls")
            cadastrarCarro()
        case "3":
            os.system ("cls")
            print("Acionando serviço de manutenção preventiva")
            manutencaoPreventiva()
            print()
        case "4":
            os.system ("cls")
            print("Apresentando Histórico de Manutenção")
            print()
        case "5": 
            os.system("cls")
            print("Serviços Agendados: ")
            SistemaDeEncomendas.listarServicosEncomendados()
            
            
        case "6":
            pagarServico()
        case "7":
            os.system ("cls")
            print("Saindo...")
            break
        case _:
            print("Opção inválida")


