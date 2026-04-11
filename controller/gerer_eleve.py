from datetime import date,datetime
from model.eleve import Eleve

eleves=[]

def add_eleve(e):
    if isinstance(e,Eleve):
        eleves.append(e)


def delete_eleve(code):
    for e in eleves:
        if int(e.code) == int(code):
            eleves.remove(e)
            break

def update_eleve(code,nom,dn,sexe,ville):
    for e in eleves:
        if int(e.code) == int(code):
            e.nom_prenom=nom
            e.date_naissance=dn
            e.sexe=sexe
            e.ville=ville
            break
    for e in eleves:
        print(e)