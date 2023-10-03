from tkinter import *
root=Tk()


class Proizvodi():
    def __init__(self,id,naziv,cena):
        self.id=id
        self.naziv=naziv
        self.cena=cena
    
    def __str__(self):
        return'{}|{}|{}'.format(self.id,self.naziv,self.cena)

class User():
    def __init__(self,username,password,stanje):
        self.username=username
        self.password=password
        self.stanje=int(stanje)

    def __str__(self):
        return '{}|{}|{}'.format(self.username,self.password,self.stanje)

class Porudzbina(User,Proizvodi):
    def __init__(self):
        self.lista_user=[]
        self.lista_proizvoda=[]
        self.porudzbina=[]
        self.tren=None


    def ucitaj_user(self):
        l=[line.strip()for line in open('User.txt')]
        for i in l:
            r=i.split('|')
            p=User(r[0],r[1],r[2])
            self.lista_user.append(p)

    def ucitaj_proizvodi(self):
        l=[line.strip()for line in open('Proizvodi.txt')]
        for j in l:
            n=j.split('|')
            p=Proizvodi(n[0],n[1],n[2])
            self.lista_proizvoda.append(p)
    
    def login(self,username,password):
        if self.tren!=None:
            print('Korisnik {} je vec ulogovan'.format(self.tren.username))
            return
        else:
            p=False                   
            for i in self.lista_user:
                if i.username==username and i.password==password:
                    self.tren=i
                    p=True
            if p==True:
                print('Uspesna prijava')
            else:
                print('Korisnik sa tim kredencijalima ne postoji')
        
    
    def sign_out(self):
        if self.tren!=None:
            self.tren=None
            print('Uspesno odjavljivanje')
        else:
            print('Nije ulogovan nijedan korisnik')

    
    def registracija(self,username,password,stanje):
        for i in self.lista_user:
            if i.username==username:
                print('Username zauzet')
                return
            elif float(stanje)<=0:
                print('Nedovoljno sredstava')
                return
        if username!='' and password!='' and float(stanje)>0:
            p=User(username,password,stanje)
            self.lista_user.append(p)
            self.update_txt()
            print('Korisnik uspesno kreiran')

    def obrisi_user(self,password):
        if self.tren==None:
            print('Nije ulogovan nijedan korisnik')
        else:
            if self.tren.password==password:
                self.lista_user.remove(self.tren)
                print('Profil uspesno obrisan')
                self.update_txt()
                self.sign_out()
                return True
            else:
                print('Sifra neispravna')
                return False
    
    def update_txt(self):
        s=True
        f=open('User.txt','w')
        f.close()
        for i in self.lista_user:
            if s:
                s=False
                f=open('User.txt','a')
                print(i,file=f,end='')
                f.close()
            else:
                f=open('User.txt','a')
                print('\n',i,file=f,sep='',end='')
                f.close()
        print('Fajl azuriran')
    
    def dodaj_u_korpu(self,id_p,kolicina=Spinbox):
        global suma
        for i in self.lista_proizvoda:
            if str(id_p)==i.id:
                    self.porudzbina.append(int(i.cena)*int(kolicina))
                    suma=sum(self.porudzbina)
                    print('{} Proizvod/a je dodato u korpu'.format(kolicina))
    
    def odustani_od_placanja(self):
        global suma
        self.porudzbina.clear()
        suma=0

    
    def placanje(self):
        global suma
        if self.tren==None:
            print('Nije ulogovan nijedan korisnik. Ulogujte se za zavrsetak kupovine')
        elif self.tren!=None:
            if int(suma)==0:
                print('Niste dodali nijedan proizvod.')
            elif int(self.tren.stanje)<=int(suma):
                print('Nemate dovoljno sredstava na racunu. Na racunu raspolozivo {} RSD'.format (self.tren.stanje))
            else:
                self.tren.stanje-=int(suma)
                print('Placanje uspesno izvrseno, novo stanje je {} RSD'.format(self.tren.stanje))
                self.update_txt()
                suma=0
                self.porudzbina.clear()
        

    
    def stanje1(self):
        global username
        global stanje
        if self.tren==None:
            print('Nije ulogovan nijedan korisnik. Ulogujte se za podatke o korisniku')
        else:
            username=self.tren.username
            stanje=str(self.tren.stanje)
            print('Username: {}\nStanje na racunu: {}'.format(username,stanje))
            proveri_stanje()
    
    def ulogovan_azuriraj(self):
        if self.tren==None:
            tp=False
            azuriraj_podatke()
        else:
            tp=True
            azuriranje1()
    
    def azuriraj(self,username,password,stanje):
        if username in [x.username for x in self.lista_user]:
            print('Username zauzet')
            return
        self.tren.username = username
        self.tren.password = password
        self.tren.stanje = stanje
        self.update_txt()
        self.lista_user.append(self.tren)
        print('Username: {}\nPassword: {}\nStanje na racunu: {}'.format(username,password,stanje))
        
        

