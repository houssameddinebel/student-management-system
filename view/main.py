import tkinter as tk
from tkinter import ttk ,messagebox
from model.eleve import Eleve
from controller.gerer_eleve import *
from datetime import datetime

#les méthodes
def effacer() :
    nom.set("")
    dn.set("")
    cb_ville.set("Agadir")
    sexe.set("m")
    e_nom.focus()
    e_dn.config(bg="blue")
    
def effacer_table():
     for item in table.get_children():
         table.delete(item)
def statistique():
    lb_total_eleve.config(text=f"Total Eléve : {len(eleves)} ")
    nbre_male = len(list(filter(lambda e: e.sexe == "m", eleves)))
    lb_total_male.config(text=f"Total Male : {nbre_male} ")
    lb_total_femelle.config(text=f"Total Femelle : {len(eleves) - nbre_male} ")
def load_table() :
    effacer_table()
    for eleve in eleves:
        genre = "Male" if eleve.sexe == "m" else "Femelle"
        date_n = datetime.strftime(eleve.date_naissance, "%d/%m/%Y")
        table.insert("", tk.END,
                     values=(eleve.code, eleve.nom_prenom, date_n, genre, eleve.ville))
def delete() :
       if code.get() != 0 :
          if messagebox.askyesno("confirmation","Voulez-vous supprimer cet éléve ? ")  == True :
                 delete_eleve(code.get())

       effacer()
       load_table()
       statistique()

def ajouter_eleve():
    try:
      e=Eleve(nom.get(),datetime.strptime(dn.get(),"%d/%m/%Y"),sexe.get(),cb_ville.get())
      add_eleve(e)
      effacer()
      #apple de la méthode de remplissage du table Treeview
      load_table()
      #appel de la méthode statistique
      statistique()
    except ValueError:
      messagebox.showerror("Message erreur","La date naissance invalide\n"
                        "Veuillez saisir la date sous forme dd/mm/yyyy")
      dn.set("")
      e_dn.focus()
      e_dn.config(bg="red")
def update():
      try:
           if int(code.get()) != 0 :
             if messagebox.askokcancel("Confirmation","Voulez-vous modifier les informations") == True:
              update_eleve(code.get(),nom.get(),datetime.strptime(dn.get(),"%d/%m/%Y"),sexe.get(),cb_ville.get())
      except ValueError:
          messagebox.showerror("Message erreur", "La date naissance invalide\n"
                                                 "Veuillez saisir la date sous forme dd/mm/yyyy")
      effacer()
      # apple de la méthode de remplissage du table Treeview
      load_table()
      # appel de la méthode statistique
      statistique()
      code.set(0)

def quitter():
     if messagebox.askyesno("Message confirmation","Voulez-vous quitter ? ")==True :
              quit()
def on_select(event):

    item=table.selection()
    if item:
        id=item[0]
        values=table.item(id,"values")
        code.set(values[0])
        nom.set(values[1])
        dn.set(values[2])
        sexe.set("m" if values[3] == "Male" else "f")
        cb_ville.set(values[4])
#*------------------------------------------------
root=tk.Tk()
root.title("Gestion des éléves")
root.geometry("700x600")
#les varaibles de travail
code=tk.StringVar(value=0)
nom=tk.StringVar()
dn=tk.StringVar()
sexe=tk.StringVar()
#les widgets
lb_fiche=tk.Label(root,text="Fiche Eléve ",bg="blue",fg="yellow",width=50)
lb_fiche.place(x=100,y=10)
#----------------------------------------------------------------------------
lb_nom=tk.Label(root,text="Nom & Prénom : ",bg="blue",fg="yellow")
lb_nom.place(x=20,y=40)
e_nom=tk.Entry(root,textvariable=nom,bg="blue",fg="yellow")
e_nom.place(x=130,y=40)
#----------------------------------------------------------------------------
lb_dn=tk.Label(root,text="Date Naissance : ",bg="blue",fg="yellow")
lb_dn.place(x=20,y=70)
e_dn=tk.Entry(root,textvariable=dn,bg="blue",fg="yellow")
e_dn.place(x=130,y=70)
#----------------------------------------------------------------------------
lb_sexe=tk.Label(root,text="Sexe Eléve : ",bg="blue",fg="yellow")
lb_sexe.place(x=20,y=100)

rb_sexe1=tk.Radiobutton(root,text="Male",variable=sexe,value="m")
rb_sexe1.place(x=130,y=100)
rb_sexe2=tk.Radiobutton(root,text="Femelle",variable=sexe ,value="f")
rb_sexe2.place(x=200,y=100)
sexe.set("m")
#----------------------------------------------------------------------------
lb_ville=tk.Label(root,text="Ville Natale : ",bg="blue",fg="yellow")
lb_ville.place(x=20,y=130)
cb_ville=ttk.Combobox(root,values=["Agadir","Tiznit","Ait Melloul","Ben sergaou","Inzegane","Autre"],state="readonly")
cb_ville.place(x=130,y=130)
cb_ville.set("Agadir")
#------------------------------------------
bt_add=tk.Button(root,text="Add",bg="green",fg="yellow",width=10,command=ajouter_eleve)
bt_add.place(x=40,y=170)
#------------------------------------------
bt_clear=tk.Button(root,text="Clear",bg="green",fg="yellow",width=10,command=effacer)
bt_clear.place(x=130,y=170)
#------------------------------------------
bt_delete=tk.Button(root,text="Delete",bg="green",fg="yellow",width=10,command=delete)
bt_delete.place(x=220,y=170)
#------------------------------------------
bt_update=tk.Button(root,text="Update",bg="green",fg="yellow",width=10,command=update)
bt_update.place(x=310,y=170)
#------------------------------------------
bt_exit=tk.Button(root,text="Exit",bg="green",fg="yellow",width=10,command=quitter)
bt_exit.place(x=400,y=170)
#-----------------------------------------------
table=ttk.Treeview(root,columns=["code","nom","dn","sexe","ville"],show="headings",height=2)
#-----------------------------afficher les entêtes
table.heading("code",text="code Eléve")
table.heading("nom",text="Nom & Prénom")
table.heading("dn",text="Date Naissance")
table.heading("sexe",text="Sexe")
table.heading("ville",text="Ville Natale")

#----------------------------------------
table.column("code",width=100)
table.column("nom",width=120)
table.column("dn",width=100)
table.column("sexe",width=100)
table.column("ville",width=100)
scroll_y=tk.Scrollbar(root,orient="vertical",command=table.yview)
scroll_x=tk.Scrollbar(root,orient="horizontal",command=table.xview)
table.config(yscrollcommand=scroll_y.set)
table.config(xscrollcommand=scroll_x.set)
table.place(x=50,y=210,width=550,height=80)
scroll_y.place(x=600,y=210,height=80)
scroll_x.place(x=50,y=290,width=550)
lb_total_eleve=tk.Label(root,text=f"Total eleve : {len(eleves)}")
lb_total_eleve.place(x=200,y= 310)
#variables nbre_male , nbre_femelle
nbre_male=len(list(filter(lambda e:e.sexe == "m",eleves)))
lb_total_male=tk.Label(root,text=f"Total Male : {nbre_male}")
lb_total_male.place(x=200,y= 330)
lb_total_femelle=tk.Label(root,text=f"Total Femelle : {len(eleves) - nbre_male}")
lb_total_femelle.place(x=200,y= 350)
table.bind("<<TreeviewSelect>>", on_select)
root.mainloop()






