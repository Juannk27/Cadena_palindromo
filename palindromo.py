#Verificar si una cadena es un palindromo

def palindromo(word):

    # Limpia la palabra (quita espacios y convierte a minúsculas)
    cleaned_word = word.replace("","").lower()

    return cleaned_word == cleaned_word [::-1] 

user_input = input("Ingrese la palabra o la frase para poder dar el resultado: ")

if palindromo(user_input):
    print(f"{user_input} la palabra agregada si es un palindromo.")
else:
    print(f"{user_input} la palabra no es un palindromo.")