def verificar_letra_a(texto):
    texto_minusculo = texto.lower()

    quantidade = texto_minusculo.count('a')

    if quantidade > 0:
        return f"A letra 'a' aparece {quantidade} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

texto = input("Digite uma string: ")
print(verificar_letra_a(texto))
