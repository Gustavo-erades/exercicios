# Flávio Siqueira | 22302701
print("\tNome: Flávio Siqueira \n\tRA: 22302701\n")
# Exercícios de Estruturas Condicionais/Decisão
# Fácil
#1
def par_ou_impar():
    num=int(input("Digite um número: "))
    if(num%2!=0):
        print("%d é um número Ímpar!"%(num))
    else:
        print("%d é um número Par!"%(num))
#2
def sinal_do_numero():
    num=int(input("Digite um número: "))
    if(num>0):
        print("%d é um número positivo"%(num))
    elif (num<0):
        print("%d é um número negativo!"%(num))
    else:
        print("O número digitado é zero!")
#3
def maior_de_idade():
    idade=int(input("Qual sua idade? "))
    if(idade>=18):
        print("Você é maior de idade! :)")
    else:
        print("Você é menor de idade! :(")
#4
def vogal_ou_consoante():
    vogais=("a","e","i","o","u")
    letra=input("Digite uma letra: ")
    if letra.isnumeric() :
        print("'%s' não é uma letra"%(letra))
    elif letra in vogais:
        print("A letra '%s' é uma vogal!"%(letra))
    elif not letra in vogais:
        print("A letra '%s' é uma consoante!"%(letra))
#5
def multiplo_de_cinco():
    num=int(input("Digite um número: "))
    if(num%5==0):
        print("O número %d é múltiplo de 5"%(num))
    else:
        print("O número %d Não é múltiplo de 5"%(num))
# Médio
#6
def maior_numero():
    num1=int(input("Digite um número: "))
    num2=int(input("Digite outro número: "))
    num3=int(input("Digite mais um número: "))
    lista=(num1,num2,num3)
    print("O maior número dentre os números digitados é: %d"%(max(lista)))
#7
def pode_votar():
    idade=int(input("Digite sua idade: "))
    if(idade==16 or idade==17):
        print("Você pode votar. Porém não é obrigado por Lei.")
    elif(18<=idade<=65):
        print("Você é obrigado a votar por lei!")
    elif(idade>65):
        print("O senhor(a) não é mais obrigado(a) a ir votar por lei.")
    else:
        print("Você ainda não pode votar.")
#8
def classificar_aluno():
    nota=int(input("Informe sua nota: "))
    if(90<=nota<=100):
        print("Você é um aluno nota 'A'.")
    elif(80<=nota<=89):
        print("Você é um aluno nota 'B'.")
    elif(70<=nota<=79):
        print("Você é um aluno nota 'C'.")
    elif(60<=nota<=69):
        print("Você é um aluno nota 'D'.")
    else:
        print("Você é um aluno nota 'F'.")
#9
def aberto_ou_fechado():
    print("****************************************")
    print("* A loja abre às 08:00 e fecha às 18:00*")
    print("* Informe um horário no formato 00:00 *")
    print("****************************************")
    horario=input("Informe um horário (exemplo: 10:30): ").split(":")
    cont=0
    for i in horario:
      cont+=1
    if(cont>2):  
        if('-1'<horario[0]<'24' and '0'<=horario[1]<='59'):
            if('08'<=horario[0]<'18'):
                print("A loja está aberta!")
            else:
                print("A loja está fechada!")
        else:
            print("Informe um horário válido!")
            aberto_ou_fechado()
    else:
        horario.append("00")
        if('-1'<horario[0]<'24' and '0'<=horario[1]<='59'):
            if('08'<=horario[0]<'18'):
                print("A loja está aberta!")
            else:
                print("A loja está fechada!")
        else:
            print("Informe um horário válido!")
            aberto_ou_fechado()
#10
def categoria():
    idade=int(input("Informe sua idade: "))
    if(idade>=5):
        if(5<=idade<=7):
            print("Nadador(a), sua categoria é Infantil.") 
        elif(8<=idade<=10):
            print("Nadador(a), sua categoria é Juvenil.")
        elif(11<=idade<=17):
            print("Nadador(a), sua categoria é Adolescente.")
        elif(idade>=18):
            print("Nadador(a), sua categoria é Adulto.")
    else:
        print("Você é muito jovem, nadador(a). ")
# Difícil
#11
def preco_cinema():
    idade=int(input("Informe sua idade: "))
    if(idade<12):
        print("O ingresso custará 10$")
    elif(12<=idade<=65):
        print("O ingresso custará 15$")
    else:
        print("O ingresso custará 12$")
