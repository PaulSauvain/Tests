############ Question 1 : Code ######(5 min)######
def process_string(var1):
    if var1.isalpha():  # check if it's a word
        if len(var1) > 2:  # check if number of char is bigger than 2
            return var1[0] + str(len(var1) - 2) + var1[-1:]  # first letter + number of char minus 2 + last char
        else:
            return var1
    else:
        return 'Error : This is not a Word'

print(process_string(input()))

############ Question 2 : Cas des tests ######(5 min)######
# - Révision de la consigne afin de définir avec plus de précision les cas limites (mot avec tiret inclus ? Plusieurs mots ? Contraction ? Taille min ? Taille max ?)
# - Mots contenant des caractères.
# - Mots contenant des chiffres.
# - Chiffre uniquement.
# - Caractères spéciaux uniquement.
# - Test à vide.
# - Test de performance (JDD avec mot très long)


