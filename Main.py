import pygame
import sys
import os
from pygame.locals import *
import time
from Shuffle import *
from Player import *
from PIL import Image


pygame.init() 
gameKoz=None
Deck =Deck()
Players=[]
Players.append(Player('Player1'))
Players.append(Player('Player2'))
Players.append(Player('Player3'))
Players.append(Player('Player4'))

Deck.shuffle()
for value in range(0,13):      
    Players[0].addtoList(Deck.deal(value*4))    
    Players[1].addtoList(Deck.deal(value*4+1))
    Players[2].addtoList(Deck.deal(value*4+2))
    Players[3].addtoList(Deck.deal(value*4+3)) 
showCard=[1,1,1,1,1,1,1,1,1,1,1,1,1]
def taking(card_number):
    if(showCard[card_number]==1):
        showCard[card_number]=0        
    return "This is an instance method."
Players[0].sort()
Players[1].sort()
Players[2].sort()
Players[3].sort()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 650))
pygame.mouse.set_visible(1)
pygame.display.set_caption('Trump-king game')
color = (0, 145, 0)
screen.fill(color)
pygame.display.flip()

Font=pygame.font.SysFont('timesnewroman',  26)
FontSuits=pygame.font.SysFont('timesnewroman',  22) 

white=(255, 255, 255)
black=(0, 0, 0)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
done=False 

Hand=Font.render("Offer time", False, black, white)

player1=Font.render("Player 1", False, black, white)
player2=Font.render("Player 2", False, black, white)
player3=Font.render("Player 3", False, black, white)
player4=Font.render("You", False, black, white)
offer1=Font.render("-", False, black, white)
offer2=Font.render("-", False, black, white)
offer3=Font.render("-", False, black, white)
offer4=Font.render("-", False, black, white)
offerPas=Font.render("pas", False, black, white)
offer5=Font.render("5 ", False, black, white)
offer6=Font.render("6 ", False, black, white)
offer7=Font.render("7 ", False, black, white)
offer8=Font.render("8 ", False, black, white)
offer9=Font.render("9 ", False, black, white)
offer10=Font.render("10", False, black, white)
offer11=Font.render("11", False, black, white)
offer12=Font.render("12", False, black, white)
offer13=Font.render("13", False, black, white)

cardSuit0=FontSuits.render("Club", False, black, white)
cardSuit1=FontSuits.render("Spade", False, black, white)
cardSuit2=FontSuits.render("Heart", False, black, white)
cardSuit3=FontSuits.render("Diamond", False, black, white)

player1Point=FontSuits.render("", False, black, white)
player2Point=FontSuits.render("", False, black, white)
player3Point=FontSuits.render("", False, black, white)
player4Point=FontSuits.render("", False, black, white)

taking1=Font.render("take 0", False, black, white)
taking2=Font.render("take 0", False, black, white)
taking3=Font.render("take 0", False, black, white)
taking4=Font.render("take 0", False, black, white)

textinput = " "
#adding cards to screen
DEFAULT_IMAGE_SIZE = (58, 83) 

unshowCard = pygame.image.load("./images/BACK.png").convert()
unshowCard = pygame.transform.scale(unshowCard, DEFAULT_IMAGE_SIZE)

middleCard = pygame.image.load("./images/JOKER-1.svg").convert()
middleCard = pygame.transform.scale(middleCard, DEFAULT_IMAGE_SIZE)

cards=[]
cardBil0=[]
cardBil1=[]
cardBil2=[]
for i in range(0,13):
    cards.append(Players[3].cardlist[i].image)
    cardBil0.append(Players[0].cardlist[i].image)
    cardBil1.append(Players[1].cardlist[i].image)
    cardBil2.append(Players[2].cardlist[i].image)
playCards=[]  
for i in range(0,4):
    playCards.append(middleCard)  


x = 30; # x coordnate of image
y = 460; # y coordinate of image
pygame.display.flip()