#12
def classifica_angulo():
    angulo=int(input("Informe o ângulo: "))
    if(angulo<90):
        print("O ângulo %d é classificado como Agudo."%(angulo))
    elif(angulo==90):
        print("O ângulo %d é classificado como Reto."%(angulo))
    elif(angulo>90):
        print("O ângulo %d é classificado como Obtuso."%(angulo))
#13
def calcula_imc():
    peso=float(input("Informe seu peso (kg): "))
    altura=float(input("Informe sua altura (metros): "))
    imc=peso/(altura**2)
    if(imc<18.5):
        print(f"Seu imc é de {imc:.2f}, por tanto você está Abaixo do peso")
    elif(18.5<=imc<=24.9):
        print(f"Seu imc é de {imc:.2f}, por tanto você está no peso Normal")
    elif(25<=imc<=29.9):
        print(f"Seu imc é de {imc:.2f}, por tanto você está em Sobrepeso")
    else:
        print(f"Seu imc é de {imc:.2f}, por tanto você está Obeso(a)")
#14
def ano_bissexto():
    ano=int(input("Informe o ano: "))
    if(ano%4==0):
        print("O ano de %d é bissexto."%(ano))
    else:
        print("O ano de %d não é bissexto."%(ano))
#15
def definir_estacao():
    meses=('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
    resp_user=input("Informe o mês: ")
    if resp_user.isnumeric():
        if(resp_user=='12' or resp_user=='1' or resp_user=='2' ):
            print("A estação do ano é Verão")
        elif(resp_user=='3' or resp_user=='4' or resp_user=='5' ):
            print("A estação do ano é Outono")
        elif(resp_user=='6' or resp_user=='7' or resp_user=='8' ):
            print("A estação do ano é Inverno")
        elif(resp_user=='9' or resp_user=='10' or resp_user=='11' ):
            print("A estação do ano é Primavera")
    else:
        if((resp_user==meses[11] or resp_user=='Dezembro') or (resp_user==meses[0] or resp_user=='Janeiro') or (resp_user==meses[1] or resp_user=='Fevereiro') ):
            print("A estação do ano é Verão")
        elif((resp_user==meses[2] or resp_user=='Março') or (resp_user==meses[3] or resp_user=='Abril') or (resp_user==meses[4] or resp_user=='Maio') ):
            print("A estação do ano é Outono")
        elif((resp_user==meses[5] or resp_user=='Junho') or (resp_user==meses[6] or resp_user=='Julho') or (resp_user==meses[7] or resp_user=='Agosto') ):
            print("A estação do ano é Inverno")
        elif((resp_user==meses[8] or resp_user=='Setembro') or (resp_user==meses[9] or resp_user=='Outubro') or (resp_user==meses[10] or resp_user=='Novembro') ):
            print("A estação do ano é Primavera")
# Exercícios de Estruturas de Repetição
# Fácil
#16
def imprimir_numeros():
    for i in range(1,11,1):
        print(i,end=" ")
#17
def calcular_soma():
    soma=[]
    N=int(input("Infome a quantidade de números a ser somados: "))
    for i in range(1,N+1,1):
        soma.append(i)
    print("A soma dos %d primeiros números é: %d"%(N,sum(soma)))
#18
def num_primo():
    listaDivisores=[]
    num=int(input("Digite um número: "))
    for i in range(1,num+1,1):
        if num%i==0:
            listaDivisores.append(i)
    if len(listaDivisores)==2:
        print("%d é um número primo."%(num))
    else:
        print("%d não é um número primo."%(num))
#19
def fatorial():
    num=int(input("Informe um número: "))
    fatorial=1
    if(num==0):
        fatorial=1
    else:
        for i in range(1,num+1,1):
            fatorial=i*fatorial
    print("O fatorial de %d equivale a %d"%(num,fatorial))
#20
def fibonacci():
    num=int(input("Informe um número: "))
    num1=1
    num2=1
    lista=[]
    if num==1:
        fibo=1
        print("Fibonacci: %d"%(num1),end=" ") 
    elif num==2:
        fibo=1
        print("Fibonacci: %d %d"%(num1,num2),end=" ") 
    else:
        print("%d %d"%(num1,num2),end=" ")
        for i in range(2,num):
            fibo = num1 + num2
            num2 = num1
            num1 = fibo
            i += 1
            lista.append(fibo)
            print(fibo,end=" ")
# Médio 
#21
def num_par():
    N=int(input("Informe um número: "))
    print("Números pares até %d:"%(N), end="")
    for i in range(1,N+1):
        if i%2==0:
            print(" %d"%(i), end="")
#22
def soma_impar():
    lista=[]
    intervalo=int(input("Informe um número: "))
    print("Soma dos números ímpares até %d:"%(intervalo), end="")
    for i in range(1,intervalo+1):
        if i%2!=0:
            lista.append(i)
    print(f" {sum(lista)}",end="")
#23
def divisores():
    lista=[]
    N=int(input("Informe um número: "))
    for i in range(1,N+1,1):
        if N%i==0:
            lista.append(i)
    print(f"O  número de divisores de {N} é {len(lista)} ")
#24
def maior_num():
    lista=[]
    numeros=input("Informe os números da lista (separados por um espaço): ").split()
    for i in numeros:
        num=int(i)
        lista.append(num)
    print(f"O maior valor presente na lista é {max(lista)}")
#25
def verificar_existencia():
    lista=[]
    numeros=input("Informe os números da lista (separados por um espaço): ").split()
    for i in numeros:
        num=int(i)
        lista.append(num)
    procura_num=int(input("Informe o número que deve ser pesquisado: "))
    if procura_num in lista:
        print(f"O número {procura_num} existe na lista!")
    else:
        print(f"O número {procura_num} não existe na lista!")
# Difícil
#26 
def primos_ate_limite():
    listaPrimos = []
    N = int(input("Digite o valor de N: "))
    for num in range(2, N+1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            listaPrimos.append(num)
    print(f"Os Números primos até {N} são: ",end="")
    for j in listaPrimos:
        print(j,end=" ")
#27
def maior_menor():
    lista=[]
    numeros=input("Informe os números da lista (separados por um espaço): ").split()
    for i in numeros:
        num=int(i)
        lista.append(num)
    print(f"O maior valor presente na lista é :{max(lista)}")
    print(f"O menor valor presente na lista é :{min(lista)}")
#28
def media_lista():
    lista=[]
    numeros=input("Informe os números da lista (separados por um espaço): ").split()
    for i in numeros:
        num=int(i)
        lista.append(num)
    media=float(sum(lista)/len(lista))
    print(f"A média da lista digitada é de: {media:.2f}")
#29
def quant_maior():
    lista=[]
    numeros=input("Informe os números da lista (separados por um espaço): ").split()
    for i in numeros:
        num=int(i)
        lista.append(num)
    num=int(input("Informe o número base: "))
    cont=0
    for i in lista:
        if i>num:
            cont+=1
    print("Há %d números maiores que %d na lista"%(cont,num))
#30
def verifica_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
def mostra_primos_em_faixa():
    listaPrimos= []
    comeco=int(input("Informe o número base da faixa: "))
    fim=int(input("Informe o número limite da faixa: "))
    for num in range(comeco, fim+1,1):
        if verifica_primo(num):
            listaPrimos.append(num)
    print("Os números primos entre", comeco, "e", fim, "são: ",end="")
    for num_primo in listaPrimos:
        print(num_primo,end=" ")
# Exercícios de Vetores (listas)
#31
# Fácil
def soma_vetor():
    vetor=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço): ").split()
    for i in valores_vetor:
        nums=int(i)
        vetor.append(nums)
    soma=sum(vetor)
    print(f"A soma de todos os elementos do vetor equivale a: {soma}")
#32
def menor_maior_vetor():
    vetor=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço): ").split()
    for i in valores_vetor:
        nums=int(i)
        vetor.append(nums)
    maior=max(vetor)
    menor=min(vetor)
    print(f"O maior elemento presente nesse vetor é {maior} e o menor é {menor}")
