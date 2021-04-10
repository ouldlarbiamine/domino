# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:50:07 2021

@author: ITDR 
"""
import random

class domino:# créer la classe dominio
    """
    constructeur qui permet de creer un instance de class Domino 
    paramaitres:
        x,y : les deux phase (phase gauche et droite )
    example :
        d=domino(1,2)
        d2=domino(6,6)
    
    """
    def __init__(self, x, y):
        self.droite = y# nb  point te3. ladroite  
        self.gauche = x#nb point te3 la gauche 
    """
        fonction  qui permet d'afficher un domino 
        paramaitres:
            sans paramaitres
        renvoie :
            chaine de caracatire de form : |phase gauche | phase droite |
       
            
    
    """
    def __str__(self):
        return str("|"+str( self.gauche)+"|"+str(self.droite)+"|")# pour afichie un domino  exemple |3|6|
    """
        fonction  qui permet de transformer un domino 
        paramaitres:
            sans paramaitres
        renvoie :
            chaine de caracatire de form : |phase gauche | phase droite |
        exmple 
         >>>d=domino(5,6)
         >>>print(d)
             |5 |6 | 
         >>>d.pivoter()
         >>>print(d)
                 |6 |5 | 
       
            
    """    
    def pivoter(self):
        self.droite,self.gauche=self.gauche,self.droite
   
    """
        fontion qui renovie le nbr de point a droite
        sans paramaitre 
        ex :
            >>>d=domino(5,6)
            >>>print(d.get_droite())
                        6
            
    """
    def get_droite(self):
        return self.droite
    """
        fontion qui renovie le nbr de point a gauche
        sans paramaitre 
        ex :
            >>>d=domino(5,6)
            >>>print(d.get_gauche())
                        5
            
    """
    def get_gauche(self):
        return self.gauche
        
    
        
        
        
        
        
class Maillon:
    #constructeur 
    def __init__(self,d):
        self._domino=d
        self.tete=None
        self.queue=None
    #str methode 
    def __str__(self):
        return self._domino.__str__()
    # renvoie element droite 
    def get_val_droite(self):
        return self._domino.get_droite()
    #renvoie element gauche 
    def get_val_gauche(self):
        return self._domino.get_gauche()
    """
            fonction renvoie true si les deux phase sans egeaux
            par ex:
                m=Maillon(domino(5,5))
                print(m.est_double())
                    True
                m2=Maillon(domino(6,5))
                print(m2.est_double())
                    False
    """
    def est_double(self):
        if self.get_val_droite()==self.get_val_gauche():
            return True
        else:
            return False
    """
            fonction compare entre maillon current et un autre maillon et comparer ces valeur 
            paramaitre : 
                Maillon M
            return :
                true si m.domino =M.domino  ou bien m.domino =M.domino.pivoter()
            par ex:
                m=Maillon(domino(5,5))
                m2=Maillon(domino(5,5))
                print(m.domino_egale_domino(m2))
                    True
                m3=Maillon(domino(6,5))
                print(m.domino_egale_domino(m3))
                    False
    """
    def domino_egale_domino(self,Maillon2):
        if self.get_val_droite()==Maillon2.get_val_gauche() and Maillon2.get_val_droite()==self.get_val_gauche() :
            return True
        elif self.get_val_droite()==Maillon2.get_val_droite() and  Maillon2.get_val_gauche()==self.get_val_gauche() :
            return True
        else:
            return False
    """
            fonction verifier si un entier n apparaite dans le domino  
            paramaitre : 
                n
            return :
                true si m.domino.gauche=n ou m.domino.droite=n
            par ex:
                m=Maillon(domino(5,5))
                
                print(m.si_val_in(5))
                    True
               
                print(m.si_val_in(3))
                    False
    """
    def si_val_in(self,n):
        if  self.get_val_droite()==n or self.get_val_gauche()==n:
            return True
        else:
            return False
    """
            fonction pivoter un maillon
              sans paramaitre : 
                
            
            par ex:
                m=Maillon(domino(5,2))
                
                print(m.pivoter_maillon())
                    |2 |5 |
               
                
    """ 
    def  pivoter_maillon(self):
        self._domino.pivoter()
        """
            fonction calculer la somme de  un maillon 
              sans paramaitre : 
                
            renvoie la somme de point 
            par ex:
                m=Maillon(domino(5,2))
                
                print(m.somme_des_point())
                    7
               
                
    """ 
    def somme_des_point(self):
        return self.get_val_droite() + self.get_val_gauche()


        
class Liste:
    #contsteur
    def __init__(self):
        self.list_domino=None
        
    def __str__(self):
        p=self.list_domino
        ch=""
        
        while p!=None:
            ch+=p.__str__()+" "
            p=p.queue
        

        return ch
        """
            fonction ajouer un element a la tete de la list  
            paramaitre : 
                element : maillon
            par ex:
                m=Maillon(domino(5,5))
                l=List()
                l.ajout_tete(m)
         
    """
    def  ajout_tete(self,element):
        
        if self.list_domino==None:
            self.list_domino=element
        else:
            x=self.list_domino.get_val_gauche()
            if element.get_val_gauche()==x and element.get_val_droite()!=x :


                element.pivoter_maillon()

            self.list_domino.tete=element
            element.queue= self.list_domino
            self.list_domino=element     
    """
         fonction ajouer un element a la fin  de la list  
            paramaitre : 
                element : maillon
            par ex:
                m=Maillon(domino(5,6))
                
                l.ajout_tete(m)
    """

    def  ajout_queue(self,element):
        if self.list_domino==None:
            self.list_domino=element
        else:
            p=self.list_domino
            while p.queue!=None:
                p=p.queue

            x=p.get_val_droite()
            if element.get_val_gauche()!=x and element.get_val_droite()==x :
                element.pivoter_maillon()
            p.queue=element
            element.tete=p
    """
    fontion  renvoyant le domino situé à l’indice i.
    paramaite :
        i :index 
    return : domino numero i ;
    
    """

    def valeur(self,i):
        p=self.list_domino
        cpt=1
        while cpt<i:
            cpt+=1
            p=p.queue
        if p==None:
            print("la valeure de i > le nombre  de domino ")
            return 
        else:
            return p
    """
    fontion  compte
    renovie la longeur des la list 
    
    
    """
    def compt(self):
        if  self.list_domino==None:
            return  0
        
        p=self.list_domino
        cpt=1
        while p.queue!=None:
            cpt+=1
            p=p.queue
        return cpt
    """
    fontion  suprime un domino .
    paramaite :
        element  :domino  
    
    
    """
    def supprime(self,n):
        if self.list_domino.domino_egale_domino(n):
            x = self.list_domino
            self.list_domino = x.queue
            x = None
            return 
        else:
            p = self.list_domino
            q=p.queue
            while p.domino_egale_domino(n)==False and q!=None :
                p = q
                q=q.queue
            if q==None:
                if p.domino_egale_domino(n):
                    q=p.tete
                    q.queue=None
                    p=None
            else:
                
                q=p.tete
                q.queue=p.queue
                p=None
    """
    fontion  renvoie le valeur de la queue de la liste 
    sans paramaite :
        
    
    
    """    

        
    def val_de_queque(self):
        p=self.list_domino
        while p.queue!=None:
            p=p.queue
        
        return p.get_val_droite()
    """
    fontion  renvoie le valeur de la tete de la liste 
    sans paramaite :
        
    
    
    """    
        
    def val_de_tete(self):
        return self.list_domino.get_val_gauche()
'''
fontion qui afficher le cotenu de la main d'un joueur
arguement  
    main : list des domino 
    retourne : chaine de caracaitre qui represent la main de joueur 
'''
def afiche_main_joueur(main):
    ch=""
    for  m in main:
        ch+=str(m.__str__())+"  "
    print (ch)
'''
fontion qui afficher le cotenu de la main d'un joueur
arguement  
    main : list des domino 
    retourne : chaine de caracaitre(?,?)  qui represent la main de pc 
    on affiche ? pour que le joueur ne connait pas ce qui est chez le pc 
    
'''
def afiche_main_PC(main):
    ch=""
    for  m in main:
        ch+="|?|?|"+"  "
    print (ch)
'''
fontion qui creer des  main pour le pc et joueur aleatoirement 
sans arguement  
retourne :dictionnaire 
        cle:value { joueur 1: 7 domino, pc :7 domino , rest :14 domino}
        
    
'''
def creer_deux_mains():
    l=[]
    cpt=0
    for i in range(0,7):
        for j in range (0,7):
            if  i>=j:
                a = domino(i, j)
                m = Maillon(a)
                l+=[m]
                cpt+=1
    Liste_des_position=[]
    k=0       
    for m in l:
        Liste_des_position+=[k]
        k+=1
    languer=len(Liste_des_position)
    main_joueur=[]
    main_PC=[]
    sign=1
    while languer>14 :
        n=random.randint(0,languer-1)
        
        languer-=1
        if sign>0:
            main_joueur+=[l[Liste_des_position[n]]]
        else :
            main_PC+=[l[Liste_des_position[n]]]
        sign=-sign
        del  Liste_des_position[n]
        
    Liste_des_position_de_rest=[]
    while languer> 0:
        n=random.randint(0,languer-1)

        Liste_des_position_de_rest+=[Liste_des_position[n]]
        del  Liste_des_position[n]

        languer-=1
        
    
    
    
    le_reste_de_domino=[]
    for n in Liste_des_position_de_rest:
        le_reste_de_domino+=[l[n]]
 
    d={"main_joueur":main_joueur,"main_PC":main_PC,"le_reste_de_domino":le_reste_de_domino}
    return d
"""
recherche dans un main si il y a un  domino double 
pararmatire :
    main : les domino d'un joueyr ou pc