text = Font.render('quit' , True , white)
screen.blit(cards[0], ( x,y)) # paint to screen
screen.blit(cards[1], ( x+65,y)) # paint to screen
screen.blit(cards[2], ( x+130,y)) # paint to screen
screen.blit(cards[3], ( x+195,y)) # paint to screen
screen.blit(cards[4], ( x+260,y)) # paint to screen
screen.blit(cards[5], ( x+325,y)) # paint to screen
screen.blit(cards[6], ( x+390,y)) # paint to screen
screen.blit(cards[7], ( x+455,y)) # paint to screen
screen.blit(cards[8], ( x+520,y)) # paint to screen
screen.blit(cards[9], ( x+585,y)) # paint to screen
screen.blit(cards[10], ( x+650,y)) # paint to screen
screen.blit(cards[11], ( x+715,y)) # paint to screen
screen.blit(cards[12], ( x+780,y)) # paint to screen 

screen.blit(playCards[0], ( 220,190)) # paint to screen
screen.blit(playCards[1], ( 400,65)) # paint to screen
screen.blit(playCards[2], ( 600,190)) # paint to screen
screen.blit(playCards[3], ( 400,310)) # paint to screen

check=False
playerGame=False
timer=0

game=True
gameControl=False
playable=[False,False,False,False]
firstHand=True

offer=True
pasControl=True

bid=True
doIt=False
bigOffer=0
bidCounter=[1,1,1,1]
gameOrders=[-1,-1,-1,-1]
gamePoints=[0,0,0,0]
gameOrder=-1
calculateNmbr=0

whoTake=-1

handCard=[None,None,None,None]    
handNumber=0 
firstPlayer=-1
koz_oynandi_mi=False
hander=0
def bidCalculater():
    counter=0
    for i in range(len(bidCounter)):
        if(bidCounter[i]==0):
            counter+=1
    if counter==3:
        return 1
    elif counter==4:
        return 0 
    return -1   
def next_turn(player_turn):
    player_turn += 1
    if player_turn == 4:
        player_turn = 0
    return player_turn   
def koz_var_mi(list,koz):
    for i in range(len(list)):
        if list[i].suit.name==koz:
            return True
    return False   
def koz_atildi_mi(list,koz):
    for i in range(len(list))    :
        if list[i].suit.name==koz:
            return True
    return False    
def calculateHand():
    global koz_oynandi_mi
    global firstPlayer
    global handCard
    global hander
    global fileWriterHand
    
    strs="game"+str(hander)+".txt"
    hander+=1
    fileWriterHand(strs,handCard)
    for i in range(4):
        playCards[i]=middleCard
        playable[i]=False
    if koz_oynandi_mi==False:
        koz_oynandi_mi = koz_var_mi(handCard,gameKoz)   
    control=koz_atildi_mi(handCard,gameKoz)
    toWho=-1
    bigOne=0
    if control:
        for i in range(4):
            if handCard[i].suit.name==gameKoz and handCard[i].value>bigOne:
                bigOne=handCard[i].value
                toWho=i
    else:
        toWho=firstPlayer
        bigOne=handCard[firstPlayer].value
        for i in range(4):
            if handCard[firstPlayer].suit.name==handCard[i].suit.name and handCard[i].value>bigOne:
                bigOne=handCard[i].value
                toWho=i           
    handCard=[None,None,None,None]   
    pygame.time.delay(400)    
    nmbr=random.randint(0,3)  
    firstPlayer=toWho
    gamePoints[toWho]+=1
    if toWho==0:
        taking1=Font.render("take "+str(gamePoints[0]), False, black, white)        
    elif toWho==1:  
        taking2=Font.render("take "+str(gamePoints[1]), False, black, white)        
    elif toWho==2:
        taking3=Font.render("take "+str(gamePoints[2]), False, black, white)        
    else:   
        taking4=Font.render("take "+str(gamePoints[3]), False, black, white)      
        
    playable[toWho]=True 
    Players[toWho].addPoint()
    print("hand")
def returner():
    print("player 0")
    Players[0].returnList()  
    print("player 1")
    Players[1].returnList()
    print("player 2")
    Players[2].returnList()
