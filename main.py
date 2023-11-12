import turtle

def poser_questions():
    reponses = []  # Déclaration de la liste pour stocker les réponses

    questions = [
        "Question 1 : ",
        "Question 2 : ",
        "Question 3 : ",
        "Question 4 : ",
        "Question 5 : ",
        "Question 6 : "
    ]
    
    for question in questions:
        while True:
            try:
                #Donner les conditions
                print("Veuillez entrer un chiffre entre 1 et 200.")
                reponse = int(input(question + " "))
                if 1 <= reponse <= 200:
                    reponses.append(reponse)
                    break  # Sortir de la boucle si la réponse est valide
                else:
                    print("La réponse doit être entre 1 et 200.")
            except ValueError:
                print("Veuillez entrer un chiffre valide.")

    return reponses

def dessin(liste_reponses):
    i = 0
    print(liste_reponses)
    while i < liste_reponses[0]:
        ma_tortue.left(liste_reponses[1])
        ma_tortue.forward(liste_reponses[2])
        ma_tortue.left(liste_reponses[1])
        ma_tortue.forward(liste_reponses[3])
        ma_tortue.left(liste_reponses[1])
        ma_tortue.forward(liste_reponses[4])
        ma_tortue.left(liste_reponses[1])
        ma_tortue.forward(liste_reponses[5])
        i = i + 1
        

if __name__ == "__main__":
    ma_tortue = turtle.Turtle()
    # Appeler la fonction
    liste_reponses = poser_questions()

    # Afficher les réponses
    print("Réponses:", liste_reponses)
    dessin1 = dessin(liste_reponses)

    # Attendez que l'utilisateur clique pour fermer la fenêtre
    turtle.onclick(turtle.bye)

    # Afficher la fenêtre
    turtle.mainloop()
