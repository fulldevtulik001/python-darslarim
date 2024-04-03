# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:01:12 2024

@author: DELL
"""

# 8 dars list(ruyxatlar) 
#Tulqin Shog'dorov

#ismlar=['Shaxboz','Islom','Akbar',"Jamshid"]
#print("Salom do'satlar yaxshimisilar " + ismlar[0] + " bugun choyxonaga boraizmi "
 #     + ismlar[-1] + "Bilan gaplashgandim "  + ismlar[-2] + ' telfon qilib bugun menikiga kelinglar debdi!')
 
#t_shaxslar=['Amur Temur',"Jaloliddin",'Abulla Qodiriy',"Islom Karimov"]
#z_shaxslar=['Ilon Mask','Anvar Narzullayev','shavkat Mirziyayev']

#print("men tarixiy shaxslardAN " + t_shaxslar.pop(2) + " BILAN ,  Zamonaviy shaxslardan esa " + z_shaxslar.pop(-1) + " suhbatlashishni istar edim")

friends=[]
friends.append("Jaxongir")
friends.append("Sardor")
friends.append("Shaxboz")
friends.append("Islom")
friends.append("Doniyor")

friends.remove('Jaxongir')
friends.remove('Sardor')

friends.append('Akbar')
friends.insert(0, 'Nodir')
friends.insert(2, 'Tulqin')

mehmonlar=[]
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(3))
print(mehmonlar)