l=Label(root,text='Yoyo Online Shop')
l.grid(row=0,column=2,columnspan=1)
text1=Text(root,height=10,width=15)
text2=Text(root,height=10,width=15)
text3=Text(root,height=10,width=15)
text4=Text(root,height=10,width=15)
photo=PhotoImage(file='1.gif')
photo2=PhotoImage(file='2.gif')
photo3=PhotoImage(file='3.gif')
photo4=PhotoImage(file='4.gif')
text1.image_create(END, image=photo)
text2.image_create(END, image=photo2)
text3.image_create(END, image=photo3)
text4.image_create(END, image=photo4)
text1.grid(row=1,column=0)
text2.grid(row=1,column=3)
text3.grid(row=6,column=0)
text4.grid(row=6,column=3)
l1=Label(root,text='Duncan Proyo')
l1.grid(row=2,column=0)
s1=Spinbox(root,from_=1,to=10,width=3)
s1.grid(row=3,column=1)
l11=Label(root,text='kolicina',width=5)
l11.grid(row=3,column=0)
l01=Label(root,text='Cena: 900 RSD')
l01.grid(row=4,column=0)
b1=Button(root,text='Dodaj u korpu',command=lambda:p.dodaj_u_korpu(('1'),s1.get()))
b1.grid(row=5,column=0)

l2=Label(root,text='Magic Yoyo T9')
l2.grid(row=2,column=3)
s2=Spinbox(root,from_=1,to=10,width=3)
s2.grid(row=3,column=4)
l12=Label(root,text='kolicina',width=5)
l12.grid(row=3,column=3)
l02=Label(root,text='Cena: 1900 RSD')
l02.grid(row=4,column=3)
b2=Button(root,text='Dodaj u korpu',command=lambda:p.dodaj_u_korpu(('2'),s2.get()))
b2.grid(row=5,column=3)

l3=Label(root,text='Duncan Freehand')
l3.grid(row=7,column=0)
s3=Spinbox(root,from_=1,to=10,width=3)
s3.grid(row=8,column=1)
l13=Label(root,text='kolicina',width=5)
l13.grid(row=9,column=0)
l03=Label(root,text='Cena: 2200 RSD')
l03.grid(row=8,column=0)
b3=Button(root,text='Dodaj u korpu',command=lambda:p.dodaj_u_korpu(('3'),s3.get()))
b3.grid(row=10,column=0)

l4=Label(root,text='Magic Yoyo Holder')
l4.grid(row=7,column=3)
s4=Spinbox(root,from_=1,to=10,width=3)
s4.grid(row=8,column=4)
l14=Label(root,text='kolicina',width=5)
l14.grid(row=8,column=3)
l04=Label(root,text='Cena: 600 RSD')
l04.grid(row=9,column=3)
b4=Button(root,text='Dodaj u korpu',command=lambda:p.dodaj_u_korpu(('4'),s4.get()))
b4.grid(row=10,column=3)

b5=Button(root,text='Idi na kasu',command=lambda:kasa())
b5.grid(row=12,column=2,columnspan=1)

def kasa():
    t=Toplevel()
    l=Label(t,text='Racun za placanje iznosi '+str(suma)+' RSD')
    l.grid(row=0,column=0)
    b=Button(t,text='Plati',command=lambda:p.placanje())
    b.grid(row=1,column=0)
    b1=Button(t,text='Odustani',command=lambda:[p.odustani_od_placanja(),t.destroy()])
    b1.grid(row=1,column=1)


menubar=Menu(root)
u=Menu(menubar,tearoff=0)
u.add_command(label='Prijavi se',command=lambda:prijavljivanje())
u.add_command(label='Registruj se',command=lambda:kreiraj_profil())
menubar.add_cascade(label='Prijava',menu=u)
u1=Menu(menubar,tearoff=0)
u1.add_command(label='Sign Out',command=lambda:odjavljivanje())
u1.add_command(label='Obrisi Profil',command=lambda:obrisi_profil())
menubar.add_cascade(label='Odjava',menu=u1)
st1=Menu(menubar,tearoff=0)
st1.add_command(label='Proveri Stanje',command=lambda:p.stanje1())
st1.add_command(label='Azuriraj podatke',command=lambda:p.ulogovan_azuriraj())
menubar.add_cascade(label='Stanje i Azuriranje',menu=st1)
ex=Menu(menubar,tearoff=0)
ex.add_command(label='Exit',command=lambda:root.destroy())
menubar.add_cascade(label='Exit',menu=ex)
root.config(menu=menubar)

