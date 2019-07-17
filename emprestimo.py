#  Criar um programa que avalia uma proposta de empréstimo.
# //    O programa recebe: idade do cliente, quanto dinheiro ele quer emprestar, quanto ele ganha por mês.

# //    REGRAS para aceita o empréstimo:
# //    - Entre 22 e 55 anos;
# //    - Valor a partir de 1000 reais;
# //    - Valor não pode ultrapassar 15x o que ele recebe

# //    RESPONDER: ACEITO OU NÃO ACEITO

# //    EXTRA:
# //    - Perguntar também a quantidade de parcelas (3 a 20 vezes) e calcular juros de 8% ao mês (COMPOSTO)
# //    RESPONDER VALOR TOTAL DO EMPRESTIMO E VALOR Da PARCELA.
IDADE = int (input ("Idade?\n"))
VALOREMPRESTIMO = int (input ("Valor que deseja?\n"))
SALARIO = int( input("O seu salário?\n"))
QTDPARCELAS = int( input ("quantas parcelas?\n"))
def emprestimo (IDADE , VALOREMPRESTIMO , SALARIO , QTDPARCELAS):
    if IDADE < 22 or IDADE > 55 or VALOREMPRESTIMO < 1000 or VALOREMPRESTIMO > SALARIO * 15 or QTDPARCELAS < 3 or QTDPARCELAS > 20:
        print ('Não aceito')
    
  
    else:
        print('Aceito')
        MONTANTE = VALOREMPRESTIMO * (1 + 0.08) ** QTDPARCELAS;
        MONTANTE = MONTANTE.toFixed(2)
        PARCELA = MONTANTE/QTDPARCELAS
        PARCELA = PARCELA.toFixed(2)
        print(f"O valor total do empréstimo é de {montante} e o valor da parcela é de {parcela}")
emprestimo(IDADE, VALOREMPRESTIMO, SALARIO, QTDPARCELAS) 