def fileWriter(fileName,list1,list2,list3,list4):
        file = open(fileName,"w")
        for i in range(13):
            file.write(". player 1  kartlari:\n")
            file.write(list1[i].suit.name+" "+str(list1[i].value)+"\n")
        for i in range(13):
            file.write(". player 2  kartlari:\n")
            file.write(list2[i].suit.name+" "+str(list2[i].value)+"\n")
        for i in range(13):
            file.write(". player 3  kartlari:\n")
            file.write(list3[i].suit.name+" "+str(list3[i].value)+"\n")
        for i in range(13):
            file.write(". user  kartlari:\n")
            file.write(list4[i].suit.name+" "+str(list4[i].value)+"\n")           
            file.write("\n")  
        file.close()     
def fileWriterHand(fileName,list1):
        file = open(fileName,"w")
        for i in range(4):
            file.write(". game  kartlari:\n")
            file.write(list1[i].suit.name+" "+str(list1[i].value)+"\n")
                
            file.write("\n")  
        file.close()             

#--------------------------------------------------------                 
while True:            
    clock.tick(60)   
    
    
    if(bid and playerGame):
        nmbr=Players[0].giveOffer(bigOffer)
        check=0
        if(nmbr>bigOffer and bidCounter[0]!=0):
            offer1=Font.render(str(nmbr), False, black, white)
            bigOffer=nmbr
            check=0
            bidCounter[0]=nmbr
        else:   
            offer1=Font.render("00", False, black, white) 
            bidCounter[0]=0
          
        nmbr=Players[1].giveOffer(bigOffer)
        if(nmbr>bigOffer and bidCounter[1]!=0):            
            offer2=Font.render(str(nmbr), False, black, white)
            bigOffer=nmbr
            bidCounter[1]=nmbr
        else:   
            offer2=Font.render("00", False, black, white)     
            bidCounter[1]=0     
        nmbr=Players[0].giveOffer(bigOffer)
        if(nmbr>bigOffer and bidCounter[2]!=0):
            offer3=Font.render(str(nmbr), False, black, white)
            bigOffer=nmbr 
            bidCounter[2]=nmbr     
        else:   
            offer3=Font.render("00", False, black, white)       
            bidCounter[2]=0
        if  pasControl:   
            playerGame=False
        doIt=False
    if bid and bidCalculater()==1:        
        bid=False
    elif bid and bidCalculater()==0:        
        bid=False
        Hand=Font.render("Game Time koz= "+str(gameKoz), False, black, white)
        offer4=Font.render("4", False, black, white)
    
    if bid==False and firstHand: 
        returner()
        fileWriter("cards.txt",Players[0].cardlist,Players[1].cardlist,Players[2].cardlist,Players[3].cardlist,)
        start=-1   
        for i in range(len(bidCounter)):
            if bidCounter[i]!=0:
                gameKoz=Players[i].returnKoz()
                whoTake=i
                playable[i]=True
                firstPlayer=i
                Hand=Font.render("Game Time koz= "+str(gameKoz), False, black, white)
                start=i
        gameOrder=start        
        for i in range(len(gameOrders)):
            gameOrders[i]=(start+i)%4       
        firstHand=False
    if game and bid==False:
        if(calculateNmbr==4):
            handNumber+=1
            calculateHand()
            calculateNmbr=0


        for i in range(3): 
            if handNumber==13:
                break           
            if playable[i]:
                pygame.time.delay(400)    
                handCard[i]=Players[i].giveCard(gameKoz,handCard,koz_oynandi_mi,calculateNmbr,i)
                playCards[i]=handCard[i].image
                
                playable[i+1]=True 
                playable[i]=False                 
                calculateNmbr+=1               
                break             
                          
        gameControl=False
        #game=False   


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()   
        if event.type == pygame.KEYDOWN:
            if check==True:
                if event.type == pygame.K_BACKSPACE:
                    textSurface=textSurface[:-1]
                else:    
                    textSurface+=event.unicode
    screen.blit(Hand, (10, 10))
    screen.blit(player1Point, (10, 40))
    screen.blit(player2Point, (10, 70))
    screen.blit(player3Point, (10, 100))
    screen.blit(player4Point, (10, 130))        
    
    taking1=Font.render("take "+str(gamePoints[0]), False, black, white)      
    taking2=Font.render("take "+str(gamePoints[1]), False, black, white)    
    taking3=Font.render("take "+str(gamePoints[2]), False, black, white)       
    taking4=Font.render("take "+str(gamePoints[3]), False, black, white)

    screen.blit(player1, (10, 280))
    screen.blit(offer1, (5, 315))
    screen.blit(taking1, (30, 315))
    
    screen.blit(player2, (360, 10))
    screen.blit(offer2, (455, 10))
    screen.blit(taking2, (480, 10))
    
    screen.blit(player3, (790, 280))
    screen.blit(offer3, (785 , 315 ))
    screen.blit(taking3, (810, 315)) 

    screen.blit(player4, (430, 609))           
    screen.blit(offer4, (395 , 574 ))  
    screen.blit(taking4, (425, 574))

    screen.blit(offerPas, (573, 410))
    screen.blit(offer5, (615, 410))
    screen.blit(offer6, (640, 410))
    screen.blit(offer7, (665, 410))
    screen.blit(offer8, (690, 410))
    screen.blit(offer9, (715, 410))
    screen.blit(offer10, (740, 410))
    screen.blit(offer11, (770, 410))
    screen.blit(offer12, (800, 410))
    screen.blit(offer13, (830, 410))   

    screen.blit(cardSuit0, (280, 410))
    screen.blit(cardSuit1, (335, 410))
    screen.blit(cardSuit2, (400, 410))
    screen.blit(cardSuit3, (460, 410))


    
    font = pygame.font.SysFont("Consolas", 55)    
    
    if showCard[0]==0:
        screen.blit(unshowCard, ( x,y)) # paint to screen
    if showCard[1]==0:    
        screen.blit(unshowCard, ( x+65,y)) # paint to screen
    if showCard[2]==0:    
        screen.blit(unshowCard, ( x+130,y)) # paint to screen
    if showCard[3]==0:    
        screen.blit(unshowCard, ( x+195,y)) # paint to screen
    if showCard[4]==0:
        screen.blit(unshowCard, ( x+260,y)) # paint to screen
    if showCard[5]==0:
        screen.blit(unshowCard, ( x+325,y)) # paint to screen
    if showCard[6]==0:
        screen.blit(unshowCard, ( x+390,y)) # paint to screen
    if showCard[7]==0:
        screen.blit(unshowCard, ( x+455,y)) # paint to screen
    if showCard[8]==0:
        screen.blit(unshowCard, ( x+520,y)) # paint to screen
    if showCard[9]==0:
        screen.blit(unshowCard, ( x+585,y)) # paint to screen
    if showCard[10]==0:
        screen.blit(unshowCard, ( x+650,y)) # paint to screen
    if showCard[11]==0:
        screen.blit(unshowCard, ( x+715,y)) # paint to screen
    if showCard[12]==0:
        screen.blit(unshowCard, ( x+780,y)) # paint to screen 

    screen.blit(playCards[0], ( 220,190)) # paint to screen
    screen.blit(playCards[1], ( 400,65)) # paint to screen
    screen.blit(playCards[2], ( 600,190)) # paint to screen
    screen.blit(playCards[3], ( 400,310)) # paint to screen    
     
    
       
    if event.type == pygame.MOUSEBUTTONDOWN:            
            if x <= mouse[0] <= x+58 and y <= mouse[1] <= y+83:
                handCard[3]=Players[3].cardlist[0]
                playCards[3]=cards[0]  
                gameControl=True
                playable[0]=True
                calculateNmbr+=1 
                taking(0)  
            elif x+65 <= mouse[0] <= x+123 and y <= mouse[1] <= y+83:
                handCard[3]=Players[3].cardlist[1]
                playCards[3]=cards[1]  
                gameControl=True     
                playable[0]=True   
                calculateNmbr+=1             
                taking(1) 
            elif x+130 <= mouse[0] <= x+188 and y <= mouse[1] <= y+83:   
                handCard[3]=Players[3].cardlist[2]
                playCards[3]=cards[2]  
                gameControl=True   
                playable[0]=True  
                calculateNmbr+=1             
                taking(2) 
            elif x+195 <= mouse[0] <= x+253 and y <= mouse[1] <= y+83: 
                handCard[3]=Players[3].cardlist[3]
                playCards[3]=cards[3]  
                gameControl=True           
                playable[0]=True 
                calculateNmbr+=1        
                taking(3) 
            elif x+260 <= mouse[0] <= x+318 and y <= mouse[1] <= y+83:
                handCard[3]=Players[3].cardlist[4]
                playCards[3]=cards[4]  
                gameControl=True      
                playable[0]=True   
                calculateNmbr+=1            
                taking(4) 
            elif x+325 <= mouse[0] <= x+383 and y <= mouse[1] <= y+83:
                handCard[3]=Players[3].cardlist[5]
                playCards[3]=cards[5] 
                gameControl=True   
                playable[0]=True 
                calculateNmbr+=1                 
                taking(5) 
            elif x+390 <= mouse[0] <= x+448 and y <= mouse[1] <= y+83: 
                handCard[3]=Players[3].cardlist[6]
                playCards[3]=cards[6]  
                gameControl=True    
                playable[0]=True     
                calculateNmbr+=1           
                taking(6) 
            elif x+455 <= mouse[0] <= x+513 and y <= mouse[1] <= y+83:   
                handCard[3]=Players[3].cardlist[7]
                playCards[3]=cards[7] 
                gameControl=True   
                playable[0]=True  
                calculateNmbr+=1              
                taking(7) 
            elif x+520 <= mouse[0] <= x+578 and y <= mouse[1] <= y+83:
                handCard[3]=Players[3].cardlist[8]
                playCards[3]=cards[8]  
                gameControl=True     
                playable[0]=True      
                calculateNmbr+=1          
                taking(8) 
            elif x+585 <= mouse[0] <= x+643 and y <= mouse[1] <= y+83:   
                handCard[3]=Players[3].cardlist[9]
                playCards[3]=cards[9]    
                gameControl=True   
                playable[0]=True   
                calculateNmbr+=1          
                taking(9) 
            elif x+670 <= mouse[0] <= x+708 and y <= mouse[1] <= y+83:
                handCard[3]=Players[3].cardlist[10]
                playCards[3]=cards[10]  
                gameControl=True     
                playable[0]=True   
                calculateNmbr+=1             
                taking(10)              
            elif x+715 <= mouse[0] <= x+773 and y <= mouse[1] <= y+83: 
                handCard[3]=Players[3].cardlist[11]
                playCards[3]=cards[11]
                gameControl=True     
                playable[0]=True    
                calculateNmbr+=1             
                taking(11) 
            elif x+780 <= mouse[0] <= x+838 and y <= mouse[1] <= y+83:
                handCard[3]=Players[3].cardlist[12]
                playCards[3]=cards[12]  
                gameControl=True  
                playable[0]=True     
                calculateNmbr+=1              
                taking(12) 
            elif 573 <= mouse[0] <= 610 and 410 <= mouse[1] <= 439 :   #pas
                doIt=True
                bigOffer=0
                offer=False
                pasControl=False
                bidCounter[3]=0
                offer4=Font.render("p", False, black, white)
            elif 615 <= mouse[0] <= 635 and 410 <= mouse[1] <= 439:  #5
                doIt=True
                bigOffer=5
                bidCounter[3]=6
                offer4=Font.render("5", False, black, white)       
            elif 640 <= mouse[0] <= 660 and 410 <= mouse[1] <= 439:  #6
                doIt=True
                bigOffer=6
                bidCounter[3]=6
                offer4=Font.render("6", False, black, white)
            elif 665 <= mouse[0] <= 685 and 410 <= mouse[1] <= 439:  #7
                doIt=True
                bigOffer=7
                bidCounter[3]=7
                offer4=Font.render("7", False, black, white)
            elif 690 <= mouse[0] <= 710 and 410 <= mouse[1] <= 439:  #8
                doIt=True
                bigOffer=8
                bidCounter[3]=8
                offer4=Font.render("8", False, black, white)                                                         
            elif 715 <= mouse[0] <= 735 and 410 <= mouse[1] <= 439:  #9
                doIt=True
                bigOffer=9
                bidCounter[3]=9
                offer4=Font.render("9", False, black, white) 
            elif 740 <= mouse[0] <= 765 and 410 <= mouse[1] <= 439:  #10
                doIt=True
                bigOffer=10
                bidCounter[3]=10
                offer4=Font.render("10", False, black, white)    
            elif 770 <= mouse[0] <= 795 and 410 <= mouse[1] <= 439:  #11
                doIt=True
                bigOffer=11
                bidCounter[3]=11
                offer4=Font.render("11", False, black, white)
            elif 800 <= mouse[0] <= 825 and 410 <= mouse[1] <= 439:  #12
                doIt=True
                bigOffer=12
                bidCounter[3]=12
                offer4=Font.render("12", False, black, white)
            elif 830 <= mouse[0] <= 855 and 410 <= mouse[1] <= 439:  #13
                doIt=True
                bigOffer=13
                bidCounter[3]=13
                offer4=Font.render("13", False, black, white) 
            elif 280 <= mouse[0] <= 325 and 410 <= mouse[1] <= 435:  #club
                Players[3].addKoz("CLUB")
                gameKoz="CLUB"
            elif 335 <= mouse[0] <= 390 and 410 <= mouse[1] <= 435:  #Spade
                Players[3].addKoz("SPADE")  
                gameKoz="SPADE"    
            elif 400 <= mouse[0] <= 450 and 410 <= mouse[1] <= 435:  #heart
                Players[3].addKoz("HEART")
                gameKoz="HEART"
            elif 460 <= mouse[0] <= 560 and 410 <= mouse[1] <= 435:  #diamond
                Players[3].addKoz("DIAMOND")  
                gameKoz="DIAMOND"     
    if event.type == pygame.MOUSEBUTTONUP and doIt and bid:
        playerGame=True
    #if event.type == pygame.MOUSEBUTTONUP and  gameControl:
     #   game=True    
    if handNumber==13:
        game=False
        player1Point=Font.render("player1 take: "+str(Players[0].returnPoint()), False, black, white)
        player2Point=Font.render("player2 take: "+str(Players[1].returnPoint()), False, black, white)
        player3Point=Font.render("player3 take: "+str(Players[2].returnPoint()), False, black, white)
        player4Point=Font.render("player4 take: "+str(Players[3].returnPoint()), False, black, white)
        if whoTake==0 and Players[0].returnPoint()>bigOffer+2:
            player1Point=Font.render("player1 take: "+str(-bigOffer), False, black, white)
        elif whoTake==0 and Players[0].returnPoint()<bigOffer:
            player1Point=Font.render("player1 take: "+str(-bigOffer), False, black, white)    
        elif whoTake==1 and Players[1].returnPoint()>bigOffer+2:
            player2Point=Font.render("player2 take: "+str(-bigOffer), False, black, white)
        elif whoTake==1 and Players[1].returnPoint()<bigOffer:
            player2Point=Font.render("player2 take: "+str(-bigOffer), False, black, white)    
        elif whoTake==2 and Players[2].returnPoint()>bigOffer+2:
            player3Point=Font.render("player3 take: "+str(-bigOffer), False, black, white)
        elif whoTake==2 and Players[2].returnPoint()<bigOffer:
            player3Point=Font.render("player3 take: "+str(-bigOffer), False, black, white)    
        elif Players[3].returnPoint()>bigOffer+2:
            player4Point=Font.render("user take: "+str(-bigOffer), False, black, white)   
        elif Players[3].returnPoint()< bigOffer:
            player4Point=Font.render("user take: "+str(-bigOffer), False, black, white)                   


      
    mouse = pygame.mouse.get_pos()   

    pygame.display.update()