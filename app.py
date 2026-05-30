"""
NEUROSPACE - SISTEMA DE TRIAGEM E GERENCIAMENTO DE MISSÕES ESPACIAIS

Este sistema gerencia registros de astronautas mantendo-os estruturalmente 
ordenados por ID desde o cadastro. A busca binária apenas localiza os dados 
sem realizar ordenações internas.

Padrão de nomenclatura: PEP 8 (snake_case)
"""
astronautas = []

pilhas_logs = []

viagens_validas = ["Mercúrio", "Vênus", "Marte", "Júpiter", "Saturno", "Urano", "Netuno", "Plutão", "Sol", "Lua"]


# 1. REQUISITO: BUSCA BINÁRIA (SEM ORDENAR INTERNAMENTE)
def buscar_astronauta_por_id(lista, id_alvo):
    """
    Busca um astronauta na lista utilizando o algoritmo de Busca Binária.

    =======================================================================
    ANÁLISE DE COMPLEXIDADE COMPUTACIONAL (BIG-O)
    -----------------------------------------------------------------------
    - Caso Médio e Pior Caso: O(log n)
    - Justificativa: O algoritmo divide o espaço de busca pela metade a cada 
      iteração do loop. Nenhuma ordenação (como .sort()) é executada aqui dentro, 
      o que respeita a exigência de não ordenar durante a busca e garante a 
      eficiência logarítmica pura.
    =======================================================================
    """
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


# 2. FUNÇÃO: INSERÇÃO ORDENADA (CADASTRO)
def cadastrar_novo_astronauta(lista, novo_astronauta):
    """
    Insere um novo registro na posição correta para que a lista permaneça organizada.

    =======================================================================
    ANÁLISE DE COMPLEXIDADE COMPUTACIONAL (BIG-O)
    -----------------------------------------------------------------------
    - Caso Médio e Pior Caso: O(n)
    - Justificativa: A função percorre a lista linearmente para achar o ponto 
      exato onde o ID deve ser inserido. O método '.insert()' desloca os elementos 
      subsequentes na memória, operando em tempo linear proporcional a 'n'.
    =======================================================================
    """
    id_novo = novo_astronauta["id"]
    posicao = 0
    
    # Encontra posicionalmente onde o ID deve entrar
    while posicao < len(lista) and lista[posicao]["id"] < id_novo:
        posicao += 1
        
    lista.insert(posicao, novo_astronauta)


# 3. REQUISITO: RECURSÃO (MÉDIA DE SAÚDE DOS ATIVOS EM MISSÃO)
def calcular_media_saude(lista, indice=0):
    """
    Calcula recursivamente a soma das médias e a quantidade de astronautas 
    ativos em missões (cujo status atual não é 'Na Terra').

    =======================================================================
    ANÁLISE DE COMPLEXIDADE COMPUTACIONAL (BIG-O)
    -----------------------------------------------------------------------
    - Caso Médio e Pior Caso: O(n)
    - Justificativa: A função visita cada elemento da lista exatamente uma vez 
      avançando via 'indice + 1'. O número de chamadas empilhadas cresce linearmente 
      com o tamanho total da lista.
    =======================================================================
    """
    # Caso Base
    if indice == len(lista):
        return 0, 0
    
    # Passo Recursivo
    soma_restante, qtd_restante = calcular_media_saude(lista, indice + 1)
    
    # Filtra tripulantes que não estão na Terra
    if lista[indice]["status"] != "Na Terra":
        media_atual = (lista[indice]["fisico"] + lista[indice]["psicologico"]) / 2
        return soma_restante + media_atual, qtd_restante + 1
    else:
        return soma_restante, qtd_restante


# 4. REQUISITO: PILHAS (SISTEMA DE LOGS DE AUDITORIA)
def empilhar_log(mensagem):
    """
    Adiciona uma mensagem de log ao topo da pilha de auditoria do sistema.

    =======================================================================
    ANÁLISE DE COMPLEXIDADE COMPUTACIONAL (BIG-O)
    -----------------------------------------------------------------------
    - Caso Médio e Pior Caso: O(1)
    - Justificativa: A inserção no final de uma lista em Python (função .append) 
      atua como o topo de uma pilha. Ela é executada em tempo constante, pois 
      não exige a reorganização ou deslocamento de outros elementos na memória.
    =======================================================================
    """
    pilhas_logs.append(mensagem)


def exibir_pilha_logs():
    """
    Desempilha e exibe os logs do sistema seguindo a lógica LIFO (Last In, First Out).
    """
    if not pilhas_logs:
        print("\n[Aviso] A pilha de logs de auditoria está vazia.")
        return
    
    print("\n--- EXIBINDO PILHA DE LOGS (DO MAIS RECENTE AO MAIS ANTIGO) ---")
    # Copia a pilha para desempilhar sem destruir o histórico principal do sistema
    pilha_auxiliar = pilhas_logs.copy()
    
    while len(pilha_auxiliar) > 0:
        log = pilha_auxiliar.pop()  # Remove e retorna o elemento do topo
        print(f"[LOG] {log}")


