def modulo(termOne, termTwo):
    resultado = termOne - termTwo
    if resultado < 0:
        resultado *= -1
        return resultado
    return resultado


def distancia(termOne, termTwo):
    return termOne+termTwo


def Permutar(string):
    if len(string) == 1:
        return string
    lista = []
    for letra in string:
        string_aux = string.replace(letra, '')
        lista.extend([letra+string for string in Permutar(string_aux)])
    return lista

arquivo = open('matriz.txt', 'r')
pontos_entrega = []
circuitos = []
coordenadas = {}
contador = 0
for linha in arquivo:
    linha = linha.replace(" ","")
    if contador == 0:
        n = int(linha[0])
        m = int(linha[1])
    elif contador <= n:
        for i in linha:
            if i == 'R':
                coordenadas['R'] = (contador, linha.index(i)+1)
            elif i != '0' and i != '\n':
                pontos_entrega.append(i)
                coordenadas[f'{i}'] = (contador, linha.index(i) + 1)
    contador += 1
for i in Permutar(''.join(pontos_entrega)):
    circuitos.append(i)
arquivo.close()
contador = 0
tempo = 0
melhorTempo = 0
melhorCircuito = [[0 for _ in range(1)] for _ in range(1)]
while contador < len(circuitos):
    for i in circuitos[contador]:
        if circuitos[contador].index(i) == 0:
            xOne = coordenadas[f'R'][0]
            xTwo = coordenadas[f'{i}'][0]
            yOne = coordenadas['R'][1]
            yTwo = coordenadas[f'{i}'][1]
            tempo += distancia(modulo(xTwo, xOne), modulo(yTwo, yOne))
            entregaAtual = i

        elif circuitos[contador].index(i) < len(circuitos[contador]) - 1:
            xOne = coordenadas[f'{entregaAtual}'][0]
            xTwo = coordenadas[f'{i}'][0]
            yOne = coordenadas[f'{entregaAtual}'][1]
            yTwo = coordenadas[f'{i}'][1]
            tempo += distancia(modulo(xTwo, xOne ),modulo(yTwo, yOne))
            entregaAtual = i
        else:
            xOne = coordenadas[f'{entregaAtual}'][0]
            xTwo = coordenadas[f'{i}'][0]
            yOne = coordenadas[f'{entregaAtual}'][1]
            yTwo = coordenadas[f'{i}'][1]
            tempo += distancia(modulo(xTwo, xOne), modulo(yTwo, yOne))
            xOne = coordenadas[f'{i}'][0]
            xTwo = coordenadas['R'][0]
            yOne = coordenadas[f'{i}'][1]
            yTwo = coordenadas['R'][1]
            tempo += distancia(modulo(xTwo, xOne), modulo(yTwo, yOne))
            if contador == 0:
                melhorTempo = tempo
                melhorCircuito[0] = circuitos[contador]
            elif tempo < melhorTempo:
                melhorTempo = tempo
                melhorCircuito[0] = circuitos[contador]
    tempo = 0
    contador += 1
print("O melhor circuito para fazer as entregas é: " + ' '.join(melhorCircuito[0]))

