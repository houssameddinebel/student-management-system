from datetime import date,datetime

class Eleve:
    count = 0

    def __init__(self,nom_prenom="anonyme", date_naissance = datetime.now(),sexe="m",ville = "Agadir"):
        Eleve.count += 1
        self.code = Eleve.count
        self.nom_prenom = nom_prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.ville = ville


    def __str__(self):
        var_sexe = "Male" if self.sexe == "m" else "female"
        dn = datetime.strftime(self.date_naissance,"%d/%m/%Y")
        return (f"Code eleve : {self.code} \n "
                f"Nom prenom : {self.nom_prenom} \n "
                f"Date naissance : {dn} \n "
                f"Sexe : {self.sexe} \n "
                f"Ville : {self.ville}")