#33
def verificar_elemento_vetor():
    vetor=[]
    valores_vetor=input("Informe os elementos que devem preencher o vetor (separados por um espaço): ").split()
    for i in valores_vetor:
        elementos=i
        vetor.append(elementos)
    pesquisar=input("Indique o elemento que deve ser procurado no vetor: ")
    if pesquisar in vetor:
        print(f"O elemento '{pesquisar}' existe no vetor!")
    else:
        print(f"O elemento '{pesquisar}' não existe no vetor!")
#34
def contar_ocorrencias_vetor():
    vetor=[]
    valores_vetor=input("Informe os elementos que devem preencher o vetor (separados por um espaço): ").split()
    for i in valores_vetor:
        elementos=i
        vetor.append(elementos)
    pesquisar=input("Indique o elemento que deve ser procurado no vetor: ")
    if pesquisar in vetor:
        ocorrencias=vetor.count(pesquisar)
        if ocorrencias>1:
            print(f"O elemento '{pesquisar}' aparece {ocorrencias} vezes no vetor!")
        else:
            print(f"O elemento '{pesquisar}' aparece {ocorrencias} vez no vetor!")
    else:
        print(f"O elemento '{pesquisar}' não existe no vetor!")
#35
def somar_posicoes_pares():
    vetor=[]
    posicoes_pares=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço): ").split()
    for i in valores_vetor:
        numeros=int(i)
        vetor.append(numeros)
    num_par=0
    while num_par<=len(vetor):
        posicoes_pares.append(vetor[num_par])
        num_par+=2
    print(f"A soma dos elementos em posições pares do vetor é de {sum(posicoes_pares)}")
