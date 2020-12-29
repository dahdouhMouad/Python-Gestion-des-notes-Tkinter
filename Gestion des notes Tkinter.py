from __future__ import print_function
from Tkinter import *
import mysql.connector
import tkMessageBox

class Etudiant(object):

    def __init__(self, cne, nom_etu, prenom_etud,filier): 
        self.cne= cne
        self.nom_etu = nom_etu
        self.prenom_etud=prenom_etud
        self.filier = filier

#getter
    def get_cne(self):
        return self.cne
    def get_nom_etu(self):
        return self.nom_etu
    def get_prenom(self):
        return self.prenom_etud
    def get_filier(self):
        return self.filier
#setter
    def set_cne(self,cne):
        self.cne==cne
    def set_nom_etu(self,nom_etu):
        self.nom_etu=nom_etu
    def set_prenom_etud(self,prenom_etud):
        self.prenom_etud=prenom_etud
    def set_filier(self,filier):
        self.filier=set_filier
class base_donnes():
    def __init__(self,host,user,passwd):
        self.host=host
        self.user=user
        self.passwd=passwd

    def bd_quory(self,query,base):
        db_connection = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,db=base)
        cur=db_connection.cursor()
        cur.execute(query)  
        db_connection.commit()
        

    def bd_quory_return(self,query,base):
        db_connection = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,db=base)
        cur1=db_connection.cursor()
        cur1.execute(query)
        data=cur1.fetchall()
        db_connection.commit() 
        return data   
        

