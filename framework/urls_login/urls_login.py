def find_urls_login(lista_strings, lista_palavras):
    # Lista para armazenar as strings que contêm alguma das palavras
    urls_encontradas = []

    # Itera sobre cada string na lista de strings
    for string in lista_strings:
        # Itera sobre cada palavra na lista de palavras
        for palavra in lista_palavras:
            # Verifica se a palavra está presente na string
            if palavra in string:
                # Adiciona a string à lista de resultados e sai do loop interno
                urls_encontradas.append(string)
                break

    return urls_encontradas
