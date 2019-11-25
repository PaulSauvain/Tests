############ Question 1 : fonction ######(15 min)######
from datetime import datetime

def hasNextCount():
    return True

def getNextCount():
     return ("12/10/19",1332)

def getWeekDayFromDate(var):
    return 6

def analyseLog(startdate,enddate):
    data = [0] * 7
    startdate = datetime.strptime(startdate, "%d/%m/%y")
    enddate = datetime.strptime(enddate, "%d/%m/%y")
    if startdate < enddate:
        while hasNextCount():
            (date, nbvisit) = getNextCount()
            date2 = datetime.strptime(date, "%d/%m/%y")
            if date2 >= startdate and date2 <= enddate:
                data[getWeekDayFromDate(date)] = data[getWeekDayFromDate(date)] + nbvisit
        return data.index(min(data))
    else:
        return "Error"

print(analyseLog("10/10/19","16/10/19"))


############ Question 2 : Cas des tests ######(5 min)######
# - Vérifier les formats de dates et cohérence
# - Vérifier les données du log (ex avec isdigit)
# - Vérifier les 3 fonctions données
# - Test à vide.
# - Test de performance (JDD avec mot très long)

############ Question 3 : Modification######(5 min)######
# - Non nécessité de la fonction getWeekDayFromDate
# - Stockage des données dans deux listes. Dans la première liste je stock la date au même indice que pour la deuxième liste qui elle contient le nombre de visiteurs.
# Exemple :
# date_list=["10/11/19","11/11/19","12/11/19","13/11/19","14/11/19","15/11/19","16/11/19","17/11/19"]
# nb_list= ["1","9","10","11","12","13","11","15"]
# For de K de 1 à K:
    # Je récupère la date en faisant une liaison d'index : date_list(nb_list.index(max(nb_list)))
    # Je remove les 2 entrées de l'indice dans les deux listes : del date_list(index)
# Réfléchir au doublon avec une recherche de valeur de visite identique.