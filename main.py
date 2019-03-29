import csv

def q_1():
    arq = open('data.csv', encoding="utf8")
    linhas = csv.reader(arq)
    nacionalidades = list()
    for i in linhas:
        if not 'nationality' in i:
            if not i[14] in nacionalidades:
                nacionalidades.append(i[14])
    print("Total nacionalidades:", len(set(nacionalidades)))
    arq.close()
    
def q_2():
    arq = open('data.csv', encoding="utf8")
    linhas = csv.reader(arq)
    clubes = list()
    for i in linhas:
        if not 'club' in i:
            if not i[3] in clubes:
                clubes.append(i[3])
    print("Total clubes:", len(set(clubes)))
    arq.close()

def q_3():
    arq = open('data.csv', encoding="utf8")
    linhas = csv.reader(arq)

    cont = 0
    for i in linhas:
        if not 'full_name' in i:
            print("Nome jogador:", i[2])
            cont += 1
            if cont == 20:
                break
    arq.close()

def q_4():
    
    arq = open('data.csv', encoding="utf8")
    linhas = csv.reader(arq)
    ct = 0
    nome = list()
    valor = list()
    aux = list()
    aux2 = list()
    jogador = list()
    salario = list()

    for i in linhas:
        if not ('full_name' or 'eur_value') in i:
            nome.append(i[2]) 
            aux2.append(i[17]) 
            valor.append(float(i[17])) 

    aux = sorted(valor, reverse=True) 

    for i in range(len(aux2)): 
        for j in range(len(aux2)): 
            if str(aux[ct]) in aux2[j]: 
                if not nome[j] in jogador:
                    jogador.append(nome[j])
                    salario.append(aux[ct])
        ct += 1
        if ct == 10:
            break
    for i in range(10):
        print('Salario:',salario[i], 'Jogador:',jogador[i])
    arq.close()

def q_5():
    arq = open('data.csv', encoding="utf8")
    linhas = csv.reader(arq)
    aux = list()
    aux2 = list()
    age = list()
    idade = list()
    nome = list()
    jogador = list()
    ct = 0
    for i in linhas:
        if not 'age' in i:
            aux.append(int(i[6])) 
            aux2.append(i[6]) 
            nome.append(i[2]) 

    age = sorted(aux, reverse=True) 

    for i in range(len(aux2)):
        for j in range(len(aux2)):
            if str(age[ct]) in aux2[j]:
                if not nome[j] in jogador:
                    jogador.append(nome[j])
                    idade.append(age[ct])
        ct += 1
        if ct == 10:
            break
    for i in range(10):
        print('Idade:',idade[i], 'Nome:',jogador[i])

    arq.close()

def q_6():
    arq = open('data.csv', encoding="utf8")
    linhas = csv.reader(arq)
    age = list()
    aux = list()
    idade = 16
    ct = 0
    c = 16
    soma = 0
    lista_idades = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in linhas:
        if not 'age' in i:
            age.append(int(i[6]))

    for i in range(len(age)):
        for j in range(len(age)):
            if age[j] == idade:
                if ct <=31:
                    lista_idades[ct] = lista_idades[ct] + 1
        idade += 1
        ct += 1

    aux = sorted(age, reverse=True)

    for i in range(len(lista_idades)):
        print(c,'anos - ', lista_idades[i])        
        c+=1    
    arq.close()

q_1()
q_2()
q_3()
q_4()
q_5()
q_6()
