# Solicita o texto para o usuario
n = input("Insira um texto: ")

l = 0 # Inicializa o contador de letras

# Verifica se é uma letra e conta quantas letras tem no texto
for char in n:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  
        l += 1

p = 1 # Inciializa o contador de palavras

# Conta o numero de palavras no texto
# Incrementa o contador pelo ' ' entre as palavras
for e in n:
   if ' ' == e:
      p += 1



s = 0 # Inicializa o contador de sentenças

# Incrementa o contador ao encontrar espaços ' '
for i in n:
   if i in ['!' , '.' , '?']:
      s += 1 


l = l / p * 100 # Calcula a media de letras por 100 palavras
s = s / p * 100 # Calcula a media de sentenças por 100 palavras

# Define o valor de index
index = round(0.0588 * l - 0.296 * s - 15.8)

if index > 16:
   print("Grade: +16") # Se  for mairo que 16 imprime Grade: +16
elif index < 1:
   print("Grade: Before 1")
else:
   print(f"Grade: {index}")

#0.0588 * L - 0.296 * S - 15.8, onde L é o número médio de letras p, 100 palavras no texto e S é o número médio de sentenças por 100 palavras no texto.