class TK(Frame,Etudiant):
    def faireApparaitreLeToplevel(self):
        def affich():
            base1 =base_donnes("localhost","root","")
            cne = SECNE.get()
            note = SENOTE.get()
            mat=SEMAT.get()
            if cne=="" or note=="" :
                pass
            else:
                query1 = " insert into notes values("+'"'+str(cne)+'"'+","+'"'+str(mat)+'"'+","+'"'+str(note)+'"'+")"
                base1.bd_quory(query1,"tp_python")

                SECNE.delete(0,END)
                SENOTE.delete(0,END)



        top=Toplevel(self)
        top.geometry('1000x700')
        base1 =base_donnes("localhost","root","")
        query = """SELECT * from etudiant"""
        data =base1.bd_quory_return(query,"tp_python")
        print(data)
        c=40
        label_1 = Label(top, text='CNE',width=20,font=("bold", 10),bg="brown4",fg='snow')
        label_1.place(x=0,y=0)
        label_1 = Label(top, text='NOM',width=20,font=("bold", 10),bg="brown4",fg='snow')
        label_1.place(x=200,y=0)
        label_1 = Label(top, text='PRENOM',width=20,font=("bold", 10),bg="brown4",fg='snow')
        label_1.place(x=400,y=0)


        Titre = Label(top, text="  Saiser Les informations  ",width=30,bg="brown4",fg='snow')
        Titre.place(x=690,y=0)
        SLMAT = Label(top, text="MATIERE:",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        SLMAT.place(x=600,y=80)
        SEMAT = Entry(top)
        SEMAT.place(x=760,y=80)
        SLCNE = Label(top, text="CNE:",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        SLCNE.place(x=600,y=130)
        SECNE = Entry(top)
        SECNE.place(x=760,y=130)
        SLNOTE = Label(top, text="NOTE:",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        SLNOTE.place(x=600,y=180)
        SENOTE = Entry(top)
        SENOTE.place(x=760,y=180)
        
        for item in data:
            label_1 = Label(top, text=item[0],width=20,font=("bold", 10),bg='bisque')
            label_1.place(x=0,y=c)
            label_1 = Label(top, text=item[1],width=20,font=("bold", 10),bg='bisque')
            label_1.place(x=200,y=c)
            label_1 = Label(top, text=item[2],width=20,font=("bold", 10),bg='bisque')
            label_1.place(x=400,y=c)
            c=c+30
        submit=Button(top, text='Submit',width=20,bg='brown',fg='white',command=affich)
        submit.place(x=740,y=230)    


    def faireApparaitreLeToplevel1(self):
        def Afficher() :
            base =base_donnes("localhost","root","")
            cne = entry_1.get()
            nom = entry_2.get()
            prenom = entry_3.get()
            filier = entry_4.get()
            
            if cne=="" or nom=="" or prenom=="" or filier=="":
                pass
            else:
            	
            	etudiant1 = Etudiant(cne,nom,prenom,filier)
                query="INSERT INTO etudiant VALUES("+'"'+str(etudiant1.get_cne())+'"'+","+'"'+str(etudiant1.get_nom_etu())+'"'+","+'"'+str(etudiant1.get_prenom())+'"'+","+'"'+str(etudiant1.get_filier())+'"'+")"
                print(query)
                base.bd_quory(query,"tp_python")
                tkMessageBox.showinfo( "Hello Python", "sucess")
                entry_1.delete(0,END)
                entry_2.delete(0,END)
                entry_3.delete(0,END)
                entry_4.delete(0,END)
                


        top=Toplevel(self)
        top.geometry('500x500')
        Titre = Label(top, text="  Saiser Les informations  ",width=30,bg="brown4",fg='snow')
        Titre.place(x=119,y=70)
        label_1 = Label(top, text="  Cne :",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        label_1.place(x=68,y=130)

        entry_1 = Entry(top)
        entry_1.place(x=240,y=130)
        

        label_2 = Label(top, text="  Nom :",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        label_2.place(x=68,y=180)

        entry_2 = Entry(top)
        entry_2.place(x=240,y=180)

        label_3 = Label(top, text="  Prenom :",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        label_3.place(x=68,y=230)

        entry_3 = Entry(top)
        entry_3.place(x=240,y=230)

        label_4 = Label(top, text=" Filier :",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        label_4.place(x=68,y=270)

        entry_4 = Entry(top)
        entry_4.place(x=240,y=270)
        Value = StringVar()
        
        submit=Button(top, text='Submit',width=20,bg='brown',fg='white',command=Afficher)
        submit.place(x=160,y=330)


    def affichenote(self):
        top=Toplevel(self)
        top.geometry('800x500')
        bas =base_donnes("localhost","root","")
        qu = """SELECT etudiant.cne,etudiant.nom_etu,notes.nom_mat,notes.note from notes,etudiant where etudiant.cne=notes.cne_etu"""
        data =bas.bd_quory_return(qu,"tp_python")
        print(data)
        Titre = Label(top, text="Les Notes",width=20,bg="brown4",fg='snow')
        Titre.place(x=290,y=0)
        label_1 = Label(top, text='CNE',width=20,font=("bold", 10),bg="brown4",fg='snow')
        label_1.place(x=0,y=40)
        label_1 = Label(top, text='NOM',width=20,font=("bold", 10),bg="brown4",fg='snow')
        label_1.place(x=200,y=40)
        label_1 = Label(top, text='MATIERE',width=20,font=("bold", 10),bg="brown4",fg='snow')
        label_1.place(x=400,y=40)
        label_1 = Label(top, text='NOTE',width=20,font=("bold", 10),bg="brown4",fg='snow')
        label_1.place(x=600,y=40)
        c=80
        for item in data:
            label_1 = Label(top, text=item[0],width=20,font=("bold", 10),bg='bisque')
            label_1.place(x=0,y=c)
            label_1 = Label(top, text=item[1],width=20,font=("bold", 10),bg='bisque')
            label_1.place(x=200,y=c)
            label_1 = Label(top, text=item[2],width=20,font=("bold", 10),bg='bisque')
            label_1.place(x=400,y=c)
            label_1 = Label(top, text=item[3],width=20,font=("bold", 10),bg='bisque')
            label_1.place(x=600,y=c)
            c=c+30

    def suppetu(self):
        def supprimer():
            base3 =base_donnes("localhost","root","")           
            CNE = entry_4.get()
            base4 =base_donnes("localhost","root","")           
            if CNE=="":
                pass
            else:
                query="delete from etudiant where CNE="+'"'+str(CNE)+'"'
                query1="delete from notes where cne_etu="+'"'+str(CNE)+'"'
                print(query)
                print(query1)
                base3.bd_quory(query,"tp_python")
                base4.bd_quory(query1,"tp_python")
                entry_4.delete(0,END)


        top=Toplevel(self)
        top.geometry('600x300')
        #Titre = Label(top, text="  Saiser Les informations  ",width=30,bg="brown4",fg='snow')
        #Titre.place(x=160,y=40)
        label_4 = Label(top, text="CNE",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        label_4.place(x=68,y=105)

        entry_4 = Entry(top)
        entry_4.place(x=240,y=105)
        Value = StringVar()
        
        submit=Button(top, text='Submit',width=20,bg='brown',fg='white',command=supprimer)
        submit.place(x=220,y=160)

    def modifiernote(self):
        def Afficher() :

            base3 =base_donnes("localhost","root","")
            MATIER = SEMAT.get()
            CNE = SECNE.get()
            NOTE = SENOTE.get()            
            if MATIER=="" or CNE=="" or NOTE=="":
                pass
            else:
                query="UPDATE notes SET note =" +'"'+str(NOTE)+'"' + "where cne_etu="+'"'+str(CNE)+'"'+"and nom_mat ="+'"'+str(MATIER)+'"'
                print(query)
                base3.bd_quory(query,"tp_python")
                SEMAT.delete(0,END)
                SECNE.delete(0,END)
                SENOTE.delete(0,END)
        
        top=Toplevel(self)
        top.geometry('500x500')
        base1 =base_donnes("localhost","root","")
        SLMAT = Label(top, text="MATIERE",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        SLMAT.place(x=20,y=80)
        SEMAT = Entry(top)
        SEMAT.place(x=170,y=80)
        SLCNE = Label(top, text="CNE",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        SLCNE.place(x=20,y=130)
        SECNE = Entry(top)
        SECNE.place(x=170,y=130)
        SLNOTE = Label(top, text="NOTE",width=20,font=("bold", 10),bg="SlateGray4",fg='snow')
        SLNOTE.place(x=20,y=180)
        SENOTE = Entry(top)
        SENOTE.place(x=170,y=180)
        submit=Button(top, text='Submit',width=20,bg='brown',fg='white',command=Afficher)
        submit.place(x=170,y=230)

    def  __init__(self):
        Frame.__init__(self,height=450,width=500, bd=1)
        self.option_add("*font","arial 12 bold")
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Gestion des notes ")
        lbl1 = Label(text = "  Gestion des notes  ",bg="brown4",fg='snow')  
        lbl1.place(x=165,y=40)
        B = Button(text ="Remplir note", width =30,bg='DarkGoldenrod3',fg='white',command = self.faireApparaitreLeToplevel)
        B.place(x=80,y=90)
        #lbl2 = Label(text = "Remplir note :",bg="sky blue",fg='gray25')  
        #lbl2.place(x=100,y=130)
        B1 = Button( text ="Afficher note",width =30,bg='DarkGoldenrod3',fg='white', command = self.affichenote)
        B1.place(x=80,y=160)

        #lbl3 = Label(text = "Afficher Note :",bg="sky blue",fg='gray25')  
        #lbl3.place(x=120,y=200)
        B3 = Button( text ="Modifier note",width =30,bg='DarkGoldenrod3',fg='white', command = self.modifiernote)
        B3.place(x=80,y=230)

        #lbl4 = Label(text = "Modifier Note :",bg="sky blue",fg='gray25')  
        #lbl4.place(x=120,y=270)
        B4 = Button( text ="Ajouter Etudiant",width =30,bg='DarkGoldenrod3',fg='white', command = self.faireApparaitreLeToplevel1)
        B4.place(x=80,y=300)
        #modifieretu = Label(text = "Supprimer Etudiant :")  
        #modifieretu.place(x=120,y=120)
        B4modifieretu = Button( text ="Supprimer Etudiant",width =30,bg='DarkGoldenrod3',fg='white',command = self.suppetu)
        B4modifieretu.place(x=80,y=360)
       


executer =TK().mainloop()
#print(base.bd_quory(query,"tp_python"))


