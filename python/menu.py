import os 
os.system ("cls")
## criando classe carro
class Carro: 
    carros = []
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Carro.carros.append(self)
    def __str__(self):
      return f" {self.marca} |{self.modelo} | {self.ano}"
    def apresentarCarro(carro):
        for carro in Carro.carros:
            print(f"Marca: {carro.marca} | Modelo: {carro.modelo} | Ano: {carro.ano}")
    
## Criando classe usuário
class User:
    def __init__(self, nomeUser, email, telefoneContato):
        self.nomeUser = nomeUser
        self.email = email
        self.telefoneContato = telefoneContato
    def __str__(self):
      return f" {self.nomeUser} |{self.email} | {self.telefoneContato}"
    def apresentarInformacoesUser(user):
        print(f"Nome: {user.nomeUser} | E-mail: {user.email} | Telefone para contato: {user.telefoneContato}")
        
## Listas de serviços
servicos = []
servicosPreventivos = []

## Funções
def cadastrarCarro():
    novoCarro = Carro(input("Digite a Marca: "),input("Digite o Modelo: "),int(input("Digite o Ano: ")))
    Carro.apresentarCarro(novoCarro)
  
def loginUser():
    novoUser = User(input("Digite seu nome completo: "), input("Digite seu e-mail: "), input("Digite seu telefone para contato: "))
    User.apresentarInformacoesUser(novoUser)
def manutencaoPreventiva():
    while True:
        print("Escolha o tipo de serviço que será executado: \n")
        print("1. Trocar baterias")
        print("2. Trocar faróis")
        print("3. Trocar óleo")
        print("4. Sair ")

        opcaoPreventiva = input("Selecione a opção: ")

        match opcaoPreventiva: 
            case "1":
                print("Marcando a troca de baterias")
                trocaBateria = 1
                servicosPreventivos.append(trocaBateria)
                break
            case "2":
                print("Marcando a troca de faróis")
                trocaFarol = 2
                servicosPreventivos.append(trocaFarol)
                break
            case "3":     
                print("Marcando a troca de óleo")  
                trocaOleo = 3
                servicosPreventivos.append(trocaOleo)
                break
            case "4":
                print("Saindo")

                break
            case _:
                print("Opção inválida")

## Menu Principal
while True: 
    print("==== Menu ====")
    print("1. Login")
    print("2. Cadastrar Carro")
    print("3. Apresentar Carros")
    print("4. Manutenção Preventiva")
    print("5. Histórico de Manutenção")
    print("6. Serviços Agendados")
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
           print("Carros: ")
           print(carros)
        case "4":
            os.system ("cls")
            print("Acionando serivço de manutenção preventiva")
            manutencaoPreventiva()
            print(servicosPreventivos)
            
        case "5": 
            os.system ("cls")
            print("Apresentando Despesas")
            print(despesas)
        case "6":
            print("Serviços Agendados: ")
            print(servicosAgendados)
        case "7":
            os.system ("cls")
            print("Saindo...")
            break
        case _:
                print("Opção inválida")
        
        
        

