# notas.py: Processador de Notas de Alunos

Script em Python para coleta de notas, cálculo de média aritmética e verificação de aprovação de alunos em lote.

## Descrição

O script `notas.py` executa um loop iterativo para registrar o nome e três notas individuais de até 100 alunos. Com base nas notas fornecidas, o programa calcula a média de cada estudante e exibe imediatamente o resultado final de aprovação.

## Regras de Negócio

* **Média de Aprovação:** Média igual ou superior a 7.0 (APROVADO).
* **Média de Reprovação:** Média inferior a 7.0 (REPROVADO).
* **Formatação:** A média final é exibida com arredondamento de duas casas decimais.

## Requisitos

* Python 3.x

## Como Executar

1. Abra o terminal no diretório onde o arquivo está localizado.
2. Execute o comando:

```bash
python notas.py