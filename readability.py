# Solicita o texto para o usuario
n = input("Insira um texto: ")
l = 0

# Verifica se é uma letra e conta quantas letras
for char in n:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  
        l += 1

# Conta quantas palavra pelo ' ' entre as palavras
p = 1
for e in n:
   if ' ' == e:
      p += 1


# Conta quantas setenças, tem no texto a partir da pontuação
s = 0
for i in n:
   if i in ['!' , '.' , '?']:
      s += 1 


l = l / p * 100 # Divide as letras por 100 palavras
s = s / p * 100 # Divide as setenças por 100 palavras
print(f"Grade: {round(0.0588 * l - 0.296 * s - 15.8)}")

#0.0588 * L - 0.296 * S - 15.8, onde L é o número médio de letras p, 100 palavras no texto e S é o número médio de sentenças por 100 palavras no texto.