renvoie : true si l'un des ces domino est double (ces deux phase egaux)
"""
def rechercher_le_domino_double(main):
    for m in main:
        if m.est_double():
            return True
    return False
        
"""
recherche dans un main et renovie le maillon qui est un domin double plus grand 
pararmatire :
    main : les domino d'un joueyr ou pc
renvoie : le double le plus grand 
"""        

def rechercher_le_domino_double_de_valeur_la_plus_elevee(main):
    val_max=-1
    
    for m in main:
        if m.est_double():
            if val_max<m.get_val_droite():
                val_max=m.get_val_droite()
                Maillon_max=m
    return Maillon_max  
        
"""
recherche dans un main et renovie le maillon plus grand  en terme de somme des ceselements 
pararmatire :
    main : list des domino d'un joueyr ou pc
renvoie : le maillon  plus grand 
"""    
def Rechercher_la_piece_qui_a_le_plus_grand_somme_de_points(main):
    som_max=-1
    
    for m in main:
        s=m.somme_des_point()
        if som_max< s:
            som_max=s
            Maillon_max=m
    return Maillon_max  

"""
fonction qui renvoie la somme des maillon d'une main
paramatire : 
    main : list des domino
renovie : 
    la somme des domino 

"""
def somme_de_points_main(main):
    s=0
    
    for m in main:
        s+=m.somme_des_point()

    return s  
"""
fonction qui suprimme un maillon m depuis main 
paramaitre :
    main : list des domino
    m : maillon 
