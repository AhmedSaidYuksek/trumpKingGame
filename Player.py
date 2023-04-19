import pygame
from Shuffle import *
import itertools
import math
def returner(str):
    if str=='CLUB':
        return 0
    elif str=='SPADE':
        return 1
    elif str=='HEART':
        return 2
    elif str=='DIAMOND':
        return 3
def faktoriyel(i):
    if i==1 or i==0:       
        return 1    
    else: 
        return i * faktoriyel(i-1)    
def koz_atildi_mi(list,koz):
    firstOne=True
    for i in range(len(list)):
        if list[i]!=None and list[i].suit.name==koz:
            if firstOne:
                return False
            return True
        else:
            firstOne=False 
    return False    
def max_utility_fun(list,cardList,nmbr):
    newOne=[]
    for i in range(len(list)) :
        newOne.append(0)
    for i in range(len(list)) :
        if list[i].value==14:
            newOne[i]==-1
        else:    
            for j in range (list[i].value,13):
                if cardList[nmbr][j]==1:
                    newOne[i]==-1
    returnValue=-1
    for i in range(len(newOne)) :
        if newOne[i]==-1:
            returnValue=i
    return returnValue        
                

class Player:
    name= None    
    point=0
    kozValue=""
    def __init__(self,name):
        self.name=name
        self.point=0
        self.cardlist = []
        self.numberHand = [0,0,0,0]
        self.kozAtildi = [False,False,False,False]
        self.cardInfo =[[0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.myCard  =[[0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0]]
    def addtoList(self, Card):
        if Card.suit.name=='CLUB':
            self.cardInfo[0][Card.value-2]=1
            self.myCard[0][Card.value-2]=1
        elif Card.suit.name=='SPADE':
            self.cardInfo[1][Card.value-2]=1
            self.myCard[1][Card.value-2]=1
        elif Card.suit.name=='HEART':
            self.cardInfo[2][Card.value-2]=1
            self.myCard[2][Card.value-2]=1
        elif Card.suit.name=='DIAMOND':
            self.cardInfo[3][Card.value-2]=1 
            self.myCard[3][Card.value-2]=1   
        self.cardlist.append(Card)  
    def addtoInfoList(self, Card):
        if Card.suit.name=='CLUB':
            self.cardInfo[0][Card.value-2]=1
        elif Card.suit.name=='SPADE':
            self.cardInfo[1][Card.value-2]=1
        elif Card.suit.name=='HEART':
            self.cardInfo[2][Card.value-2]=1
        elif Card.suit.name=='DIAMOND':
            self.cardInfo[3][Card.value-2]=1  
    def removetoList(self,Card):
        self.cardlist.remove(Card) 
    def returnKoz(self):
        return self.kozValue 
    def addKoz(self,koz):
        self.kozValue=str(koz)       
    def play(self,nmbr):
        return self.cardlist.pop(nmbr)
    def sort(self):
        self.cardlist.sort(key=lambda x: x.cost, reverse=True)
    def addPoint(self):
        self.point+=1   
    def returnPoint(self):
        return self.point   
    def returnList(self):    
        for i in range(13):
            print(self.cardlist[i].suit," - ",self.cardlist[i].value)
    def giveOffer(self,sayi):
        returnValue=0
        koz=-1
        card=[0,0,0,0]
        konum=[-1,-1,-1,-1]        
        for i in range(13):
            if self.cardlist[i].suit.name=='CLUB':
                card[0]+=1
                if konum[0]==-1:
                    konum[0]=i
            elif self.cardlist[i].suit.name=='SPADE':
                card[1]+=1
                if konum[1]==-1:
                    konum[1]=i
            elif self.cardlist[i].suit.name=='HEART':
                card[2]+=1
                if konum[2]==-1:
                    konum[2]=i 
            elif self.cardlist[i].suit.name=='DIAMOND':
                card[3]+=1 
                if konum[3]==-1:
                    konum[3]=i                 
        for i in range(4):
            maxValue=0
            if card[i]>=4:                
                if self.cardlist[konum[i]].value==14 and self.cardlist[konum[i]+1].value==13 and self.cardlist[konum[i]+2].value==12 :
                    maxValue+=card[i]#ilk3 ya da 4 fark etmez                    
                elif self.cardlist[konum[i]].value==14 and self.cardlist[konum[i]+1].value==13 and self.cardlist[konum[i]+2].value==11 :
                    if card[i]>=7:#ilk 2 ve j kizin cikma olasiligine gore hesaplandi                        
                        maxValue+=card[i]  
                    else:
                        maxValue+=card[i]-1
                elif self.cardlist[konum[i]].value==14 and self.cardlist[konum[i]+1].value==12 and self.cardlist[konum[i]+2].value==11 :
                    if card[i]>=11:#iki kart disarda ise %33 ihtimal ile birinde iki kart ayni anda var alinabilir risk                         
                        maxValue+=card[i]  
                    else:#diger türlü 3 kart disarda olsa bile %55 ihtimal ile birinde k ve bir kart daha var 1 el kaybedilebilir
                        maxValue+=card[i]-1 
                elif self.cardlist[konum[i]].value==13 and self.cardlist[konum[i]+1].value==12 and self.cardlist[konum[i]+2].value==11 :                                          
                    maxValue+=card[i]-1  #as yok bir el kesin verilir diger olasilik 4 kartin olması ile ayni
                elif self.cardlist[konum[i]].value==14 and self.cardlist[konum[i]+1].value==13 :
                    if card[i]>=9:  #el sayisi daha dusuk ise birinin elinde kiz ile beraber iki kart daha olma ihtimali artiyor                      
                        maxValue+=card[i]  
                    else:
                        maxValue+=card[i]-1
                elif self.cardlist[konum[i]].value==14 and self.cardlist[konum[i]+1].value==12 :
                    if card[i]>=9:#el kaybetmez
                        maxValue+=card[i]
                    elif self.cardlist[konum[i]+2].value==11 or self.cardlist[konum[i]+1].value==10:                     
                        maxValue+=card[i]-1  #bir tane kaybedebilir
                    elif card[i]>=7:  
                        maxValue+=card[i]-1        
                elif self.cardlist[konum[i]].value==13 and self.cardlist[konum[i]+1].value==12 :
                    #bastan 1 kart verir kalan muhtemel 9 kart icin hesaplarsak
                    #13-4(herkesin en az bir el alabilecegini dusunsek) kalan 9 kartin en az 4u bizim 
                    # 5 karti da rakiplere dagitirsak buyuk olasilikla 2-2-1 veya 3-1-1 seklinde dagilir bu da bir elin k ile alma anlamina gelir
                    # kalan 5 kartin en az 3u bizim kalan kartlarin da birinde toplanmis olma ihtimali %50 alinabilir bir risk dagildigini kabul edersek
                    #bu elde de q ile almasina denk gelir onun icin tek bir kart fedasi ile cozulecegini kabul ediyot
                    maxValue+=card[i]-1                     
                elif self.cardlist[konum[i]].value==12 and self.cardlist[konum[i]+1].value==11 :  #%50 sans ile 
                    if card[i]>=9:# %50 sans ile  dagilmistir alinabilir risk 11 icin 
                         # birinin elinde iki buyuk kartin da olabilirligi 10 icin %33 alinabilir ihtimal
                         # # birinin elinde iki buyuk kartin ayni anda da olabilirligi 9 icin %28 alinabilir ihtimal                       
                        maxValue+=card[i]-1 
                    elif card[i]>=5 and self.cardlist[konum[i]+2].value==10 :#iki el kaybedip gerisini alabilir en buyuk 3 kart olacagiicin 
                        maxValue+=card[i]-2  
                    else:#  daha kucuk durumlarda hesaplama buyuk olasılıkla girmemenin mantikli hala geldigi haldedir 
                        maxValue+=0
                elif card[i]>=7:
                    mmbr= int(math.ceil(float(card[i])/3))
                    maxValue+=card[i]-mmbr #oyuncunun bir kart destesinden çok karti varsa bir sekilde cok kart almasini bekliyoruz
                if maxValue>0:        
                    for j in range(1,4): 
                        if card[(i+j)%4]>=3:
                            if self.cardlist[konum[(i+1)%4]].value==14 and self.cardlist[konum[(i+1)%4]+1].value==13 and self.cardlist[konum[(i+1)%4]+2].value==12 :
                               maxValue+=3 
                            elif self.cardlist[konum[(i+1)%4]].value==14 and self.cardlist[konum[(i+1)%4]+1].value==13:
                               maxValue+=2   
                            elif self.cardlist[konum[(i+1)%4]].value==14 and self.cardlist[konum[(i+1)%4]+1].value==12:
                               maxValue+=2  
                            elif self.cardlist[konum[(i+1)%4]].value==13 and self.cardlist[konum[(i+1)%4]+1].value==12:
                               maxValue+=2  
                            elif self.cardlist[konum[(i+1)%4]].value==14 or self.cardlist[konum[(i+1)%4]].value==13 or self.cardlist[konum[(i+1)%4]].value==12:
                               maxValue+=1 
                        elif card[(i+j)%4]==2:
                            if self.cardlist[konum[(i+1)%4]].value==14 and self.cardlist[konum[(i+1)%4]+1].value==13 :
                               maxValue+=2 
                            elif self.cardlist[konum[(i+1)%4]].value==14 :
                               maxValue+=1  
                            elif self.cardlist[konum[(i+1)%4]].value==13 and self.cardlist[konum[(i+1)%4]+1].value==12 :
                               maxValue+=1                                                          
                        elif card[(i+j)%4]==1:
                            if self.cardlist[konum[(i+1)%4]].value==14 :
                               maxValue+=1
            if maxValue>returnValue:
                returnValue=maxValue                   
                koz=i
            maxValue=0    
        print("--------------------") 
        if koz !=-1:
            if koz==0:
               self.kozValue= "CLUB"
            elif koz==1:
               self.kozValue= "SPADE"
            elif koz==2:
               self.kozValue= "HEART"
            else:   
              self.kozValue=  "DIAMOND"     

        if(returnValue<4 or returnValue<sayi):
            returnValue=0
        elif  returnValue-sayi>=3:   
            returnValue-=1
         
        return returnValue
    
    def giveCard(self,koz,list,koz_atildi,hand_nmbr,player_number):
        for i in range(len(list)):
            if list[i]!=None:
                if list[i].suit.name=='CLUB':
                    self.cardInfo[0][list[i].value-2]=1
                elif list[i].suit.name=='SPADE':
                    self.cardInfo[1][list[i].value-2]=1
                elif list[i].suit.name=='HEART':
                    self.cardInfo[2][list[i].value-2]=1
                elif list[i].suit.name=='DIAMOND':
                    self.cardInfo[3][list[i].value-2]=1
        
        lookNumber=player_number-hand_nmbr         
        if lookNumber<-1:
            lookNumber+=4
        played_fun =0.0  
        risk_fun =0.0
        utility_fun  =0.0        
        return_fun=[]
        for i in range(len(self.cardlist)):
             
            if self.numberHand[returner(self.cardlist[i].suit.name)]>=3 or self.kozAtildi[returner(self.cardlist[i].suit.name)]:
                played_fun=0
            else:
                played_fun=1  
            numberCard=13
            for j in range(13):
                numberCard-=self.cardInfo[returner(self.cardlist[i].suit.name)][j]     
            if numberCard<3:
                risk_fun=1
            else:    #((numbercard/3)*3!+3^(numbercard-3)) /3^numbercard           
                nmbr=(3+3*(2**numberCard-1))/3**numberCard                
                risk_fun=1-nmbr
            utility_fun_list=[]
            for j in range(self.cardlist[i].value,13):                
                if self.cardInfo[returner(self.cardlist[i].suit.name)][j]!=1 or self.myCard[returner(self.cardlist[i].suit.name)][j]==1 :
                    utility_fun_list.append(j)    
            utility_fun_list.sort()
            if len(utility_fun_list )==0:
                utility_fun=1      
            elif  len(utility_fun_list )==1:
                if self.myCard[returner(self.cardlist[i].suit.name)][utility_fun_list[0]]==1: 
                    utility_fun=1
            else:
                cardNmbr=0
                others=0
                for kart in range(len(utility_fun_list)):
                    if self.myCard[returner(self.cardlist[i].suit.name)][utility_fun_list[kart]]==1:
                        cardNmbr+=1
                    else:
                        others+=1
                if cardNmbr==len(utility_fun_list):
                    utility_fun=1
                elif self.myCard[returner(self.cardlist[i].suit.name)][utility_fun_list[0]]==1:
                    utility_fun=0
                else:
                    if others==2 and len(utility_fun_list)>=3:
                        utility_fun=0.55+0.11*(len(utility_fun_list)-3)
                    elif others==1 and len(utility_fun_list)>=3: 
                        utility_fun=1 
                    else: #olasilik kucuk
                        utility_fun= (cardNmbr)/(len(utility_fun_list)*10)    
            if returner(self.cardlist[i].suit.name)!=returner(koz):   
                return_fun.append((utility_fun*risk_fun)*played_fun)  
            else:
                just=False
                for kart in range(len(self.cardlist)):
                    if self.cardlist[i].suit.name!=koz:
                        just==True
                if just:
                    return_fun.append(0)
                else:            
                    return_fun.append(((utility_fun*risk_fun)*played_fun)-0.0001)    

        if list[lookNumber]==None:
            maxReturn=-1
            maxReturnIndex=-1
            if koz_atildi:
                for i in range(len(self.cardlist)):
                    
                    if maxReturn<=return_fun[i]:
                        maxReturn=return_fun[i]
                        maxReturnIndex=i
            else:
                for i in range(len(self.cardlist)):
                    if returner(self.cardlist[i].suit.name)!=returner(koz):
                        if maxReturn<=return_fun[i]:
                            maxReturn=return_fun[i]
                            maxReturnIndex=i  
            card=self.cardlist[maxReturnIndex]
            self.cardlist.remove(self.cardlist[maxReturnIndex])
            return card
        club = []
        spade = []
        heart = []
        diamond = []
        firstCard=None
        for i in range(len(self.cardlist)):
            if self.cardlist[i].suit.name=='CLUB':
                club.append(self.cardlist[i])
            elif self.cardlist[i].suit.name=='SPADE':
                spade.append(self.cardlist[i])
            elif self.cardlist[i].suit.name=='HEART':
                heart.append(self.cardlist[i]) 
            elif self.cardlist[i].suit.name=='DIAMOND':
                diamond.append(self.cardlist[i])  
        if list[lookNumber].suit.name=='CLUB':
            self.numberHand[0]+=1
            koz_control=koz_atildi_mi(list,koz)
            if koz_control:
                koz_control[0]=True
            if len(club)>=1:                
                if koz_control and list[lookNumber].suit.name!=koz:
                    card=club[len(club)-1]
                    self.cardlist.remove(club[len(club)-1])    
                    return card     
                else:
                    bigOne=0
                    for kart in range(len(list)):
                        if list[kart]!=None and list[kart].suit.name=='CLUB' and list[kart].value>bigOne:
                            bigOne=list[kart].value
                    if club[0].value<bigOne:
                        card=club[len(club)-1]
                        self.cardlist.remove(club[len(club)-1])
                        return card
                    else:                        
                        nmbr=max_utility_fun(club,self.cardInfo,0)
                        if nmbr!=-1:
                            card=club[nmbr]
                            self.cardlist.remove(club[nmbr])
                            return card
                        else:
                            returnValue=0
                            for i in range(len(club)):
                                if club[i].value>bigOne:
                                    returnValue=i
                            card=club[returnValue]
                            self.cardlist.remove(club[returnValue])
                            return card    
            elif koz=='SPADE':  
                    if len(spade)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='SPADE' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(club)):
                                if spade[i].value>max_koz:
                                    returnValue=i

                            card=spade[returnValue]
                            self.cardlist.remove(spade[returnValue])
                            return card
                        else:
                            card=spade[len(spade)-1]
                            self.cardlist.remove(spade[len(spade)-1])
                            return card    
            elif koz=='HEART':
                    if len(heart)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='HEART' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(heart)):
                                if heart[i].value>max_koz:
                                    returnValue=i

                            card=heart[returnValue]
                            self.cardlist.remove(heart[returnValue])
                            return card
                        else:
                            card=heart[len(heart)-1]
                            self.cardlist.remove(heart[len(spade)-1])
                            return card        
            elif koz=='DIAMOND':
                    if len(diamond)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='DIAMOND' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(diamond)):
                                if diamond[i].value>max_koz:
                                    returnValue=i

                            card=diamond[returnValue]
                            self.cardlist.remove(diamond[returnValue])
                            return card
                        else:
                            card=diamond[len(spade)-1]
                            self.cardlist.remove(diamond[len(diamond )-1])
                            return card        
        elif list[lookNumber].suit.name=='SPADE': 
            self.numberHand[1]+=1           
            koz_control=koz_atildi_mi(list,koz)
            if koz_control:
                koz_control[1]=True
            if len(spade)>=1:
                if koz_control and list[lookNumber].suit.name!=koz:
                    card=spade[len(spade)-1]
                    self.cardlist.remove(spade[len(spade)-1])
                    return card     
                else:
                    bigOne=0                    
                    for kart in range(len(list)):
                        if list[kart]!=None and list[kart].suit.name=='SPADE' and list[kart].value>bigOne:
                            bigOne=list[kart].value
                    if spade[0].value<bigOne:
                        card=spade[len(spade)-1]
                        self.cardlist.remove(spade[len(spade)-1])
                        return card
                    else:
                        nmbr=max_utility_fun(spade,self.cardInfo,0)
                        if nmbr!=-1:
                            card=spade[nmbr]
                            self.cardlist.remove(spade[nmbr])
                            return card
                        else:
                            returnValue=0
                            for i in range(len(spade)):
                                if spade[i].value>bigOne:
                                    returnValue=i
                            card=spade[returnValue]
                            self.cardlist.remove(spade[returnValue])
                            return card    
            elif koz=='CLUB':
                    if len(club)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='CLUB' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(club)):
                                if club[i].value>max_koz:
                                    returnValue=i

                            card=club[returnValue]
                            self.cardlist.remove(club[returnValue])
                            return card
                        else:
                            card=club[len(club)-1]
                            self.cardlist.remove(club[len(club)-1])
                            return card    
            elif koz=='HEART':
                    if len(heart)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='HEART' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(heart)):
                                if heart[i].value>max_koz:
                                    returnValue=i

                            card=heart[returnValue]
                            self.cardlist.remove(heart[returnValue])
                            return card
                        else:
                            card=heart[len(heart)-1]
                            self.cardlist.remove(heart[len(spade)-1])
                            return card        
            elif koz=='DIAMOND':
                    if len(diamond)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='DIAMOND' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(diamond)):
                                if diamond[i].value>max_koz:
                                    returnValue=i

                            card=diamond[returnValue]
                            self.cardlist.remove(diamond[returnValue])
                            return card
                        else:
                            card=diamond[len(diamond)-1]
                            self.cardlist.remove(diamond[len(diamond)-1])
                            return card           
        elif list[lookNumber].suit.name=='HEART' : 
            self.numberHand[2]+=1           
            koz_control=koz_atildi_mi(list,koz)
            if koz_control:
                koz_control[2]=True
            if len(heart)>=1:
                if koz_control and list[lookNumber].suit.name!=koz :
                    card=heart[len(heart)-1]
                    self.cardlist.remove(heart[len(heart)-1])
                    return card     
                else:
                    bigOne=0                    
                    for kart in range(len(list)):
                        if list[kart]!=None and list[kart].suit.name=='HEART' and list[kart].value>bigOne:
                            bigOne=list[kart].value
                    if heart[0].value<bigOne:
                        card=heart[len(heart)-1]
                        self.cardlist.remove(heart[len(heart)-1])
                        return card
                    else:
                        nmbr=max_utility_fun(heart,self.cardInfo,0)
                        if nmbr!=-1:
                            card=heart[nmbr]
                            self.cardlist.remove(heart[nmbr])
                            return card
                        else:
                            returnValue=0
                            for i in range(len(heart)):
                                if heart[i].value>bigOne:
                                    returnValue=i
                            card=heart[returnValue]
                            self.cardlist.remove(heart[returnValue])
                            return card    
            elif koz=='CLUB':
                    if len(club)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='CLUB' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(club)):
                                if club[i].value>max_koz:
                                    returnValue=i

                            card=club[returnValue]
                            self.cardlist.remove(club[returnValue])
                            return card
                        else:
                            card=club[len(club)-1]
                            self.cardlist.remove(club[len(club)-1])
                            return card    
            elif koz=='SPADE':
                    if len(spade)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='SPADE' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(spade)):
                                if spade[i].value>max_koz:
                                    returnValue=i

                            card=spade[returnValue]
                            self.cardlist.remove(spade[returnValue])
                            return card
                        else:
                            card=spade[len(spade)-1]
                            self.cardlist.remove(spade[len(spade)-1])
                            return card        
            elif koz=='DIAMOND':
                    if len(diamond)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='DIAMOND' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(diamond)):
                                if diamond[i].value>max_koz:
                                    returnValue=i

                            card=diamond[returnValue]
                            self.cardlist.remove(diamond[returnValue])
                            return card
                        else:
                            card=diamond[len(diamond)-1]
                            self.cardlist.remove(diamond[len(diamond)-1])
                            return card             
        elif list[lookNumber].suit.name=='DIAMOND':
            self.numberHand[3]+=1
            koz_control=koz_atildi_mi(list,koz)
            if koz_control:
                koz_control[3]=True
            if len(diamond)>=1:
                if koz_control and list[lookNumber].suit.name!=koz:
                    card=diamond[len(diamond)-1]
                    self.cardlist.remove(diamond[len(diamond)-1])
                    return card     
                else:
                    bigOne=0                    
                    for kart in range(len(list)):
                        if list[kart]!=None and list[kart].suit.name=='DIAMOND' and list[kart].value>bigOne:
                            bigOne=list[kart].value
                    if diamond[0].value<bigOne:
                        card=diamond[len(diamond)-1]
                        self.cardlist.remove(diamond[len(diamond)-1])
                        return card
                    else:
                        nmbr=max_utility_fun(diamond,self.cardInfo,0)
                        if nmbr!=-1:
                            card=diamond[nmbr]
                            self.cardlist.remove(diamond[nmbr])
                            return card
                        else:
                            returnValue=0
                            for i in range(len(diamond)):
                                if diamond[i].value>bigOne:
                                    returnValue=i
                            card=diamond[returnValue]
                            self.cardlist.remove(diamond[returnValue])
                            return card    
            elif koz=='CLUB':
                    if len(club)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='CLUB' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(club)):
                                if club[i].value>max_koz:
                                    returnValue=i

                            card=club[returnValue]
                            self.cardlist.remove(club[returnValue])
                            return card
                        else:
                            card=club[len(club)-1]
                            self.cardlist.remove(club[len(club)-1])
                            return card    
            elif koz=='HEART':
                    if len(heart)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='HEART' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(heart)):
                                if heart[i].value>max_koz:
                                    returnValue=i

                            card=heart[returnValue]
                            self.cardlist.remove(heart[returnValue])
                            return card
                        else:
                            card=heart[len(heart)-1]
                            self.cardlist.remove(heart[len(heart)-1])
                            return card        
            elif koz=='SPADE':
                    if len(spade)>=1:
                        if koz_control:
                            max_koz=0
                            for i in range(len(list)):
                                if list[i]!=None and list[i].suit.name=='SPADE' and list[i].value>max_koz:
                                    max_koz=list[i].value
                            returnValue=0
                            for i in range(len(spade)):
                                if spade[i].value>max_koz:
                                    returnValue=i

                            card=spade[returnValue]
                            self.cardlist.remove(spade[returnValue])
                            return card
                        else:
                            card=spade[len(spade)-1]
                            self.cardlist.remove(spade[len(spade)-1])
                            return card              
        taking=[0,0,0,0]
        for i in range(4):
            for j in range(13):
                taking[0]+=self.cardInfo[i][j]
        if len(club)==0:
            taking[0]=-1
        if len(spade)==0:
            taking[1]=-1
        if len(heart)==0:
            taking[2]=-1
        if len(diamond)==0:
            taking[3]=-1       
        big=taking[3]
        returnI=3
        for i in range (3)  :
            if taking[i]>big:
                big=taking[i]
                returnI=i
        if returnI==0:
            card=club[len(club)-1]
            self.cardlist.remove(club[len(club)-1])
            return card
        elif returnI==1:
            card=spade[len(spade)-1]
            self.cardlist.remove(spade[len(spade)-1])
            return card
        elif returnI==2:
            card=heart[len(heart)-1]
            self.cardlist.remove(heart[len(heart)-1])
            return card
        else :       
            card=diamond[len(diamond)-1]
            self.cardlist.remove(diamond[len(diamond)-1])
            return card