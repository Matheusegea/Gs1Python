# 🚀 NeuroSpace - Sistema de Triagem e Gerenciamento de Missões Espaciais

## 📋 Descrição

O **NeuroSpace** é um sistema desenvolvido em Python para gerenciamento de astronautas e missões espaciais. O projeto foi construído com foco na aplicação de estruturas de dados e algoritmos fundamentais, incluindo **Busca Binária**, **Recursão** e **Pilhas**, além de conceitos de análise de complexidade computacional (Big-O).

O sistema permite cadastrar astronautas, gerenciar missões, acompanhar indicadores de saúde física e psicológica, registrar auditorias por meio de logs e realizar análises pós-missão.

---

## 👨‍💻 Integrantes

| RM     | Nome                            |
| ------ | ------------------------------- |
| 563490 | Matheus Tozarelli Egea          |
| 565573 | Luara Martins de Oliveira Ramos |
| 563643 | Rafael Lorenzini Xavier         |
| 563082 | Felipe Ferrari Sumida           |

---

## 🎯 Objetivos do Projeto

* Gerenciar registros de astronautas.
* Manter os dados ordenados por ID desde o cadastro.
* Implementar busca eficiente utilizando Busca Binária.
* Utilizar Recursão para cálculos estatísticos.
* Aplicar Pilhas para auditoria e rastreamento de eventos.
* Simular impactos físicos e psicológicos causados por missões espaciais.

---

## ⚙️ Funcionalidades

### 1. Cadastro de Astronautas

* Registro de astronautas com:

  * ID único
  * Nome
  * Saúde física
  * Saúde psicológica
  * Missão atual
  * Destino espacial

### 2. Busca Binária por ID

* Localiza astronautas de forma eficiente.
* Não realiza ordenação durante a busca.
* A lista permanece ordenada desde o momento do cadastro.

### 3. Cálculo da Média de Saúde

* Utiliza Recursão.
* Considera apenas astronautas que estão em missão.
* Exclui astronautas que retornaram para a Terra.

### 4. Atualização de Missões

* Permite alterar a missão atual.
* Atualiza automaticamente o planeta de destino.

### 5. Análise Pós-Missão

* Simula desgaste físico e psicológico.
* Retorna astronautas para o status "Na Terra".
* Gera relatórios médicos automáticos.
* Emite alertas para estados críticos.

### 6. Listagem de Astronautas

* Exibe todos os registros ordenados por ID.

### 7. Sistema de Logs

* Implementado utilizando Pilha (LIFO).
* Registra:

  * Cadastros
  * Alterações de missão
  * Retornos de missões

---

## 🧠 Estruturas de Dados Utilizadas

### Busca Binária

Responsável pela localização eficiente de astronautas através do ID.

**Complexidade:**

* Melhor caso: O(1)
* Caso médio: O(log n)
* Pior caso: O(log n)

---

### Inserção Ordenada

Mantém a lista organizada sem necessidade de ordenação posterior.

**Complexidade:**

* Caso médio: O(n)
* Pior caso: O(n)

---

### Recursão

Utilizada para calcular a média de saúde dos astronautas ativos.

**Complexidade:**

* Caso médio: O(n)
* Pior caso: O(n)

---

### Pilha (Stack)

Utilizada para armazenar os logs de auditoria.

**Operação utilizada:**

* Push → append()

**Complexidade:**

* O(1)

---

## 🌎 Destinos Disponíveis

* Mercúrio
* Vênus
* Marte
* Júpiter
* Saturno
* Urano
* Netuno
* Plutão
* Sol
* Lua

---

## 📂 Estrutura do Sistema

```text
NeuroSpace
│
├── Cadastro de Astronautas
├── Busca Binária
├── Inserção Ordenada
├── Cálculo Recursivo de Saúde
├── Atualização de Missões
├── Simulação Pós-Missão
├── Pilha de Logs
└── Interface de Menu (CLI)
```

---

## ▶️ Como Executar

### Pré-requisitos

* Python 3.10 ou superior

### Execução

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Entre na pasta do projeto:

```bash
cd NeuroSpace
```

3. Execute o programa:

```bash
python main.py
```

---

## 📌 Menu Principal

```text
1. Cadastrar Novo Astronauta / Missão
2. Buscar Astronauta por ID
3. Calcular Média de Saúde
4. Atualizar Missão
5. Analisar Impacto Pós-Missão
6. Listar Astronautas
7. Exibir Pilha de Logs
0. Sair
```

---

## 📊 Exemplo de Uso

```text
ID: 101
Nome: João Silva
Saúde Física: 90
Saúde Psicológica: 85
Missão: Exploração Alpha
Destino: Marte
```

Resultado:

```text
[Sucesso] 'João Silva' cadastrado com sucesso e alocado em Marte!
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Programação Estruturada
* Busca Binária
* Recursão
* Pilhas (Stack)
* Análise de Complexidade (Big-O)

---

## 📖 Conceitos Acadêmicos Aplicados

* Estruturas de Dados
* Algoritmos de Busca
* Recursividade
* Pilhas
* Validação de Dados
* Simulação Computacional
* Complexidade Computacional

---

## 🚀 Conclusão

O NeuroSpace demonstra a aplicação prática de conceitos fundamentais de Ciência da Computação em um cenário de gerenciamento de missões espaciais. O projeto combina eficiência algorítmica, organização de dados e simulação de processos reais, proporcionando uma solução completa para controle e monitoramento de astronautas.
