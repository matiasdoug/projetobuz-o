#função para criar uma matriz
def matriz(lin, col, valor):
    matriz = []
    
    for i in range(lin):
        linha = []
        
        for j in range(col):            
            linha.append(valor)
            
        matriz.append(linha)
        
    return matriz
        
#atribuição da matriz para a variável
a = matriz(8,5,0)

#print da matriz com os assentos
for i in a:
    print(i)
    
#variável de controle do while
v = 0


#loop que simula 5 vendas
while v < 5:
    
    #adiciona 1 para variável de controle
    #para registar os loop executados
    v = v+1
    
    #input do usuário para escolha de linha e coluna do assento
    l = int(input("Escolha sua linha de 0 a 7:\n"))
    c = int(input("Escolha sua coluna de 0 a 4:\n"))
    
    #condição para barrar a compra na frente 
    if l == 0:
        print("Frente do onibus indisponível")   
    #condição para barrar a compra no corredor 
    elif c == 2:
        print("Você não pode sentar no corredor!")
    #condição de assento inválido    
    elif l > 7:
        print("Linha inválida!")
    elif c > 4:
        print("Coluna inválida!")
    #condição para verificar se esta disponível     
    elif a[l][c] == 0:
        print("Assento reservado, obrigado pela compra!")
        #caso esteja marcar 1 para deixar indisponível
        a[l][c] = 1
    #caso o assento esteja reservado     
    else:
        print("Assento indisponível!")

with open('assento.txt', 'a') as arquivo:
    for i in a:
        print(i, file=arquivo)
        



                


    