# Médio 
#36
def produto_escalar():
    vetor1=[]
    valores_vetor1=input("Informe os números que devem preencher o primeiro vetor (separados por um espaço):\n").split()
    for i in valores_vetor1:
        numeros_vetor1=int(i)
        vetor1.append(numeros_vetor1)
    vetor2=[]
    valores_vetor2=input("Informe os números que devem preencher o segundo vetor (separados por um espaço):\n").split()
    for i in valores_vetor2:
        numeros_vetor2=int(i)
        vetor2.append(numeros_vetor2)
    if len(vetor1)==len(vetor2):
        cont=0
        calculo=0
        while cont<=(len(vetor1)-1):
            calculo=(vetor1[cont]*vetor2[cont])+calculo
            cont+=1
    print(f"O produto escalar entre os vetores é de: {calculo}")
#37
def inverter_ordem():
    vetor=[]
    valores_vetor=input("Informe os elementos que devem preencher o vetor (separados por um espaço):\n").split()
    for i in valores_vetor:
        elementos_vetor=i
        vetor.append(elementos_vetor)
    vetor.reverse()
    print(f"Vetor na ordem invertida: {vetor}")       
#38
def contar_positivos():
    vetor=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço):\n").split()
    for i in valores_vetor:
        numeros_vetor=int(i)
        vetor.append(numeros_vetor)
    positivo=0
    for j in vetor:
        if j>=0:
            positivo+=1
    if positivo>1:
        print("Há %d números positivos no vetor."%(positivo))
    elif positivo==1:
        print("Há %d número positivo no vetor."%(positivo))
    else:
         print("Não há números positivos no vetor.")
#39
def ordem_crescente():
    vetor=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço):\n").split()
    for i in valores_vetor:
        numeros_vetor=int(i)
        vetor.append(numeros_vetor)
    crescente=0
    if(len(vetor)>1):
        for i in range(1,len(vetor)):
            if vetor[i-1]<vetor[i]:
                crescente+=1
        if crescente==(len(vetor)-1):
            print("A lista está em ordem crescente")
        else:
            print("A lista não está em ordem crescente")
    else:
        print("Só há um elemento na lista!")
#40
def soma_2vetores():
    vetor1=[]
    valores_vetor1=input("Informe os números que devem preencher o primeiro vetor (separados por um espaço):\n").split()
    for i in valores_vetor1:
        numeros_vetor1=int(i)
        vetor1.append(numeros_vetor1)
    vetor2=[]
    valores_vetor2=input("Informe os números que devem preencher o segundo vetor (separados por um espaço):\n").split()
    for i in valores_vetor2:
        numeros_vetor2=int(i)
        vetor2.append(numeros_vetor2)
    soma_tudo=(sum(vetor1))+(sum(vetor2))
    print(f"A soma dos elementos dos dois vetores equivale a: {soma_tudo}")
# Difícil
#41
def vetores_iguais():
    vetor1=[]
    valores_vetor1=input("Informe os números que devem preencher o primeiro vetor (separados por um espaço):\n").split()
    for i in valores_vetor1:
        numeros_vetor1=int(i)
        vetor1.append(numeros_vetor1)
    vetor2=[]
    valores_vetor2=input("Informe os números que devem preencher o segundo vetor (separados por um espaço):\n").split()
    for i in valores_vetor2:
        numeros_vetor2=int(i)
        vetor2.append(numeros_vetor2)
    if vetor1 == vetor2:
        print("Os vetores são iguais!")
    else:
        print("Os vetores não são iguais!")
