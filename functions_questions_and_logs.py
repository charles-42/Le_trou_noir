import random
#appel d'une version colorée de print
from rich import print
score = 0
health = 50





# Dictionnaire principal pour notre jeu, contenant des listes pour les réponses
questions_dictionnary = {
    "Bonjour ?": {
        "propositions": ["Oui", "Non", "Peut-être", "Jaune"],
         "good_response": "Oui"
    },
    "À quoi était consacré ce temple ?": {
        "propositions": ["A toi", "A moi", "Aux autres", "A une divinité"],
        "good_response": "A toi"
    },
    "Quand a été construit ce temple ?": {
        "propositions": ["Il y à des millénaires", "Il y à quelques siècles", "Il y a des décennies", "Il vient d'être construit"],
        "good_response": "Il vient d'être construit"
    },
    "Qui était l'architecte ou le constructeur principal de ce temple ?": {
        "propositions": ["Un roi", "Un groupuscule", "Un architecte", "Un peuple indigène"],
        "good_response": "Un roi"
    }
}

# On définit les bonnes réponses aux questions dans un autre dictionnaire.
response_dictionnary = {
    "Bonjour ?": "Oui",
    "À quoi était consacré ce temple ?": "A toi",
    "Quand a été construit ce temple ?": "Il vient d'être construit",
    "Qui était l'architecte ou le constructeur principal de ce temple ?": "Un roi"
}

# Liste de mots pour la réussite du joueur
felicitations_quotes = ['[bold green]Bravo !', '[bold green]Excellent !', '[bold green]Quel génie !', '[bold green]Quel talent !',
                        "[bold green]C'est une prouesse incroyable, tu es un véritable érudit"]

# Un dictionnaire pour sauvegarder les réponses du joueur
save_player_answer = {}

# Définition des attributs du joueur
# score = 0
# health = 50

def question_launcher(question_key):
    """
    :param question_key: Take the keys from the dictionary questions.
    :type question_key: dict & str
    :return: The player's result.
    :rtype:
    """

    global score, health # Le statement `global`, permet d'appeler des variables déclarer hors de la fonction.

    question = questions_dictionnary[question_key]
    print(question_key)
    for i, propositions in enumerate(question["propositions"]):
        print(f"{i + 1}. {propositions}")
    user_answer = input("Entrez le chiffre associé à la proposition de votre choix : ")
    

    if question["propositions"][int(user_answer) - 1] == question["good_response"]:

        print(felicitations_quotes[random.randrange(0, 4)])
        score += random.randint(1, 5)
        print(f"[green]Votre score est de {score} et votre santé est de {health}")
           
    
    elif question["propositions"][int(user_answer) - 1] != question["good_response"]:

        print("[bold red]Ah! ah! ah!")
        health -= random.randint(4, 11)
        if health <= 0:
            print("*\------------------------------/*")
            print("[bold italic yellow on red blink]LOOOSER !!!")
            exit()
        print(f"[italic red]Votre score est de {score} et votre santé est de {health}")



    save_player_answer[question_key] = user_answer



def save_logs():
    """
    :return: Création d'un fichier qui va contenir toutes les actions du joueur.
    :rtype: file
    """

    with open("game_log.txt", "a") as fichier:
        fichier.write(f"Score: {score}\n")
        fichier.write(f"Santé: {health}\n")
        for question_key, answer in save_player_answer.items():
            fichier.write(f"{question_key}: {answer}")
            if questions_dictionnary[question_key]["good_response"] == questions_dictionnary[question_key]["propositions"][int(answer) - 1]:
                fichier.write(" (Bonne réponse)\n*\------------------------------/* \n")
            else:
                fichier.write(f" (Mauvaise réponse), la bonne réponse était :  {response_dictionnary.get(question_key)}\n*\------------------------------/* \n")
