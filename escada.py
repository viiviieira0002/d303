# exercício da escada:
# O usuário deve escolher o material e o número de lances de escada
# Feito em python.
    
print ("Quantos lances de escada você gostaria?")
lances = int(input())

print ("Qual material deseja utilizar?")
material = input()
desenho = ""

i = 0

while i <= lances:
    print (desenho)
    desenho = desenho + material
    i = i + 1

