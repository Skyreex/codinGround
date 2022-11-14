nbEtudiants = int(input("Donner le nombre d'étudiants : "))
for j in range(1, nbEtudiants+1):
    nom = input("Entrez le nom d'étudiant : ")
    math = int(input(f"Entrez la note de math pour l'étudiant {nom} : "))
    phy = int(input(f"Entrez la note de physique pour l'étudiant {nom} : "))
    fr = int(input(f"Entrez la note de français pour l'étudiant {nom} : "))
    ang = int(input(f"Entrez la note d'anglais pour l'étudiant {nom} : "))
    hg = int(input(f"Entrez la note d'histoire-géo pour l'étudiant {nom} : "))
    print(f"l'étudiant {nom} a eu : {((math + phy) * 5 + (ang + hg) * 2 + fr * 4) / 18}")
