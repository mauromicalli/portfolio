# Um pequeno jogo em Python no estilo letreco.


# Importando biblioteca para colorir os textos
from colorama import Fore, Back, init

# Importando biblioteca para pegar palavra aleatória
import random


# Abrindo arquivo de dicionário de palavras com 5 letras
try:
    with open("5letras.txt", "r", encoding="utf-8") as arquivo:
        dicionario = {linha.strip() for linha in arquivo}
except FileNotFoundError:
    print("Erro: Arquivo de dicionário não encontrado, trabalhando com interno")
#Se não encontrou, utiliza dicionario interno
    dicionario = {"EDEMA","FOLHA","JANTA","BANCO","AMORA"}

# Escolhe uma palavra aleatória
palavra = random.choice(list(dicionario))

# Inicia variáveis
palavras_digitadas = []
letras_digitadas = []
teclado = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
# Cores
texto = Fore.BLACK
normal = Back.WHITE + texto
verde = Back.GREEN + texto
amarelo =  Back.YELLOW + texto
preto = Back.BLACK + texto
vermelho = Back.RED + texto

# Nos testes, descomentar a linha abaixo para mostrar a palavra sorteada
#mensagem = "Hint: " + palavra
mensagem = ""

# Tabela de cores, preenchida com valores padrão (preto)
cores = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]


# Funçao que desenha o tabuleiro do jogo
def desenha_tabela():
    print(amarelo+"FATECordle"+normal+"\n")
    for lin in range (6):
        print(normal +"+---+---+---+---+---+")
        linha = ""
        try:
            if (palavras_digitadas[lin]):
                for col in range(5):
                    linha += normal + "|"
                    if cores[lin][col] == 2:
                        linha += verde + " "+palavras_digitadas[lin][col]+" "
                    elif cores[lin][col] == 1:
                        linha += amarelo + " "+palavras_digitadas[lin][col]+" "
                    else:
                        linha += preto + " "+palavras_digitadas[lin][col]+" "
                linha += normal + "|"
        except:
        # Se a linha não tiver ainda palavra digitada, preenche a linha do tabuleir vazia
            linha += normal + "|   |   |   |   |   |"
        print(linha)
    print(normal + "+---+---+---+---+---+\n")


# Função que desenha o teclado
def desenha_teclado():
    linha = ""
    for letra in teclado:
        if letra in letras_digitadas and letra in palavra:
            linha += verde+"["+letra+"]"
        elif letra in letras_digitadas:
            linha += preto+"["+letra+"]"
        else:
            linha += normal+"["+letra+"]"
        # Se a letra for A ou L, começa em uma nova linha 
        if letra == "P":
            linha += normal+"\n "+normal
        if letra == "L":
            linha += normal+"\n  "
    print(linha+normal)


# Função que adiciona a palavra na lista de palavras digitadas, e atualiza a tabela de cores do tabuleiro
def adiciona_palavra(texto,lin):
    conta = {}
    # Conta quantas vezes cada letra aparece na palavra
    for letra in palavra:
        conta[letra] = conta.get(letra,0) + 1
    # Encontra as letras verdes (posição correta)
    for i in range(5):
        if (texto[i] == palavra[i]):
            cores[lin][i] = 2
            # Subtrai 1 do contador, para não pintar novamente uma letra já pintada
            conta[texto[i]] -= 1
    # Encontra as letras amarelas (posição errada)
    for i in range(5):
        if (cores[lin][i] != 2) and (texto[i] in palavra) and (conta[texto[i]] > 0):
            cores[lin][i] = 1
            conta[texto[i]] -= 1
    #Adiciona na lista de palavras digitadas
    palavras_digitadas.append(texto)


# Corpo principal do jogo, executa 6 vezes até preencher toda tabela, ou até acertar
while len(palavras_digitadas) < 6:
    print("\n" * 100)
    desenha_tabela()
    desenha_teclado()
    print(normal+mensagem)
    tentativa = input(normal+"Digite a palavra: ").upper()
# Aqui verifica se a palavra digitada é valida
    if (len(tentativa) == 5) and (tentativa not in palavras_digitadas) and (tentativa in dicionario):
        mensagem = ""
        # Adiciona na lista de palavras_digitadas
        adiciona_palavra(tentativa,len(palavras_digitadas))
        if tentativa == palavra:
            print("\n" * 100)
            desenha_tabela()
            print(amarelo+" *** GANHOU ****")
            break
        for letra in tentativa:
            if letra not in letras_digitadas:
                letras_digitadas.append(letra)
    else:
        mensagem = "Digite uma palavra válida, não repetida e de 5 letras"

# Chegou ao fim e não acertou. Desenha o tabuleiro preenchido, exibe mensagem
if tentativa != palavra:
    print("\n" * 100)
    desenha_tabela()
    print(verde + palavra)
    print(vermelho + " *** PERDEU *** \n"+ normal)