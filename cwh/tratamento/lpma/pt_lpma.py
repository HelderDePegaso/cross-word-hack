def avaliar(combinacao, alta, media, baixa):
    # Verifica se os dois primeiros ou dois últimos são iguais, caso sim a combinação vai para o array de baixa prioridade
    if combinacao[0] == combinacao[1] or combinacao[-1] == combinacao[-2]:
        baixa.append(combinacao)
        return

    firstDif = 0;
    lastChar = ""
    isAlta = True
    
    for char in combinacao:
        if firstDif == 0:
            firstDif += 1
            lastChar = char
            continue

        if char != lastChar:
            firstDif += 1

        if char == lastChar:
            media.append(combinacao)
            isAlta = False
            return

        lastChar = char

    if isAlta:
        alta.append(combinacao)