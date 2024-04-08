import os 
os.system("cls")
def agendamentoDeServicos():
    listaDeServicos = []
    listaServicoMotor = []
    listaServicoTransmissao = []
    listaServicoChassi = []
    listaServicoSuspensao = []
    listaServicoSistemaLubrificacao = []
    listaServicoSistemaArrefecimento = []
    listaServicoSistemaFreio = []
    listaServicoSistemaCombustivel = []
    listaServicoSistemaEscape= []
    listaServicoSistemaDirecao = []
    listaServicoSistemaEletrico = []

    def menuMotor():
        while True: 
            servico1 = print("1. Vazamento do óleo do cárter")
            servico2 = print("2. Superaquecimento devido a falhas no sistema de arrefecimento")
            servico3 = print("3. Desgaste dos pistões e anéis")
            servico4 = print("4. Falha na bomba de óleo")
            servico5 = print("5. Problemas de ignição (velas ou bobinas)")
            servico6 = print("6. Danos à cabeça do cilindro")
            servico7 = print("7. Falha na corrente de distribuição ou correia dentada")
            print("8. Sair")

            opcaoMotor = input("Selecione uma opção: ")

            match opcaoMotor:
                case  "1":
                    os.system ("cls")
                    listaServicoMotor.append(servico1)
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    listaServicoMotor.append(servico2)
                    print("")
                    break 
                case "3":
                    os.system("cls")
                    listaServicoMotor.append(servico3)
                    print("")
                case "4":
                    listaServicoMotor.append(servico4)
                case "5":
                    listaServicoMotor.append(servico5)
                case "6":
                    listaServicoMotor.append(servico6)
                case "7":
                    listaServicoMotor.append(servico7)
                case "8":
                    os.system("cls")
                    print("Saindo..")

                
            


    def menuTransmissao():
        while True: 
            print("1. Transmissão escorregando entre as marchas")
            print("2. Ruídos anormoais")
            print("3. Vazamentos de fluído de transmissão")
            print("4. Engates duros ou imprecisos")
            print("5. Desgaste ou danos nas engrenagens")
            print("6. Sair")

            opcaoTransmissao = input("Selecione uma opção: ")

            match opcaoTransmissao:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()
    def menuChassi():
        while True: 
            print("1. Corrosão ou ferrugem na estrutura")
            print("2. Desalinhamento devido a impactos")
            print("3. Soldas quebradas ou rachadas")
            print("4. Danos estruturais devido a acidentes")
            print("5. Sair")

            opcaoChassi = input("Selecione uma opção: ")

            match opcaoChassi:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()
    def menuSuspensao():
        while True: 
            print("1. Amortecedores vazando ou desgastados")
            print("2. Molas quebradas ou enfraquecidas")
            print("3. Barras estabilizadoras danificadas")
            print("4. Buchas desgastadas")
            print("5. Desalinhamento ou desbalanceamento das rodas")
            print("6. Sair")

            opcaoSuspensao = input("Selecione uma opção: ")

            match opcaoSuspensao:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()

    def menuSistemaLubrificacao():
        while True: 
            print("1. Vazamento do óleo do motor")
            print("2. Baixa pressão do óleo")
            print("3. Filtro de óleo entupido")
            print("4. Desgaste dos mancais ou bronzinas")
            print("5. Contaminação do óleo por líquido de arrefecimento")
            print("6. Sair")

            opcaoMotor = input("Selecione uma opção: ")

            match opcaoMotor:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()

    def menuSistemaArrefecimento():
        while True: 
            print("1. Vazamento no radiador")
            print("2. Termostato com defeito")
            print("3. Bomba d'água vazando ou com falha")
            print("4. Corrosão nos componentes do sistemas")
            print("5. Ventilador de refrigeração com problemas")
            print("6. Sair")

            opcaoMotor = input("Selecione uma opção: ")

            match opcaoMotor:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()
    def menuSistemaFreio():
        while True: 
            print("1. Pedal de freio esponjoso")
            print("2. Freios rangendo ou chiando")
            print("3. Falha na frenagem, como pedal afundando até o chão")
            print("4. Vazamentos de fluido de freio")
            print("5. Desgaste excessivo das pastilhas ou tambores")
            print("6. Sair")

            opcaoMotor = input("Selecione uma opção: ")

            match opcaoMotor:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()

    
    def menuSistemaCombustivel():
        while True: 
            print("1. Bomba de comnustível com defeito")
            print("2. Vazamento de combustível nas linhas ou conexões")
            print("3. Injetores entupidos ou com defeito")
            print("4. Filtro de combustível obstruído")
            print("5.Problenas na pressão de combustível")
            print("6. Sair")

            opcaoCombustivel = input("Selecione uma opção: ")

            match opcaoCombustivel:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()
    def menuSistemaEscape():
        while True: 
            print("1. Ruído excessivo do escapamento")
            print("2. Vazamentos nos coletores de escape")
            print("3. Catalisador danificado ou obstruído")
            print("4. Corrosão ou danos nos tubos de escape")
            print("5. Problemas com sensores de oxigênio")
            print("6. Sair")

            opcaoEscape = input("Selecione uma opção: ")

            match opcaoEscape:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()
    
    def menuSistemaDirecao():
        while True: 
            print("1. Vazamento do óleo do cárter")
            print("2. Superaquecimento devido a falhas no sistema de arrefecimento")
            print("3. Desgaste dos pistões e anéis")
            print("4. Falha na bomba de óleo")
            print("5. Problemas de ignição (velas ou bobinas)")
            print("6. Danos à cabeça do cilindro")
            print("7. Falha na corrente de disttribuição ou correia dentad")
            print("8. Sair")

            opcaoMotor = input("Selecione uma opção: ")

            match opcaoMotor:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()   
    def menuSistemaEletrico():
        while True: 
            print("1. Fusíveis queimados")
            print("2. Falha na bateria ou alternador")
            print("3. Luzes queimadas")
            print("4. Problemas com o sistema de partida")
            print("5. Falha nos componentes eletrônicos, como sensores ou atuadores")
            print("6. Sair")

            opcaoMotor = input("Selecione uma opção: ")

            match opcaoMotor:
                case  "1":
                    os.system ("cls")
                    print("Agendando serviço relacionado ao vazamento de óleo")
                    break
                case "2":
                    os.system ("cls")
                    print("Devido a falha do sistema de arrefecimento, direcionaremos-o para a sessão de serviços relacionados ao arrefecimento.")
                    break 
                case "3":
                    os.system("cls")
                    print()
                            
    while True: 
        os.system ("cls")
        print("Escolha o tipo de serviço que será executado: \n")
        print("1. Motor")
        print("2. Transmissão")
        print("3. Chassi")
        print("4. Supensão")
        print("5. Sistema de Lubrificação")
        print("6. Sistema de Arrefecimento")
        print("7. Sistema de Freio")
        print("8. Sistema de Combustível")
        print("9. Sistema de Escape")
        print("10. Sistema de Direção")
        print("11. Sistema Elétrico")
        print("12. Sair ")

        opcaoServico = input("Selecione a opção: ")
        match opcaoServico:
            case "1":
                os.system ("cls")
                menuMotor()
                break
            case "2":
                os.system("cls")
                menuTransmissao()
                break
            case "3":
                os.system("cls")
                menuChassi()
                break
            case "4":
                os.system("cls")
                menuSuspensao()
                break
            case "5":
                os.system("cls")
                menuSistemaLubrificacao()
                break
            case "6":
                os.system("cls")
                menuSistemaArrefecimento()
                break
            case "7":
                os.system("cls")
                menuSistemaFreio()
                break
            case "8":
                os.system("cls")
                menuSistemaCombustivel()
                break
            case "9":
                os.system("cls")
                menuSistemaEscape()
                break
            case "10":
                os.system("cls")
                menuSistemaDirecao()
                break
            case "11":
                os.system("cls")
                menuSistemaEletrico()
                break
            case "12":
                os.system("cls")
                print("Saindo...")
                break



                        