renvoie main sans dominon m


"""
def  Supprimer_un_domino_de_la_main(main,m):
    j=0
    for m2 in main:
        if m2.domino_egale_domino(m):
            del main[j]
        j+=1

"""
fonction qui si on peut ajouter un domino a un main 
paramaitre :
    main : list des domino
    m : maillon 
renvoie true si les extrimite de la list (tete et queue ) on un phase ou plus
avec mm valeur que domino  phase 

"""            
def  si_il_peut_jouer(main,jue):
    t=jue.val_de_queque()
    q=jue.val_de_queque()
    for m in main:
        if m.si_val_in(t) or m.si_val_in(q) :
            return True
        
    return False
           
  #======================================================================================================      
  #======================================================================================================      
  #======================================================================================================      
  #======================================================================================================      
  #========================================                                    ==========================      
  #========================================        programe principal          =============================================      
  #========================================                                    ==========================      
  #======================================================================================================      
  #======================================================================================================      
  #======================================================================================================      
  #======================================================================================================      
        











d=creer_deux_mains()
main_joueur=d['main_joueur']

main_PC=d['main_PC']
le_reste_de_domino=d['le_reste_de_domino']
                                                                                                                                                                                                                                                                                                



'''
Recherche d'un morceau de dominos pour commencer à jouer 

'''


if rechercher_le_domino_double(main_joueur) :
    joueur=rechercher_le_domino_double_de_valeur_la_plus_elevee(main_joueur)

    if rechercher_le_domino_double(main_PC) :
        pc=rechercher_le_domino_double_de_valeur_la_plus_elevee(main_PC)
        if joueur.get_val_droite()>pc.get_val_droite():
            print("Le joueur est celui qui commence la pièce ",joueur)
            Le_joueur_qui_commence="joueur"
        else:
            print("l'ordinateur  est celui qui commence la pièce ",pc)
            Le_joueur_qui_commence="pc"

    else :
        print("Le joueur est celui qui commence la pièce ",joueur)
        Le_joueur_qui_commence="joueur"
else:
    
    if rechercher_le_domino_double(main_PC) :
        pc=rechercher_le_domino_double_de_valeur_la_plus_elevee(main_PC)
        print("l'ordinateur  est celui qui commence la pièce ",pc)
        Le_joueur_qui_commence="pc"
    else:
        m_som_max_joueur=Rechercher_la_piece_qui_a_le_plus_grand_somme_de_points(main_joueur)
        m_som_max_pc=Rechercher_la_piece_qui_a_le_plus_grand_somme_de_points(main_PC)
        som_max_joueur=m_som_max_joueur.get_val_droite()+m_som_max_joueur.get_val_gauche()
        som_max_pc=m_som_max_pc.get_val_droite()+m_som_max_pc.get_val_gauche()
        
        if som_max_joueur>som_max_pc:
            joueur=m_som_max_joueur
            print("Le joueur est celui qui commence la pièce ",joueur)
            Le_joueur_qui_commence="joueur"
        else:
            pc=m_som_max_pc
            print("l'ordinateur  est celui qui commence la pièce ",pc)
            Le_joueur_qui_commence="pc"

b=True  
nb_de_joue=1
pc_est_jouer=True
joueur_est_jouer=True
joue =Liste() 
'''
poure jouer la première domino
'''
print("/====================================/")
print("|   le jeu num 1:")
print("/====================================/")
"""
Si la plus grande pièce est à la main de l'ordinateur
"""
if Le_joueur_qui_commence=="pc":
    print("le tour de l'ordinateur':")
    

    joue.ajout_tete(pc)
    Supprimer_un_domino_de_la_main(main_PC,pc)
    
    #main_joueur=d['main_joueur']
    print("main_joueur")
    afiche_main_joueur(main_joueur)
    print("main_PC")
    #main_PC=d['main_PC']
    afiche_main_PC(main_PC)
    print("le_reste_de_domino")
    #le_reste_de_domino=d['le_reste_de_domino']
    afiche_main_PC(le_reste_de_domino)
    print("les domino qui jouer ")
    print(joue)
    suivant ="joueur"
    '''
     Si la plus grande pièce est à la main du jeoueur
    
    '''
else:
    print("le tour du joueur:")


    joue.ajout_tete(joueur)
    Supprimer_un_domino_de_la_main(main_joueur,joueur)
  #  main_joueur=d['main_joueur']
    print("main_joueur")
    afiche_main_joueur(main_joueur)
    print("main_PC")
   # main_PC=d['main_PC']
    afiche_main_joueur(main_PC)
    print("le_reste_de_domino")
    #le_reste_de_domino=d['le_reste_de_domino']
    afiche_main_joueur(le_reste_de_domino)
    print("les domino qui jouer ")
    print(joue)
    suivant ="pc"
nb_de_joue=1
b=True

while (main_joueur!=[] and main_PC!=[] and b) :
    input("Appuyez sur entre pour passer au tour suivant ")
    nb_de_joue+=1
    if suivant =="joueur":#Signifie que le joueur précédent est l'ordinteur
        
        
        print("/====================================/")
        print("|le tour de joueur","   le jeu num ",nb_de_joue,":")
        print("/====================================/")
    elif suivant =="pc":#Signifie que le joueur précédent est le joueur
                
        print("/====================================/")
        print("|le tour de l'ordinateur" ,"   le jeu num ",nb_de_joue,":")
        print("/====================================/")
    


        
    
    q=joue.val_de_queque()
    t=joue.val_de_tete()
    if q==t:# Si le dernier chiffre à droite est égal au dernier chiffre à gauche 
        '''
        Si le dernier chiffre à droite est égal au dernier chiffre à gauche 
        et le tour de joueur 
        '''  
    
        if suivant=="joueur":# #la prochain Tour
        
            suivant="pc"
            liste_des_juex_posible=[]
            """
            Si vous trouvez au moins un morceau qui peut être joué 
        
            """            
            if si_il_peut_jouer(main_joueur,joue):
                
                
                
                for m in  main_joueur:
                    if m.si_val_in(q) :
                        liste_des_juex_posible+=[m]
                        
                        
                """
                Si vous trouvez qu'un seul morceau peut être joué
    
                """                          
                if len(liste_des_juex_posible)==1:
                    joueur_est_jouer=True
                    joue.ajout_tete(liste_des_juex_posible[0])
                    Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[0])
                    joueur_est_jouer=True
                    
                else:
                    """
                    Si vous trouvez plusieur morceau domino peut être joué 
        
                    """  
                    cpt=0
                    for m in liste_des_juex_posible:
                        print(cpt,"=>",m)
                        cpt+=1
                    choix=int(input("Choisissez le numéro de domino :"))
                    joueur_est_jouer=True
                    joue.ajout_tete(liste_des_juex_posible[choix])
                    Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[choix])

            
            else:
                """
                S'il ne trouve pas une pièce, 
                nous trouvons un domino qui peut être joué, 
                nous devons choisir les pièces restantes 
                """
                if le_reste_de_domino==[]:
                    joueur_est_jouer=False
    
                else:
                    j=len(le_reste_de_domino)-1
                    ajout=True
                    while(j>-1 and ajout):
                        
                        m=le_reste_de_domino[j]
                        
                        if m.si_val_in(t):
                            joueur_est_jouer=True
                            joue.ajout_tete(m)
                            del le_reste_de_domino[j]
                            ajout=False
    
                        else:
                            main_joueur+=[m]
                            del le_reste_de_domino[j]
                        j-=1
                        
                    if ajout==True:
                        joueur_est_jouer=False



        else:
            """
            Si le dernier chiffre à droite est égal au dernier chiffre à gauche 
            et le tour de lordinateur
            """ 
            
            suivant="joueur"#la prochain Tour
            
            
    
                    

            liste_des_juex_posible=[]
            """
            Si vous trouvez au moins un morceau qui peut être joué 
            """
            if si_il_peut_jouer(main_PC,joue):
                

            
                for m in  main_PC:
                    if m.si_val_in(q) :
                        liste_des_juex_posible+=[m]
                """
                Si vous trouvez qu'un seul morceau peut être joué
    
                """  
                if len(liste_des_juex_posible)==1:
                    
                    
                    joue.ajout_tete(liste_des_juex_posible[0])
                    Supprimer_un_domino_de_la_main(main_PC,liste_des_juex_posible[0])
                    pc_est_jouer=True
                    """
                    Si vous trouvez plusieur morceau domino peut être joué 
        
                    """  
                else:
                    cpt=0
                    max_some_point=0
                    for m in liste_des_juex_posible:
                        if max_some_point<m.somme_des_point():
                            max_some_point=m.somme_des_point()
                            m_de_max=m
                    joue.ajout_tete(m_de_max)
                    Supprimer_un_domino_de_la_main(main_PC,m_de_max)
                    pc_est_jouer=True
                    

            else:
                """
                S'il ne trouve pas une pièce, 
                nous trouvons un domino qui peut être joué, 
                nous devons choisir les pièces restantes 
                """
                if le_reste_de_domino==[]:
                    pc_est_jouer=False
            
                else:
                    j=len(le_reste_de_domino)-1
                    ajout=True
                    while(j>-1 and ajout):
                        m=le_reste_de_domino[j]
                        
                        if m.si_val_in(t):
                            joue.ajout_tete(m)
                            del le_reste_de_domino[j]
                            ajout=False
                            pc_est_jouer=True

                        else:
                            main_PC+=[m]
                            del le_reste_de_domino[j]
                        j-=1
                        
                    if ajout==True:
                        pc_est_jouer=True
             

#####################################################################################################

    
    
    else:
                
        """
        Si le dernier chiffre à droite n'est égal pas  au dernier chiffre à gauche 
        et le tour de  joueur
        """ 
    
        if suivant=="joueur":
            suivant="pc"#la prochain Tour

            liste_des_juex_posible=[]
            """
            Si vous trouvez au moins un morceau qui peut être joué 
            """
            if si_il_peut_jouer(main_joueur,joue):
                for m in  main_joueur:
                    if m.si_val_in(q) or  m.si_val_in(t) :
                        liste_des_juex_posible+=[m]
                """
                Si vous trouvez qu'un seul morceau peut être joué
    
                """  
                if len(liste_des_juex_posible)==1:
                    if  liste_des_juex_posible[0].si_val_in(q) and  liste_des_juex_posible[0].si_val_in(t) :

                        """
                        Si la pièce peut être placée des deux côtés 
                        """
                        choix=int(input("Si vous souhaitez le placer à droite, appuyez sur 1 \nSi vous souhaitez le placer à gache, appuyez sur 2 "))
                        if choix==1:
                            joue.ajout_tete(liste_des_juex_posible[0])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[0])
                            joueur_est_jouer=True
                        if choix==2:
                            joue.ajout_queue(liste_des_juex_posible[0])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[0])
                            joueur_est_jouer=True
                            
 
                    
                    elif  liste_des_juex_posible[0].si_val_in(q)  :
                            joue.ajout_queue(liste_des_juex_posible[0])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[0])
                            joueur_est_jouer=True
                    elif  liste_des_juex_posible[0].si_val_in(t)  :

                            joue.ajout_tete(liste_des_juex_posible[0])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[0])
                            joueur_est_jouer=True


                        
                    


                else:
                    """
                    Si vous trouvez plusieur morceau domino peut être joué 
        
                    """  
                    cpt=0
                    for m in liste_des_juex_posible:
                        print(cpt,"=>",m)
                        cpt+=1
                    choix=int(input("Choisissez le numéro de domino "))
                    if  liste_des_juex_posible[choix].si_val_in(q) and  liste_des_juex_posible[choix].si_val_in(t) :
                        choix2=int(input("Si vous souhaitez le placer à droite, appuyez sur 1 \nSi vous souhaitez le placer à gache, appuyez sur 2 "))
                        if choix2==2:
                            joue.ajout_tete(liste_des_juex_posible[choix])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[choix])
                            joueur_est_jouer=True
                        if choix2==1:
                            joue.ajout_queue(liste_des_juex_posible[choix])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[choix])
                            joueur_est_jouer=True
                            
 
                    
                    elif  liste_des_juex_posible[choix].si_val_in(q)  :
                            joue.ajout_queue(liste_des_juex_posible[choix])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[choix])
                            joueur_est_jouer=True
                    elif  liste_des_juex_posible[choix].si_val_in(t)  :

                            joue.ajout_tete(liste_des_juex_posible[choix])
                            Supprimer_un_domino_de_la_main(main_joueur,liste_des_juex_posible[choix])
                            joueur_est_jouer=True
            else:
                """
                S'il ne trouve pas une pièce, 
                nous trouvons un domino qui peut être joué, 
                nous devons choisir les pièces restantes 
                """
            
                if le_reste_de_domino==[]:
                    joueur_est_jouer=False

                else:
                    
                    j=len(le_reste_de_domino)-1
                    ajout=True
                    while(j>-1 and ajout):
                        m=le_reste_de_domino[j]
                        if m.si_val_in(t) and m.si_val_in(q):
                                choix2=int(input("Si vous souhaitez le placer à droite, appuyez sur 1 Si vous souhaitez le placer à gache, appuyez sur 2 "))
                                if choix2==2:
                                    joue.ajout_tete(m)
                                    Supprimer_un_domino_de_la_main(main_joueur,m)
                                    joueur_est_jouer=True
                                if choix2==1:
                                    joue.ajout_queue(m)
                                    Supprimer_un_domino_de_la_main(main_joueur,m)
                                    joueur_est_jouer=True
                                ajout=False   
                        elif m.si_val_in(t):
                            joue.ajout_tete(m)
                            del le_reste_de_domino[j]
                            joueur_est_jouer=True
                            ajout=False
                            

                        elif m.si_val_in(q) :
                            joueur_est_jouer=True
                            joue.ajout_queue(m)
                            del le_reste_de_domino[j]
                            ajout=False
                            


                        else:
                            main_joueur+=[m]
                            del le_reste_de_domino[j]
                        j-=1
                    if ajout==True:
                        joueur_est_jouer=False

                    
        
        
        
        
        else:
            """
            Si le dernier chiffre à droite n'est égal pas  au dernier chiffre à gauche 
            et le tour de l'ordinateur 
            """ 
            suivant="joueur" #la prochain Tour
            
            liste_des_juex_posible=[]
            """
            Si vous trouvez au moins un morceau qui peut être joué 
            """
            if si_il_peut_jouer(main_PC,joue):
                
                
    
                
                for m in  main_PC:
                    if m.si_val_in(q) :
                        liste_des_juex_posible+=[m]
                """
                Si vous trouvez qu'un seul morceau peut être joué
    
                """  
                if len(liste_des_juex_posible)==1:

  
                 
                    if  liste_des_juex_posible[0].si_val_in(q)  :
                            pc_est_jouer=True
                            joue.ajout_queue(liste_des_juex_posible[0])
                            Supprimer_un_domino_de_la_main(main_PC,liste_des_juex_posible[0])
                    else :
                            """
                            Si vous trouvez plusieur morceau domino peut être joué 
                
                            """  


                            pc_est_jouer=True
                            joue.ajout_tete(liste_des_juex_posible[0])
                            Supprimer_un_domino_de_la_main(main_PC,liste_des_juex_posible[0])
    
    
    
    
    
    
                else:
                    cpt=0
                    max_some_point=0
                    for m in liste_des_juex_posible:
                        if max_some_point<m.somme_des_point():
                            max_some_point=m.somme_des_point()
                            m_de_max=m

                 
                    if  m_de_max.si_val_in(q)  :
                            joue.ajout_queue(m_de_max)
                            Supprimer_un_domino_de_la_main(main_PC,m_de_max)
                            pc_est_jouer=True
                    else :
    
                            joue.ajout_tete(m_de_max)
                            Supprimer_un_domino_de_la_main(main_PC,m_de_max)
                            pc_est_jouer=True
    
                
    
            else:
                """
                S'il ne trouve pas une pièce, 
                nous trouvons un domino qui peut être joué, 
                nous devons choisir les pièces restantes 
                """
            
            
                if le_reste_de_domino==[]:
                    pc_est_jouer=False
                else:
                    j=len(le_reste_de_domino)-1
                    ajout=True
                    while(j>-1 and ajout):
                        m=le_reste_de_domino[j]
                        
                        if m.si_val_in(t):
                            joue.ajout_tete(m)
                            del le_reste_de_domino[j]
                            ajout=False
                            pc_est_jouer=True
    
    
    
                        elif m.si_val_in(q):
                            joue.ajout_queue(m)
                            del le_reste_de_domino[j]
                            ajout=False
                            pc_est_jouer=True
                            
    
    
                        else:
                            main_PC+=[m]
                            del le_reste_de_domino[j]
                        j-=1
                    if ajout==True:
                        pc_est_jouer=False
    
    
    """
    S'il n'est pas possible de jouer pour l'ordinateur et le joueur
    doit être arrêtée 
    """
    if pc_est_jouer==False and joueur_est_jouer==False:
        b=False
    print("-  la main de joueur ")
    if main_joueur==[]:
        print("vide")
    else:
        
        afiche_main_joueur(main_joueur)
    print("- a main de l'ordinateur  ")
    if main_PC==[]:
        print("vide")
    else:
        afiche_main_PC(main_PC)
    print("- le reste de domino ")
    if le_reste_de_domino==[]:
        print("vide")
    else:
        
        afiche_main_PC(le_reste_de_domino)
    print(" - Pièces qui ont été jouées  ")
    print(joue)
    

somme_des_point_de_joueur=somme_de_points_main(main_joueur)
somme_des_point_de_lordinateur=somme_de_points_main(main_PC)




if b :
    if main_joueur==[]:
        print("Le joueur est le gagnant et le nombre total de points est  : ",somme_des_point_de_lordinateur)
        
    if main_PC==[]:
        print("L'ordinateur est le gagnant et le total des points est :",somme_des_point_de_joueur)
else:
    if somme_des_point_de_joueur<somme_des_point_de_lordinateur:
        print("Le joueur est le gagnant et le nombre total de points est  : ",somme_des_point_de_lordinateur)
    elif somme_des_point_de_joueur>somme_des_point_de_lordinateur:
        print("L'ordinateur est le gagnant et le total des points est:",somme_des_point_de_joueur)
        
    else :
        print("Le résultat est équivalent  ",somme_des_point_de_joueur,":",somme_des_point_de_lordinateur)
        
        


        
        
        
        
        
        