# 5. FUNÇÕES ADICIONAIS E REGRAS DE NEGÓCIO
def atualizar_missao_astronauta(id_astronauta, nova_missao, novo_planeta):
    """
    Altera a missão de um tripulante e redefine seu planeta de destino atual.
    """
    astronauta = buscar_astronauta_por_id(astronautas, id_astronauta)
    if astronauta:
        astronauta["missao"] = nova_missao
        astronauta["status"] = f"Em {novo_planeta}"
        
        mensagem_log = f"Missão do ID {id_astronauta} alterada para '{nova_missao}' em {novo_planeta}."
        empilhar_log(mensagem_log)
        
        print(f"\n[Sucesso] {astronauta['nome']} alocado na missão '{nova_missao}' com destino a {novo_planeta}!")
    else:
        print("\n[Erro] Astronauta não encontrado para atualização.")


def analisar_saude_pos_missao(id_astronauta, duracao_em_meses):
    """
    Simula o impacto de desgaste físico/psicológico e retorna o tripulante à Terra.
    """
    astronauta = buscar_astronauta_por_id(astronautas, id_astronauta)
    
    if astronauta:
        if astronauta["status"] == "Na Terra":
            print(f"\n[Aviso] {astronauta['nome']} já se encontra em repouso na Terra.")
            return

        planeta_anterior = astronauta["status"]
        astronauta["status"] = "Na Terra"

        desgaste_fisico = duracao_em_meses * 1.5
        desgaste_psicologico = duracao_em_meses * 2.0
        
        novo_fisico = min(100.0, max(0.0, astronauta["fisico"] - desgaste_fisico))
        novo_psicologico = min(100.0, max(0.0, astronauta["psicologico"] - desgaste_psicologico))
        nova_media_combinada = (novo_fisico + novo_psicologico) / 2
        
        astronauta["fisico"] = novo_fisico
        astronauta["psicologico"] = novo_psicologico

        mensagem_log = f"Astronauta ID {id_astronauta} retornou à Terra após {duracao_em_meses} meses no espaço."
        empilhar_log(mensagem_log)

        print("\n" + "-"*45)
        print(f"  RELATÓRIO MÉDICO PÓS-MISSÃO: {astronauta['nome'].upper()}")
        print("-"*45)
        print(f"Origem do Retorno: {planeta_anterior}")
        print(f"Status Atual: RETORNOU PARA A TERRA (Removido da Média Espacial)")
        print(f"Tempo de Exposição Espacial: {duracao_em_meses} meses")
        print(f"Saúde Física Atual: {novo_fisico:.1f}% (-{desgaste_fisico}%)")
        print(f"Saúde Psicológica Atual: {novo_psicologico:.1f}% (-{desgaste_psicologico}%)")
        print(f"Índice de Prontidão Geral: {nova_media_combinada:.1f}%")
        print("-"*45)
        
        if nova_media_combinada < 35:
            print("[ALERTA MÉDICO] Estado crítico atingido. Encaminhar para reabilitação imediata!")
        else:
            print("[STATUS] Astronauta em parâmetros seguros. Liberado para quarentena e repouso.")
    else:
        print("\n[Erro] Astronauta não encontrado para simulação pós-missão.")


def escolher_viagem_menu():
    """
    Exibe as opções válidas de planetas e retorna o nome escolhido.
    """
    while True:
        print("\n--- SELEÇÃO DE DESTINO ---")
        for i, planeta in enumerate(viagens_validas, start=1):
            print(f"{i}. {planeta}")
        
        try:
            escolha = int(input("Escolha o número correspondente a Viagem: "))
            if 1 <= escolha <= len(viagens_validas):
                return viagens_validas[escolha - 1]
            else:
                print(f"[Erro] Seleção inválida. Escolha um número de 1 a {len(viagens_validas)}.")
        except ValueError:
            print("[Erro Entrada] Digite apenas o número inteiro da opção.")