def proveri_stanje():
    t=Toplevel()
    l=Label(t,text='Podaci o korisniku')
    l.pack()
    l1=Label(t,text='Username: '+username+'\nStanje na racunu: '+stanje)
    l1.pack()

def azuriraj_podatke():
    t=Toplevel()
    l=Label(t,text='Nije ulogovan nijedan korisnik.Ulogujte se za azuriranje podataka.')
    l.pack()

def azuriranje1():
    t=Toplevel()
    l=Label(t,text='Podaci o korisniku')
    l.grid(row=0,column=1)
    l1=Label(t,text='Username')
    l1.grid(row=1,column=0)
    e1=Entry(t)
    e1.insert(END,p.tren.username)
    e1.grid(row=1,column=1)
    l2=Label(t,text='Password')
    l2.grid(row=2,column=0)
    e2=Entry(t)
    e2.insert(END,p.tren.password)
    e2.grid(row=2,column=1)
    l3=Label(t,text='Stanje')
    l3.grid(row=3,column=0)
    e3=Entry(t)
    e3.insert(END,p.tren.stanje)
    e3.grid(row=3,column=1)
    b=Button(t,text='Azuriraj podatke',command=lambda:p.azuriraj(e1.get(),e2.get(),e3.get()))
    b.grid(row=4,column=1,columnspan=1)
    b1=Button(t,text='Odustani',command=lambda:t.destroy())
    b1.grid(row=5,column=1,columnspan=1)


def prijavljivanje():
   t=Toplevel()
   l1=Label(t,text='Username')
   l1.grid(row=2,column=0)
   e1=Entry(t)
   e1.grid(row=2,column=1)
   l2=Label(t,text='Password')
   l2.grid(row=3,column=0)
   e2=Entry(t)
   e2.grid(row=3,column=1)
   b=Button(t,text='Login',command=lambda:p.login(e1.get(),e2.get()))
   b.grid(row=4,column=1,columnspan=1)

def kreiraj_profil():
    t=Toplevel()
    l=Label(t,text='Username')
    l.grid(row=0,column=0)
    e=Entry(t)
    e.grid(row=0,column=1)
    l1=Label(t,text='Password')
    l1.grid(row=1,column=0)
    e1=Entry(t)
    e1.grid(row=1,column=1)
    l2=Label(t,text='Stanje na racunu')
    l2.grid(row=2,column=0)
    e2=Entry(t)
    e2.grid(row=2,column=1)
    b1=Button(t,text='Registruj se',command=lambda:p.registracija(e.get(),e1.get(),e2.get()))
    b1.grid(row=3,column=1,columnspan=1)

def odjavljivanje():
    t=Toplevel()
    l=Label(t,text='Da li ste sigurni da zelite da se odjavite?')
    l.grid(row=0,column=1,columnspan=1)
    bd=Button(t,text='Da',command=lambda:p.sign_out())
    bd.grid(row=1,column=0)
    bn=Button(t,text='Ne',command=lambda:t.destroy())
    bn.grid(row=1,column=1)



def obrisi_profil():
    global t4
    def obrisi1():
        global t4
        if p.obrisi_user(e2.get()):
            t.destroy()
            root.iconify()
            root.focus_force()
        else:
            t.destroy()
    t=Toplevel()
    l=Label(t,text='Unesite sifru kako biste obrisali profil')
    l.grid(row=0,column=1,columnspan=1)
    l1=Label(t,text='Password')
    l1.grid(row=1,column=0)
    e2=Entry(t)
    e2.grid(row=1,column=1)
    b=Button(t,text='Obrisi',command=lambda:obrisi1())
    b.grid(row=2,column=1,columnspan=1)
t4=None

p=Porudzbina()
p.ucitaj_user()
# for i in p.lista_user:
#     print()
#     print(i)
#     print()
# p.login('Petar Petrovic','5555')
p.ucitaj_proizvodi()
# for j in p.lista_proizvoda:
#     print()
#     print(j)
# p.registracija('njnj','12356','6000')






























mainloop()