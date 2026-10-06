# File Hash Checker

Criei este script em Python para calcular o hash SHA-256 de arquivos locais de forma rápida e direta. 

A ideia nasceu da necessidade de validar a integridade de dados e garantir que um arquivo não sofreu nenhuma alteração ou corrupção no meio do caminho.

## O que o script faz

- Lê arquivos locais em blocos de bytes para otimizar o uso de memória.
- Gera o código SHA-256 correspondente de forma precisa.
- Trata automaticamente caminhos com espaços ou aspas (caso você arraste o arquivo para o terminal).

## Como testar por aí

Basta ter o Python instalado, colocar o script na sua máquina e rodar no terminal:

```bash
python hash_checker.py
