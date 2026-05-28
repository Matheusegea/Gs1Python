Astronautas = []

Desfazer_Pilha = []


# BUSCA BINÁRIA
def buscar_astronauta_por_id(lista, id_alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio]["id"] == id_alvo:
            return lista[meio]
        elif lista[meio]["id"] < id_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1         
    return None


def cadastrar_novo_astronauta(lista, novo_astronauta):
    id_novo = novo_astronauta["id"]
    
    # Encontra a posição correta onde o novo ID deve entrar
    posicao = 0
    while posicao < len(lista) and lista[posicao]["id"] < id_novo:
        posicao += 1
        
    lista.insert(posicao, novo_astronauta)

# RECURSÃO
def calcular_media_saude(lista, indice=0):
    # Caso Base
    if indice == len(lista):
        return 0, 0
    
    soma_restante, qtd_restante = calcular_media_saude(lista, indice + 1)
    
    if lista[indice]["status"] == "No Espaço":
        media_atual = (lista[indice]["fisico"] + lista[indice]["psicologico"]) / 2
        return soma_restante + media_atual, qtd_restante + 1
    else:
        return soma_restante, qtd_restante

# PILHAS
def atualizar_missao_astronauta(id_astronauta, nova_missao):
    astronauta = buscar_astronauta_por_id(Astronautas, id_astronauta)
    if astronauta:
        # Guarda o estado atual na pilha antes de modificar
        estado_anterior = {
            "id": astronauta["id"],
            "missao_antiga": astronauta["missao"],
            "status_antigo": astronauta["status"]
        }
        Desfazer_Pilha.append(estado_anterior) 
        
        astronauta["missao"] = nova_missao
        astronauta["status"] = "No Espaço" 
        
        print(f"\n[Sucesso] {astronauta['nome']} foi designado para a nova missão '{nova_missao}'")
    else:
        print("\n[Erro] Astronauta não encontrado para atualização.")


def desfazer_ultima_alteracao():
    if not Desfazer_Pilha:
        print("\n[Aviso] Nada para desfazer. A pilha de UNDO está vazia!")
        return

    ultimo_comando = Desfazer_Pilha.pop() 
    
    astronauta = buscar_astronauta_por_id(Astronautas, ultimo_comando["id"])
    if astronauta:
        astronauta["missao"] = ultimo_comando["missao_antiga"]
        if "status_antigo" in ultimo_comando:
            astronauta["status"] = ultimo_comando["status_antigo"]
        print(f"\n[UNDO] Alteração desfeita! {astronauta['nome']} voltou para a missão '{astronauta['missao']}' com o local: '{astronauta['status']}'.")


def analisar_saude_pos_missao(id_astronauta, duracao_em_meses):
    astronauta = buscar_astronauta_por_id(Astronautas, id_astronauta)
    
    if astronauta:
        if astronauta["status"] == "Na Terra":
            print(f"\n[Aviso] {astronauta['nome']} já se encontra na Terra em período de repouso.")
            return

        # Modifica o status para que ele não conte mais na média de saúde espacial!
        astronauta["status"] = "Na Terra"

        # -1.5% de perda de massa muscular/óssea por mês (físico)
        desgaste_fisico = duracao_em_meses * 1.5
        # -2.0% de fadiga mental/isolamento por mês (psicológico)
        desgaste_psicologico = duracao_em_meses * 2.0
        
        novo_fisico = max(0, astronauta["fisico"] - desgaste_fisico)
        novo_psicologico = max(0, astronauta["psicologico"] - desgaste_psicologico)
        nova_media_combinada = (novo_fisico + novo_psicologico) / 2
        
        astronauta["fisico"] = novo_fisico
        astronauta["psicologico"] = novo_psicologico

        print(f"\n" + "-"*45)
        print(f"  RELATÓRIO MÉDICO PÓS-MISSÃO: {astronauta['nome'].upper()}")
        print(f"-"*45)
        print(f"Status Atualizado: RETORNOU PARA A TERRA")
        print(f"Tempo no Espaço: {duracao_em_meses} meses")
        print(f"Saúde Física Atual: {novo_fisico:.1f}%")
        print(f"Saúde Psicológica Atual: {novo_psicologico:.1f}%")
        print(f"Índice de Prontidão Geral: {nova_media_combinada:.1f}%")
        print(f"-"*45)
        
        if nova_media_combinada < 35:
            print("[ALERTA MÉDICO] Estado critico atingido. Encaminhar para reabilitação")
        else:
            print("[STATUS] Astronauta apto para iniciar período padrão de quarentena e repouso.")
    else:
        print("\n[Erro] Astronauta não encontrado")

