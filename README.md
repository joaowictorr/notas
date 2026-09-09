# notas.py: Processador e Analisador de Notas de Alunos

Script em Python para coleta contínua de notas, validação de entradas, cálculo da média aritmética individual e acompanhamento do desempenho de alunos.

## Descrição

O script `notas.py` executa um loop contínuo que permite registrar o nome e três notas individuais de alunos. O programa inclui validações de segurança para impedir notas acima do limite permitido, determina o status de aprovação de cada estudante e calcula a média geral da turma de forma dinâmica.

## Funcionalidades e Regras de Negócio

* **Execução Contínua:** Permite registrar múltiplos alunos sem um limite fixo predeterminado.
* **Encerramento Manual:** O programa pode ser encerrado a qualquer momento digitando `exit` no campo do nome.
* **Validação de Entrada:** Impede o processamento de notas inválidas (superiores a 10.0).
* **Média de Aprovação:** Média igual ou superior a 7.0 (`APROVADO`).
* **Média de Reprovação:** Média inferior a 7.0 (`REPROVADO`).
* **Acumulador de Médias:** Calcula e acumula a soma das médias para análises gerais.
* **Formatação:** Exibe as médias com precisão de duas casas decimais.

## Requisitos

* Python 3.14

## Como Executar

1. Abra o terminal no diretório onde o arquivo está localizado.
2. Execute o comando:

```bash
python notas.py