#42
def ordem_decrescente():
    vetor=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço):\n").split()
    for i in valores_vetor:
        numeros_vetor=int(i)
        vetor.append(numeros_vetor)
    decrescente=0
    if(len(vetor)>1):
        for i in range(1,len(vetor)):
            if vetor[i-1]>vetor[i]:
                decrescente+=1
        if decrescente==(len(vetor)-1):
            print("A lista está em ordem decrescente")
        else:
            print("A lista não está em ordem decrescente")
    else:
        print("Só há um elemento na lista!")
#43
def rotacionar_direita():
    vetor=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço):\n").split()
    for i in valores_vetor:
        elementos_vetor=int(i)
        vetor.append(elementos_vetor)
    num_rep=int(input("Informe quantos deslocamentos para a direita devem ser feitos: "))
    if num_rep>0:
        quant_elementos=(len(vetor))
        num_rep=num_rep%quant_elementos
        vetor_direita=vetor.copy()
        for i in range(quant_elementos):
            vetor_direita[(i+num_rep)%quant_elementos]=vetor[i]
        if num_rep>1:
            print(f"O vetor após {num_rep} repetições ficou assim: {vetor_direita}")
        else:
            print(f"O vetor após {num_rep} repetição ficou assim: {vetor_direita}")
    else:
        print("Informe um número de repetições válido!")
        rotacionar_direita()
#44
def achar_posição():
    vetor=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço):\n").split()
    for i in valores_vetor:
        elementos_vetor=i
        vetor.append(elementos_vetor)
    procura_por=input("Informe o elemento que deve ser procurado na lista: ")
    if procura_por in vetor:
        posicao=vetor.index(procura_por)
        print(f"O elemento '{procura_por}' está  na posição {posicao} da lista.")
    else:
        print("Não existe esse elemento na lista!")
#45
def somar_posicoes_impares():
    vetor=[]
    posicoes_impares=[]
    valores_vetor=input("Informe os números que devem preencher o vetor (separados por um espaço): ").split()
    for i in valores_vetor:
        numeros=int(i)
        vetor.append(numeros)
    num_impar=1
    while num_impar<=(len(vetor)-1):
        if(num_impar%2!=0):
            posicoes_impares.append(vetor[num_impar])
        num_impar+=1
    print(f"A soma dos elementos em posições impares do vetor é de {sum(posicoes_impares)}")
# Exercícios de Técnicas de Modularização
# Fácil
#46
def soma_2numeros(num1,num2):
   soma=int(num1)+int(num2)
   return soma 
#47
def produto_2numeros(num1,num2)->float:
   produto=float(num1)*float(num2)
   return produto
#48
def quadrado(num):
    return num**2
#49
def cubo(num):
    return num**3
#50
def raiz_quadrada(num):
    return num**(1/2)
# Médio
#51
def retorna_media(lista):
    media=float(sum(lista)/len(lista))
    return media
#52
def soma_valores_impares(lista):
    soma=0
    for i in lista:
        if i%2!=0:
            soma=soma+i
    return soma
#53
def soma_valores_pares(lista):
    soma=0
    for i in lista:
        if i%2==0:
            soma=soma+i
    return soma
#54
def retorna_maior_num(lista):
    return max(lista)
#55
def retorna_menor_num(lista):
    return min(lista)
# Difícil
#56
def soma_primos(numbers):
    soma_primo = 0
    for num in numbers:
        if verifica_primo(num):
            soma_primo += num
    return soma_primo
#57
def retorna_produto(lista):
    produto=1
    for i in lista:
        produto=produto*i
    return produto
#58
def retorna_soma_quadrados(lista):
    soma_quadrado=0
    for i in lista:
        soma_quadrado= quadrado(i)+ soma_quadrado   
    return soma_quadrado
#59
def retorna_soma_quadrados(lista):
    soma_quadrado=0
    for i in lista:
        soma_quadrado= cubo(i)+ soma_quadrado   
    return soma_quadrado
#60
def retorna_media_quadrados(lista):
    listaQuadrados=[]
    for i in lista:
        listaQuadrados.append(quadrado(i))
    return retorna_media(listaQuadrados)      