# INTERFACE DE LINHA DE COMANDO
def menu():
    while True:
        print("\n" + "="*82)
        print("NEUROSPACE - SISTEMA DE ANALISE E GERENCIAMENTO DE MISSÕES ESPACIAIS E ASTRONAUTAS")
        print("="*82)
        print("1. Cadastrar Novo Astronauta / Missão")
        print("2. Buscar Astronauta por ID")
        print("3. Calcular Média de Saúde (Apenas Ativos em missões)")
        print("4. Atualizar Missão de um Astronauta")
        print("5. Desfazer Última Alteração")
        print("6. Analisar Impacto de Saúde Pós-Missão (Retorno à Terra)")
        print("7. Listar Todos os Astronautas e Missões")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- CADASTRO DE NOVA MISSÃO ---")
            id_novo = int(input("Digite o ID (int) do astronauta: "))
            
            if buscar_astronauta_por_id(Astronautas, id_novo) is not None:
                print("\n[Erro] Já existe um astronauta cadastrado com este ID!")
                continue
                
            nome_novo = input("Nome do astronauta: ")
            novo_fisico = int(input("Nota de saúde física (0 a 100): "))
            novo_psicologico = int(input("Nota de saúde psicológica (0 a 100): "))
            nova_missao = input("Nome da Missão: ")
            
            novo_registro = {
                "id": id_novo,
                "nome": nome_novo,
                "fisico": novo_fisico,
                "psicologico": novo_psicologico,
                "missao": nova_missao,
                "status": "No Espaço" 
            }
            
            cadastrar_novo_astronauta(Astronautas, novo_registro)
            print(f"\n[Sucesso] '{nome_novo}' cadastrado com sucesso na missão '{nova_missao}'!")
        
        elif opcao == "2":
            id_busca = int(input("Digite o ID (int) do astronauta: "))
            resultado_busca = buscar_astronauta_por_id(Astronautas, id_busca)
            if resultado_busca:
                print(f"\nAstronauta Encontrado:\n Nome: {resultado_busca['nome']}\n Físico: {resultado_busca['fisico']:.1f}%\n Psicológico: {resultado_busca['psicologico']:.1f}%\n Local: {resultado_busca['status']}\n Missão: {resultado_busca['missao']}")
            else:
                print("\n[!] Astronauta não localizado.")
                
        elif opcao == "3":
            soma, quantidade = calcular_media_saude(Astronautas)
            media = soma / quantidade if quantidade > 0 else 0
            print(f"\n[Análise] A média de prontidão de saúde apenas dos astronautas NO ESPAÇO é: {media:.2f}% (Total: {quantidade} ativos)")
            
        elif opcao == "4":
            id_astronauta = int(input("Digite o ID (int) do astronauta: "))
            nova_missao = input("Digite o nome da nova Missão: ")
            atualizar_missao_astronauta(id_astronauta, nova_missao)
            
        elif opcao == "5":
            desfazer_ultima_alteracao()
            
        elif opcao == "6":
            print("\n--- SIMULAÇÃO DE SAÚDE RETORNO DE MISSÃO ---")
            id_analise = int(input("Digite o ID (int) do astronauta que retornou: "))
            meses_no_espaco = int(input("Quantos meses durou a missão espacial? "))
            analisar_saude_pos_missao(id_analise, meses_no_espaco)
            
        elif opcao == "7":
            print("\nAstronautas Cadastrados e suas Missões:")
            for dados in Astronautas:
                print(f"ID: {dados['id']} | Nome: {dados['nome']} | Local: {dados['status']} | Missão: {dados['missao']} | Físico: {dados['fisico']:.1f}% | Psicologico: {dados['psicologico']:.1f}%")
                
        elif opcao == "0":
            print("\nSistema encerrado")
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    menu()