# INTERFACE DE LINHA DE COMANDO
def menu():
    while True:
        print("\n" + "="*82)
        print("NEUROSPACE - SISTEMA DE ANALISE E GERENCIAMENTO DE MISSÕES ESPACIAIS E ASTRONAUTAS")
        print("="*82)
        print("1. Cadastrar Novo Astronauta / Missão")
        print("2. Buscar Astronauta por ID")
        print("3. Calcular Média de Saúde (Apenas Ativos em Missões)")
        print("4. Atualizar Missão de um Astronauta (Envia para outro Planeta)")
        print("5. Analisar Impacto de Saúde Pós-Missão (Retorno à Terra)")
        print("6. Listar Todos os astronautas e Missões")
        print("7. Exibir Pilha de Logs do Sistema")
        print("0. Sair")
        print("="*82)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            print("\n--- CADASTRO DE NOVA MISSÃO ---")
            try:
                id_novo = int(input("Digite o ID (Apenas números inteiros): "))
            except ValueError:
                print("\n[Erro Entrada] O ID precisa ser obrigatoriamente um número inteiro!")
                continue
            
            if buscar_astronauta_por_id(astronautas, id_novo) is not None:
                print("\n[Erro Cadastro] Já existe um astronauta cadastrado com este ID!")
                continue
                
            nome_novo = input("Nome do astronauta: ").strip()
            if not nome_novo:
                print("\n[Erro Entrada] O nome não pode ser deixado em branco!")
                continue

            try:
                novo_fisico = int(input("Nota de saúde física (0 a 100): "))
                novo_psicologico = int(input("Nota de saúde psicológica (0 a 100): "))
                if not (0 <= novo_fisico <= 100) or not (0 <= novo_psicologico <= 100):
                    print("\n[Erro Entrada] As notas de saúde devem estar estritamente entre 0 e 100!")
                    continue
            except ValueError:
                print("\n[Erro Entrada] As notas de saúde precisam ser números inteiros válidos!")
                continue
                
            nova_missao = input("Nome da Missão Espacial: ").strip()
            if not nova_missao:
                print("\n[Erro Entrada] O nome da missão não pode be em branco!")
                continue
            
            planeta_destino = escolher_viagem_menu()
            
            novo_registro = {
                "id": id_novo,
                "nome": nome_novo,
                "fisico": novo_fisico,
                "psicologico": novo_psicologico,
                "missao": nova_missao,
                "status": f"Em {planeta_destino}" 
            }
            
            cadastrar_novo_astronauta(astronautas, novo_registro)
            empilhar_log(f"Astronauta '{nome_novo}' (ID: {id_novo}) cadastrado com sucesso.")
            print(f"\n[Sucesso] '{nome_novo}' cadastrado com sucesso e alocado em {planeta_destino}!")
        
        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do astronauta: "))
            except ValueError:
                print("\n[Erro Entrada] O ID informado deve ser um número inteiro!")
                continue

            resultado_busca = buscar_astronauta_por_id(astronautas, id_busca)
            if resultado_busca:
                print(f"\nAstronauta Encontrado:")
                print(f" Nome: {resultado_busca['nome']}")
                print(f" Físico: {resultado_busca['fisico']:.1f}%")
                print(f" Psicológico: {resultado_busca['psicologico']:.1f}%")
                print(f" Status/Local Atual: {resultado_busca['status']}")
                print(f" Missão Corrente: {resultado_busca['missao']}")
            else:
                print("\n[!] Astronauta não localizado na base de dados.")
                
        elif opcao == "3":
            soma, quantidade = calcular_media_saude(astronautas)
            media = soma / quantidade if quantidade > 0 else 0
            print(f"\n[Análise] Média de prontidão dos ativos EM MISSÃO: {media:.2f}% (Total: {quantidade} astronautas fora da Terra)")
            
        elif opcao == "4":
            try:
                id_astronauta = int(input("Digite o ID do astronauta: "))
            except ValueError:
                print("\n[Erro Entrada] O ID informado deve ser um número inteiro!")
                continue

            nova_missao = input("Digite o nome da nova Missão: ").strip()
            if not nova_missao:
                print("\n[Erro Entrada] O campo de nova missão não pode ser vazio!")
                continue

            novo_planeta = escolher_viagem_menu()
            atualizar_missao_astronauta(id_astronauta, nova_missao, novo_planeta)
            
        elif opcao == "5":
            print("\n--- SIMULAÇÃO DE SAÚDE: RETORNO DE MISSÃO ---")
            try:
                id_analise = int(input("Digite o ID do astronauta que retornou: "))
                meses_no_espaco = int(input("Quantos meses durou a missão espacial? "))
                if meses_no_espaco < 0:
                    print("\n[Erro Entrada] A quantidade de meses não pode ser un valor negativo!")
                    continue
            except ValueError:
                print("\n[Erro Entrada] Ambas as entradas precisam ser números inteiros!")
                continue

            analisar_saude_pos_missao(id_analise, meses_no_espaco)
            
        elif opcao == "6":
            if not astronautas:
                print("\n[Aviso] Não há astronautas cadastrados no sistema até o momento.")
            else:
                print("\nAstronautas Cadastrados (Ordenados por ID):")
                for dados in astronautas:
                    print(f"ID: {dados['id']} | Nome: {dados['nome']} | Local: {dados['status']} | Missão: {dados['missao']} | Físico: {dados['fisico']:.1f}% | Psicológico: {dados['psicologico']:.1f}%")
                
        elif opcao == "7":
            exibir_pilha_logs()

        elif opcao == "0":
            print("\nEncerrando o ecossistema NeuroSpace. Até a próxima missão!")
            break
        else:
            print("\nOpção inválida! Selecione um número de 0 a 7.")


if __name__ == "__main__":
    menu()