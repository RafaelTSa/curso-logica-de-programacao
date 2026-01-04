# Simulador de Caixa Eletrônico 🏧

Este projeto simula as operações básicas de saque em um caixa eletrônico. O objetivo é praticar estruturas de repetição com condições de parada e validações lógicas.

## 📝 Sobre o Projeto

O programa inicia com um saldo fixo e permite que o usuário realize saques consecutivos. O sistema valida se há saldo suficiente para cada operação e atualiza o valor disponível em tempo real.

## 🚀 Funcionalidades

- **Controle de Saldo**: Impede saques maiores que o valor disponível.
- **Loop Condicional**: O programa roda enquanto houver saldo ou até o usuário encerrar.
- **Saída Voluntária**: Opção de digitar `0` para sair do sistema a qualquer momento.
- **Formatação Monetária**: Exibição do saldo com duas casas decimais.

## 🛠️ Tecnologias e Conceitos

- **Linguagem**: Python
- **Estruturas**: `while`, `if`, `else`, `break`
- **Operadores**: Comparação e subtração com atribuição (`-=`)

## ▶️ Como Executar

Certifique-se de ter o Python instalado. No terminal, execute:

```bash
python CaixaEletronico.py
```