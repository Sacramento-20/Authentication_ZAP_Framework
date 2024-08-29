import re

# Função para carregar regex de um arquivo
def carregar_regex(arquivo):
    with open(arquivo, 'r') as file:
        regex_list = [linha.strip() for linha in file.readlines()]
    return regex_list

# Função para encontrar correspondências
def encontrar_correspondencias(texto, regex_list):
    correspondencias = {}
    for regex in regex_list:
        correspondencias[regex] = re.findall(regex, texto, re.IGNORECASE)
    return correspondencias

# Carregar regex do arquivo
regex_list = carregar_regex('valid_elements.txt')

# Texto de teste
texto_teste = "sdalkfjlçaskdfjlkadfjsfdahkjh.css, nome-password_sadfjk, password-16546 txtPassword"

# Encontrar correspondências
correspondencias = encontrar_correspondencias(texto_teste, regex_list)

# Exibir resultados
for regex, matches in correspondencias.items():
    print(f"Matches for '{regex}': {matches}")
