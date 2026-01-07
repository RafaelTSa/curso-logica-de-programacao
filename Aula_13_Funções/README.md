# 🐍 Aula 13: Funções em Python

Este diretório contém exemplos práticos sobre o uso de **Funções** em Python. O objetivo é demonstrar como modularizar o código, evitar repetições e organizar a lógica de programação em blocos reutilizáveis.

## 📂 Arquivos do Projeto

Abaixo está a descrição detalhada de cada script contido nesta aula:

### 1. `funcoes.py` (Introdução)
Este arquivo introduz o conceito básico de funções.
- **Conceito**: Define o que é uma função e por que utilizá-la (Princípio DRY - *Don't Repeat Yourself*).
- **Funcionalidade**:
  - Cria uma função chamada `saudacao(nome)`.
  - Recebe dados do usuário via `input`.
  - Imprime uma mensagem personalizada.


### 2. `media.py` (Múltiplos Parâmetros)
Demonstra como passar mais de um argumento para uma função.
- **Conceito**: Funções que aceitam múltiplos parâmetros para realizar um cálculo interno.
- **Funcionalidade**:
  - Define `calcular_media(n1, n2, n3)`.
  - Realiza a média aritmética de três números fixos.
  - Exibe o resultado formatado com duas casas decimais.


### 3. `retorno_valores.py` (Retorno de Dados)
Foca na captura de resultados processados pela função utilizando `return`.
- **Conceito**: Diferença entre apenas imprimir algo na tela e retornar um valor para ser usado posteriormente no código.
- **Funcionalidade**:
  - Implementa quatro funções matemáticas básicas: `somar`, `subtrair`, `multiplicar` e `dividir`.
  - Solicita dois números inteiros ao usuário.
  - Armazena o retorno de cada função em uma variável `resultado` antes de exibi-lo.


## 🚀 Como Executar

Certifique-se de ter o Python instalado. Navegue até a pasta `Aula_13_Funções` no seu terminal e execute os arquivos individualmente:

```bash
# Para testar a saudação básica
python funcoes.py

# Para testar o cálculo de média
python media.py

# Para testar as operações matemáticas com retorno
python retorno_valores.py
```

## 📝 Aprendizados Chave

- **Definição (`def`)**: Como declarar novas funções.
- **Parâmetros**: Como passar informações para dentro da função.
- **Retorno (`return`)**: Como extrair o resultado do processamento da função para variáveis externas.