# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:12:57 2024

@author: DELL
"""

#for operatori

#ismlar=['jAMSHID',  'Sarvar','Anvar','Turg\'un','Nizomiddin']

#for ism in ismlar:
#    print(f"Salom mening dustim {ism} sani ko'rganimdan xursandman!")
#print(f" Sikl jaroyoni {len(ismlar)} marotaba takrorlanadi" )

#toq_sonlar=list(range(11,100,2))
#for son in toq_sonlar:
#    print(f"{son} ni kubi {son**3} ga teng " )

#kinolar=[]
#print("Sevimli kinolarizgizni kiritng")
#for n in range(5):

#    kinolar.append(input(f" {n+1} kino nomini kiriting: "))
#print(kinolar)
    

people=int(input("bugun nechta inson bilan suhbatlashdingiz"))
odamlar=[]
for p in range(people):
   odamlar.append(input(f" {p+1} chi suhbatlashgan insoniz: "))
print(odamlar)