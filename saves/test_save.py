import pygame
import sys
from random import randint, choice

pygame.init()
screen = pygame.display.set_mode([1200,776])
pygame.display.set_caption("Poker")
icon = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\chip.jpeg")
pygame.display.set_icon(icon)

font = pygame.font.SysFont("arialblack", 25)
font2 = pygame.font.SysFont("arialblack", 18)


tisch = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\Tisch.jpeg")

kreuz_Ass_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz Ass.jpeg")
kreuz_König_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz König.jpeg")
kreuz_Dame_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz Dame.jpeg")
kreuz_Bube_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz Bube.jpeg")
kreuz_10_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 10.jpeg")
kreuz_9_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 9.jpeg")
kreuz_8_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 8.jpeg")
kreuz_7_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 7.jpeg")
kreuz_6_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 6.jpeg")
kreuz_5_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 5.jpeg")
kreuz_4_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 4.jpeg")
kreuz_3_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 3.jpeg")
kreuz_2_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\kreuz 2.jpeg")

piek_Ass_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek Ass.jpeg")
piek_König_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek König.jpeg")
piek_Dame_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek Dame.jpeg")
piek_Bube_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek Bube.jpeg")
piek_10_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 10.jpeg")
piek_9_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 9.jpeg")
piek_8_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 8.jpeg")
piek_7_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 7.jpeg")
piek_6_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 6.jpeg")
piek_5_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 5.jpeg")
piek_4_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 4.jpeg")
piek_3_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 3.jpeg")
piek_2_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\piek 2.jpeg")

herz_Ass_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz Ass.jpeg")
herz_König_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz König.jpeg")
herz_Dame_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz Dame.jpeg")
herz_Bube_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz Bube.jpeg")
herz_10_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 10.jpeg")
herz_9_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 9.jpeg")
herz_8_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 8.jpeg")
herz_7_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 7.jpeg")
herz_6_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 6.jpeg")
herz_5_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 5.jpeg")
herz_4_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 4.jpeg")
herz_3_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 3.jpeg")
herz_2_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\herz 2.jpeg")

caro_Ass_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro Ass.jpeg")
caro_König_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro König.jpeg")
caro_Dame_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro Dame.jpeg")
caro_Bube_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro Bube.jpeg")
caro_10_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 10.jpeg")
caro_9_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 9.jpeg")
caro_8_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 8.jpeg")
caro_7_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 7.jpeg")
caro_6_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 6.jpeg")
caro_5_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 5.jpeg")
caro_4_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 4.jpeg")
caro_3_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 3.jpeg")
caro_2_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\caro 2.jpeg")

karte_geschlossen_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\karte_geschlossen.jpeg")

dealer_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\dealer.jpeg")
chip_b = pygame.image.load("C:\\Users\\Aaron\\Desktop\\Poker\\nicht originale\\chip.jpeg")

class Karte :
    def __init__(self, bild, name, farbe) :
        self.bild = bild
        self.name = name 
        self.farbe = farbe
        self.x = 0
        self.y = 671

kreuz_Ass = Karte(kreuz_Ass_b, 14, 4)
kreuz_König = Karte(kreuz_König_b, 13, 4)
kreuz_Dame = Karte(kreuz_Dame_b, 12, 4)
kreuz_Bube = Karte(kreuz_Bube_b, 11, 4)
kreuz_10 = Karte(kreuz_10_b, 10, 4)
kreuz_9 = Karte(kreuz_9_b, 9, 4)
kreuz_8 = Karte(kreuz_8_b, 8, 4)
kreuz_7 = Karte(kreuz_7_b, 7, 4)
kreuz_6 = Karte(kreuz_6_b, 6, 4)
kreuz_5 = Karte(kreuz_5_b, 5, 4)
kreuz_4 = Karte(kreuz_4_b, 4, 4)
kreuz_3 = Karte(kreuz_3_b, 3, 4)
kreuz_2 = Karte(kreuz_2_b, 2, 4)

piek_Ass = Karte(piek_Ass_b, 14, 3)
piek_König = Karte(piek_König_b, 13, 3)
piek_Dame = Karte(piek_Dame_b, 12, 3)
piek_Bube = Karte(piek_Bube_b, 11, 3)
piek_10 = Karte(piek_10_b, 10, 3)
piek_9 = Karte(piek_9_b, 9, 3)
piek_8 = Karte(piek_8_b, 8, 3)
piek_7 = Karte(piek_7_b, 7, 3)
piek_6 = Karte(piek_6_b, 6, 3)
piek_5 = Karte(piek_5_b, 5, 3)
piek_4 = Karte(piek_4_b, 4, 3)
piek_3 = Karte(piek_3_b, 3, 3)
piek_2 = Karte(piek_2_b, 2, 3)

herz_Ass = Karte(herz_Ass_b, 14, 2)
herz_König = Karte(herz_König_b, 13, 2)
herz_Dame = Karte(herz_Dame_b, 12, 2)
herz_Bube = Karte(herz_Bube_b, 11, 2)
herz_10 = Karte(herz_10_b, 10, 2)
herz_9 = Karte(herz_9_b, 9, 2)
herz_8 = Karte(herz_8_b, 8, 2)
herz_7 = Karte(herz_7_b, 7, 2)
herz_6 = Karte(herz_6_b, 6, 2)
herz_5 = Karte(herz_5_b, 5, 2)
herz_4 = Karte(herz_4_b, 4, 2)
herz_3 = Karte(herz_3_b, 3, 2)
herz_2 = Karte(herz_2_b, 2, 2)

caro_Ass = Karte(caro_Ass_b, 14, 1)
caro_König = Karte(caro_König_b, 13, 1)
caro_Dame = Karte(caro_Dame_b, 12, 1)
caro_Bube = Karte(caro_Bube_b, 11, 1)
caro_10 = Karte(caro_10_b, 10, 1)
caro_9 = Karte(caro_9_b, 9, 1)
caro_8 = Karte(caro_8_b, 8, 1)
caro_7 = Karte(caro_7_b, 7, 1)
caro_6 = Karte(caro_6_b, 6, 1)
caro_5 = Karte(caro_5_b, 5, 1)
caro_4 = Karte(caro_4_b, 4, 1)
caro_3 = Karte(caro_3_b, 3, 1)
caro_2 = Karte(caro_2_b, 2, 1)

karten = [kreuz_Ass, kreuz_König, kreuz_Dame, kreuz_Bube, kreuz_10, kreuz_9, kreuz_8, kreuz_7, kreuz_6, kreuz_5, kreuz_4, kreuz_3, kreuz_2, piek_Ass, piek_König, piek_Dame, piek_Bube, piek_10, piek_9, piek_8, piek_7, piek_6, piek_5, piek_4, piek_3, piek_2, herz_Ass, herz_König, herz_Dame, herz_Bube, herz_10, herz_9, herz_8, herz_7, herz_6, herz_5, herz_4, herz_3, herz_2, caro_Ass, caro_König, caro_Dame, caro_Bube, caro_10, caro_9, caro_8, caro_7, caro_6, caro_5, caro_4, caro_3, caro_2]

def textObjekt(text, font, farbe) :
    textFlaeche = font.render(text, True, farbe)
    return textFlaeche, textFlaeche.get_rect()


anzahl_spieler = 1
farbe_plus = (50, 50, 50)
farbe_minus = (50, 50, 50)
farbe_ende = (50, 50, 50)

zeit = 0
zählen = False
klicken = True

go = True
while go :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: sys.exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN :
        pos1 = pygame.mouse.get_pos()

        if klicken :
            if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 70 and pos1[1] < 120 and anzahl_spieler < 10 :
                anzahl_spieler += 1 
                klicken = False
                zählen = True
            elif pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 120 and pos1[1] < 170 and anzahl_spieler > 1 :
                anzahl_spieler -= 1 
                klicken = False
                zählen = True
            elif pos1[0] > 700 and pos1[0] < 800 and pos1[1] > 70 and pos1[1] < 170 :
                pygame.time.wait(200)
                go = False

    pos1 = pygame.mouse.get_pos()
    
    if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 70 and pos1[1] < 120 :
        farbe_plus = (125, 125, 125)
    else :
        farbe_plus = (50, 50, 50)

    if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 120 and pos1[1] < 170 :
        farbe_minus = (125, 125, 125)
    else :
        farbe_minus = (50, 50, 50)

    if pos1[0] > 700 and pos1[0] < 800 and pos1[1] > 70 and pos1[1] < 170 :
        farbe_ende = (125, 125, 125)
    else :
        farbe_ende = (50, 50, 50)

    textGrund,textKasten = textObjekt("Wie viele seid ihr?",font,(255,255,255))
    textKasten.center = ((600, 40))
    screen.blit(textGrund,textKasten)

    pygame.draw.rect(screen, (35, 35, 35), (550, 70, 100, 100))
    pygame.draw.rect(screen, farbe_plus, (625, 70, 25, 50))
    pygame.draw.rect(screen, farbe_minus, (625, 120, 25, 50))
    pygame.draw.line(screen, (100, 100, 100), (625, 120), (649, 120), 2)
    pygame.draw.rect(screen, farbe_ende, (700, 70, 100, 100))

    textGrund2,textKasten2 = textObjekt(str(anzahl_spieler), font,(255,255,255))
    textKasten2.center = ((580, 115))
    screen.blit(textGrund2,textKasten2)

    textGrund3,textKasten3 = textObjekt("+", font,(255,255,255))
    textKasten3.center = ((637, 95))
    screen.blit(textGrund3,textKasten3)

    textGrund4,textKasten4 = textObjekt("-", font,(255,255,255))
    textKasten4.center = ((637, 140))
    screen.blit(textGrund4,textKasten4)

    textGrund5,textKasten5 = textObjekt("weiter", font,(255,255,255))
    textKasten5.center = ((750, 120))
    screen.blit(textGrund5,textKasten5)

    pygame.display.update()

    if zählen :
        zeit += 1 

    if zeit >= 300 :
        zeit = 0 
        zählen = False
        klicken = True

farbe_plus = (50, 50, 50)
farbe_minus = (50, 50, 50)
farbe_ende = (50, 50, 50)

zeit = 0
zählen = False
klicken = True 

if anzahl_spieler == 1 :
    ki_min = 1
else :
    ki_min = 0

anzahl_ki = ki_min

screen.fill((0, 0, 0))

go = True
while go :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN :
        pos1 = pygame.mouse.get_pos()

        if klicken :
            if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 70 and pos1[1] < 120 and anzahl_ki < 9 :
                anzahl_ki += 1 
                klicken = False
                zählen = True
            elif pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 120 and pos1[1] < 170 and anzahl_ki > ki_min :
                anzahl_ki -= 1 
                klicken = False
                zählen = True
            elif pos1[0] > 700 and pos1[0] < 800 and pos1[1] > 70 and pos1[1] < 170 :
                pygame.time.wait(200)
                go = False

    pos1 = pygame.mouse.get_pos()
    
    if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 70 and pos1[1] < 120 :
        farbe_plus = (125, 125, 125)
    else :
        farbe_plus = (50, 50, 50)

    if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 120 and pos1[1] < 170 :
        farbe_minus = (125, 125, 125)
    else :
        farbe_minus = (50, 50, 50)

    if pos1[0] > 700 and pos1[0] < 800 and pos1[1] > 70 and pos1[1] < 170 :
        farbe_ende = (125, 125, 125)
    else :
        farbe_ende = (50, 50, 50)

    textGrund,textKasten = textObjekt("Mit wie vielen Kis wollt ihr spielen?", font,(255,255,255))
    textKasten.center = ((600, 40))
    screen.blit(textGrund,textKasten)

    pygame.draw.rect(screen, (35, 35, 35), (550, 70, 100, 100))
    pygame.draw.rect(screen, farbe_plus, (625, 70, 25, 50))
    pygame.draw.rect(screen, farbe_minus, (625, 120, 25, 50))
    pygame.draw.line(screen, (100, 100, 100), (625, 120), (649, 120), 2)
    pygame.draw.rect(screen, farbe_ende, (700, 70, 100, 100))

    textGrund2,textKasten2 = textObjekt(str(anzahl_ki), font,(255,255,255))
    textKasten2.center = ((580, 115))
    screen.blit(textGrund2,textKasten2)

    textGrund3,textKasten3 = textObjekt("+", font,(255,255,255))
    textKasten3.center = ((637, 95))
    screen.blit(textGrund3,textKasten3)

    textGrund4,textKasten4 = textObjekt("-", font,(255,255,255))
    textKasten4.center = ((637, 140))
    screen.blit(textGrund4,textKasten4)

    textGrund5,textKasten5 = textObjekt("weiter", font,(255,255,255))
    textKasten5.center = ((750, 120))
    screen.blit(textGrund5,textKasten5)

    pygame.display.update()

    if zählen :
        zeit += 1 

    if zeit >= 300 :
        zeit = 0 
        zählen = False
        klicken = True

geld_menge = 100
farbe_plus = (50, 50, 50)
farbe_minus = (50, 50, 50)
farbe_ende = (50, 50, 50)

zeit = 0
zählen = False
klicken = True

screen.fill((0,0,0))

go = True
while go :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: sys.exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN :
        pos1 = pygame.mouse.get_pos()

        if klicken :
            if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 70 and pos1[1] < 120 and geld_menge < 10000 :
                geld_menge += 100
                klicken = False
                zählen = True
            elif pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 120 and pos1[1] < 170 and geld_menge > 100 :
                geld_menge -= 100
                klicken = False
                zählen = True
            elif pos1[0] > 700 and pos1[0] < 800 and pos1[1] > 70 and pos1[1] < 170 :
                pygame.time.wait(200)
                go = False

    pos1 = pygame.mouse.get_pos()
    
    if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 70 and pos1[1] < 120 :
        farbe_plus = (125, 125, 125)
    else :
        farbe_plus = (50, 50, 50)

    if pos1[0] > 625 and pos1[0] < 650 and pos1[1] > 120 and pos1[1] < 170 :
        farbe_minus = (125, 125, 125)
    else :
        farbe_minus = (50, 50, 50)

    if pos1[0] > 700 and pos1[0] < 800 and pos1[1] > 70 and pos1[1] < 170 :
        farbe_ende = (125, 125, 125)
    else :
        farbe_ende = (50, 50, 50)

    textGrund,textKasten = textObjekt("Mit wie viel wollt ihr anfangen?", font,(255,255,255))
    textKasten.center = ((600, 40))
    screen.blit(textGrund,textKasten)

    pygame.draw.rect(screen, (35, 35, 35), (550, 70, 100, 100))
    pygame.draw.rect(screen, farbe_plus, (625, 70, 25, 50))
    pygame.draw.rect(screen, farbe_minus, (625, 120, 25, 50))
    pygame.draw.line(screen, (100, 100, 100), (625, 120), (649, 120), 2)
    pygame.draw.rect(screen, farbe_ende, (700, 70, 100, 100))

    textGrund2,textKasten2 = textObjekt(str(geld_menge), font,(255,255,255))
    textKasten2.center = ((580, 115))
    screen.blit(textGrund2,textKasten2)

    textGrund3,textKasten3 = textObjekt("+", font,(255,255,255))
    textKasten3.center = ((637, 95))
    screen.blit(textGrund3,textKasten3)

    textGrund4,textKasten4 = textObjekt("-", font,(255,255,255))
    textKasten4.center = ((637, 140))
    screen.blit(textGrund4,textKasten4)

    textGrund5,textKasten5 = textObjekt("weiter", font,(255,255,255))
    textKasten5.center = ((750, 120))
    screen.blit(textGrund5,textKasten5)

    pygame.display.update()

    if zählen :
        zeit += 1 

    if zeit >= 300 :
        zeit = 0 
        zählen = False
        klicken = True

screen.fill((0,0,0))

class Kombination :
    def __init__(self, wert, karten_menge, höhe) :
        self.wert = wert
        self.karten_menge = karten_menge
        self.höhe = höhe

class Paar(Kombination) :
    def __init__(self, wert) :
        Kombination.__init__(self, wert, 2, 1)

class zwei_Paare(Kombination) :
    def __init__(self, wert, wert2) :
        Kombination.__init__(self, wert, 4, 2)
        self.wert2 = wert2

class Drilling(Kombination) :
    def __init__(self, wert) :
        Kombination.__init__(self, wert, 3, 3)

class Strasse(Kombination) :
    def __init__(self, wert) :
        Kombination.__init__(self, wert, 5, 4)

class Flush(Kombination) :
    def __init__(self, wert, wert2, wert3, wert4, wert5) :
        Kombination.__init__(self, wert, 5, 5)
        self.wert2 = wert2
        self.wert3 = wert3
        self.wert4 = wert4
        self.wert5 = wert5

class Full_House(Kombination) :
    def __init__(self, wert, wert2) :
        Kombination.__init__(self, wert, 5, 6)
        self.wert2 = wert2

class Vierling(Kombination) :
    def __init__(self, wert) :
        Kombination.__init__(self, wert, 4, 7)

class Straight_Flush(Kombination) :
    def __init__(self, wert) :
        Kombination.__init__(self, wert, 5, 8)

class Royal_Flush(Kombination) :
    def __init__(self) :
        Kombination.__init__(self, None, 5, 9)

class Spieler :
    def __init__(self, geld, farbe, gesetzt, setzen) :
        self.geld = geld
        self.farbe = farbe
        self.gesetzt = gesetzt
        self.setzen = setzen 
        self.gesetzt2 = 0
        self.g = 0 
        self.schreiben = False
        self.imSpiel = True
        self.war_dran = False
        self.war_dealer = False
        self.karte = None
        self.blatt = []
        self.kerten2 = []
        self.benutzt = []
        self.art = "spieler"

    def spieler_zeichnen(self) :
        screen.blit(self.blatt[0].bild, feld1)
        screen.blit(self.blatt[1].bild, feld2)

        if self.geld > geboten :
            if self.schreiben :
                pygame.draw.rect(screen, (180, 0, 0), (900, 700, 100, 50))
                pygame.draw.rect(screen, (0, 0, 0), (900, 700, 100, 50), 1)
                pygame.draw.line(screen, (0, 0, 0), (910, 740), (990, 740))    
            else :
                pygame.draw.rect(screen, (120, 0, 0), (900, 700, 100, 50))
                pygame.draw.rect(screen, (0, 0, 0), (900, 700, 100, 50), 1)
                pygame.draw.line(screen, (0, 0, 0), (910, 740), (990, 740))

            textGrund,textKasten = textObjekt(str(self.setzen), font, (0, 0, 0))
            textKasten.center = (950, 725)
            screen.blit(textGrund,textKasten)

        pos1 = pygame.mouse.get_pos()
        if pos1[0] > 1010 and pos1[0] < 1100 and pos1[1] > 700 and pos1[1] < 750 :
            pygame.draw.rect(screen, (150, 0, 0), (1010, 700, 90, 50))
        else :
            pygame.draw.rect(screen, (100, 0, 0), (1010, 700, 90, 50))

        textGrund,textKasten = textObjekt("all in", font2, (0, 0, 0))
        textKasten.center = (1055, 725)
        screen.blit(textGrund,textKasten)

        if self.geld > geboten :
            pos1 = pygame.mouse.get_pos()
            if pos1[0] > 790 and pos1[0] < 890 and pos1[1] > 700 and pos1[1] < 750 :
                pygame.draw.rect(screen, (150, 0, 0), (790, 700, 100, 50))
            else :
                pygame.draw.rect(screen, (100, 0, 0), (790, 700, 100, 50))

            if geboten <= self.gesetzt :
                pygame.draw.rect(screen, (50, 50, 50), (790, 700, 100, 50))

            textGrund,textKasten = textObjekt("go along", font2, (0, 0, 0))
            textKasten.center = (840, 725)
            screen.blit(textGrund,textKasten)

        pos1 = pygame.mouse.get_pos()
        if pos1[0] > 680 and pos1[0] < 780 and pos1[1] > 700 and pos1[1] < 750 :
            pygame.draw.rect(screen, (150, 0, 0), (680, 700, 100, 50))
        else :
            pygame.draw.rect(screen, (100, 0, 0), (680, 700, 100, 50))

        if geboten == self.gesetzt :
            textGrund,textKasten = textObjekt("ckeck", font2, (0, 0, 0))
            textKasten.center = (730, 725)
            screen.blit(textGrund,textKasten)
        else :
            textGrund,textKasten = textObjekt("fold", font2, (0, 0, 0))
            textKasten.center = (730, 725)
            screen.blit(textGrund,textKasten)

        if self.geld > geboten :
            pos1 = pygame.mouse.get_pos()
            if pos1[0] > 1110 and pos1[0] < 1190 and pos1[1] > 700 and pos1[1] < 750 :
                pygame.draw.rect(screen, (150, 0, 0), (1110, 700, 80, 50))
            else :
                pygame.draw.rect(screen, (100, 0, 0), (1110, 700, 80, 50))

            if self.setzen == "0" :
                pygame.draw.rect(screen, (50, 50, 50), (1110, 700, 80, 50))

            textGrund,textKasten = textObjekt("bet", font2, (0, 0, 0))
            textKasten.center = (1150, 725)
            screen.blit(textGrund,textKasten)

        textGrund,textKasten = textObjekt(str(pott), font, (0, 0, 0))
        textKasten.center = (600, 200)
        screen.blit(textGrund,textKasten)

        screen.blit(chip_b, (650,180))


    def mausklick(self) :
        global amZug
        global geboten
        global pott

        pos1 = pygame.mouse.get_pos()
        if pos1[0] > 900 and pos1[0] < 1000 and pos1[1] > 700 and pos1[1] < 750 :
            self.schreiben = True
        elif pos1[0] > 680 and pos1[0] < 780 and pos1[1] > 700 and pos1[1] < 750 :
            if geboten == self.gesetzt :
                if amZug + 1 < len(spieler) :
                    amZug += 1 
                else :
                    amZug = 0 
                pygame.time.wait(500)
            else :
                self.imSpiel = False
                if amZug + 1 < len(spieler) :
                    amZug += 1 
                else :
                    amZug = 0

            zeichne()

            screen.blit(karte_geschlossen_b, (feld1))
            screen.blit(karte_geschlossen_b, (feld2))

            pygame.display.update()
            pygame.time.wait(500)

            self.war_dran = True

            while True :
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT: sys.exit()

                gedrueckt = pygame.key.get_pressed()
                if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                    pygame.time.wait(300)
                    break

        elif pos1[0] > 1110 and pos1[0] < 1190 and pos1[1] > 700 and pos1[1] < 750 :
            if self.setzen != "0" and self.gesetzt + int(self.setzen) >= geboten :
                self.gesetzt += int(self.setzen)
                self.geld -= int(self.setzen)
                geboten = self.gesetzt
                self.schreiben = False

                for i in niedriger :
                    i.gesetzt2 += i.g

                if amZug + 1 < len(spieler) :
                    amZug += 1 
                else :
                    amZug = 0

                self.setzen = "0" 

                zeichne()

                screen.blit(karte_geschlossen_b, (feld1))
                screen.blit(karte_geschlossen_b, (feld2))

                pygame.display.update()
                pygame.time.wait(500)

                self.war_dran = True

                while True :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT: sys.exit()

                    gedrueckt = pygame.key.get_pressed()
                    if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                        pygame.time.wait(300)
                        break

        elif pos1[0] > 1010 and pos1[0] < 1100 and pos1[1] > 700 and pos1[1] < 750 :
            self.setzen = "0"
            self.gesetzt += self.geld
            self.schreiben = False

            if self.gesetzt > geboten :
                geboten = self.gesetzt

            if self.gesetzt < geboten :
                self.gesetzt2 = self.gesetzt + pott
                self.g = self.gesetzt2

                niedriger.append(self)

            for i in niedriger :
                i.gesetzt2 += self.geld

            if amZug + 1 < len(spieler) :
                amZug += 1 
            else :
                amZug = 0

            self.geld = 0 

            zeichne()

            screen.blit(karte_geschlossen_b, (feld1))
            screen.blit(karte_geschlossen_b, (feld2))

            pygame.display.update()
            pygame.time.wait(500)

            self.war_dran = True

            while True :
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT: sys.exit()

                gedrueckt = pygame.key.get_pressed()
                if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                    pygame.time.wait(300)
                    break

        elif pos1[0] > 790 and pos1[0] < 890 and pos1[1] > 700 and pos1[1] < 750 :
            if geboten > self.gesetzt :
                d = geboten - self.gesetzt

                self.setzen = "0"
                self.gesetzt += d
                self.geld -= d
                self.schreiben = False

                for i in niedriger :
                    i.gesetzt2 += i.g

                if amZug + 1 < len(spieler) :
                    amZug += 1 
                else :
                    amZug = 0

                zeichne()

                screen.blit(karte_geschlossen_b, (feld1))
                screen.blit(karte_geschlossen_b, (feld2))

                pygame.display.update()
                pygame.time.wait(500)

                self.war_dran = True

                while True :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT: sys.exit()

                    gedrueckt = pygame.key.get_pressed()
                    if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                        pygame.time.wait(300)
                        break


    def tippen(self) :
        if self.schreiben :
            gedrueckt = pygame.key.get_pressed()

            if gedrueckt[pygame.K_0] or gedrueckt[pygame.K_KP0] :
                if self.setzen[0] != "0" :
                    if int(self.setzen + "0") <= self.geld :
                        self.setzen += "0"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_1] or gedrueckt[pygame.K_KP1] :
                if int(self.setzen + "1") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "1"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "1"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_2] or gedrueckt[pygame.K_KP2] :
                if int(self.setzen + "1") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "2"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "2"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_3] or gedrueckt[pygame.K_KP3] :
                if int(self.setzen + "1") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "3"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "3"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_4] or gedrueckt[pygame.K_KP4] :
                if int(self.setzen + "4") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "4"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "4"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_5] or gedrueckt[pygame.K_KP5] :
                if int(self.setzen + "5") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "5"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "5"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_6] or gedrueckt[pygame.K_KP6] :
                if int(self.setzen + "6") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "6"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "6"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_7] or gedrueckt[pygame.K_KP7] :
                if int(self.setzen + "7") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "7"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "7"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_8] or gedrueckt[pygame.K_KP8] :
                if int(self.setzen + "8") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "8"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "8"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_9] or gedrueckt[pygame.K_KP9] :
                if int(self.setzen + "9") <= self.geld :
                    if self.setzen[0] == "0" and len(self.setzen) == 1 : 
                        self.setzen = "9"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
                    else :
                        self.setzen += "9"
                        zeichne()
                        pygame.display.update()
                        pygame.time.wait(500)
            elif gedrueckt[pygame.K_BACKSPACE] or gedrueckt[pygame.K_KP_EQUALS] :
                if len(self.setzen) == 1 :
                    self.setzen = "0"
                else :
                    neu = ""
                    i = 0
                    for z in self.setzen :
                        if i == len(self.setzen) - 1 :
                            break
                        neu += z
                        i += 1

                    self.setzen = neu

                    zeichne()
                    pygame.display.update()
                    pygame.time.wait(500)
            elif gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER] :
                self.schreiben = False

class Ki(Spieler) :
    def __init__(self, farbe) :
        Spieler.__init__(self, geld_menge, farbe, 0, "0")
        self.art = "Ki"

    def spieler_zeichnen(self) :
        pass

    def tippen(self) :
        pass

    def mausklick(self) :
        pass

    def checken_folden(self) :
        global amZug, geboten, pott

        if geboten == self.gesetzt :
            if amZug + 1 < len(spieler) :
                amZug += 1 
            else :
                amZug = 0 
            pygame.time.wait(500)
        else :
            self.imSpiel = False
            if amZug + 1 < len(spieler) :
                amZug += 1 
            else :
                amZug = 0

        zeichne()

        screen.blit(karte_geschlossen_b, (feld1))
        screen.blit(karte_geschlossen_b, (feld2))

        pygame.display.update()
        pygame.time.wait(500)

        self.war_dran = True

        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT: sys.exit()

            gedrueckt = pygame.key.get_pressed()
            if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                pygame.time.wait(300)
                break

    def funk_setzen(self) :
        global amZug, geboten, pott

        if self.setzen != "0" and self.gesetzt + int(self.setzen) >= geboten :
            self.gesetzt += int(self.setzen)
            self.geld -= int(self.setzen)
            geboten = self.gesetzt
            self.schreiben = False

            for i in niedriger :
                i.gesetzt2 += i.g

            if amZug + 1 < len(spieler) :
                amZug += 1 
            else :
                amZug = 0

            self.setzen = "0" 

            zeichne()

            screen.blit(karte_geschlossen_b, (feld1))
            screen.blit(karte_geschlossen_b, (feld2))

            pygame.display.update()
            pygame.time.wait(500)

            self.war_dran = True

            while True :
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT: sys.exit()

                gedrueckt = pygame.key.get_pressed()
                if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                    pygame.time.wait(300)
                    break

    def funk_all_in(self) :
        global amZug, geboten, pott

        self.setzen = "0"
        self.gesetzt += self.geld
        self.schreiben = False

        if self.gesetzt > geboten :
            geboten = self.gesetzt

        if self.gesetzt < geboten :
            self.gesetzt2 = self.gesetzt + pott
            self.g = self.gesetzt2

            niedriger.append(self)

        for i in niedriger :
            i.gesetzt2 += self.geld

        if amZug + 1 < len(spieler) :
            amZug += 1 
        else :
            amZug = 0

        self.geld = 0 

        zeichne()

        screen.blit(karte_geschlossen_b, (feld1))
        screen.blit(karte_geschlossen_b, (feld2))

        pygame.display.update()
        pygame.time.wait(500)

        self.war_dran = True

        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT: sys.exit()

            gedrueckt = pygame.key.get_pressed()
            if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                pygame.time.wait(300)
                break

    def mitgehen(self) :
        global amZug, geboten, pott

        if geboten > self.gesetzt :
            d = geboten - self.gesetzt

            self.setzen = "0"
            self.gesetzt += d
            self.geld -= d
            self.schreiben = False

            for i in niedriger :
                i.gesetzt2 += i.g

            if amZug + 1 < len(spieler) :
                amZug += 1 
            else :
                amZug = 0

            zeichne()

            screen.blit(karte_geschlossen_b, (feld1))
            screen.blit(karte_geschlossen_b, (feld2))

            pygame.display.update()
            pygame.time.wait(500)

            self.war_dran = True

            while True :
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT: sys.exit()

                gedrueckt = pygame.key.get_pressed()
                if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER]:
                    pygame.time.wait(300)
                    break

    def machen(self) :
        liste = self.blatt + mitte

        bestes = None
        liste = mitte + s.blatt
        stop = False

        self.benutzt = []

        self.karten2 = []
        i = 0
    
        while i < len(liste) :
            grösstes = liste[0]
            for x in liste :
                if x.name > grösstes.name :
                    grösstes = x
            
            self.karten2.append(grösstes)
            liste.remove(grösstes)

        #Royal Flush

        for k in self.karten2 :
            if k.name == 14 :
                for k2 in self.karten2 :
                    if k2.name == 13 and k2.farbe == k.farbe :
                        for k3 in self.karten2 :
                            if k3.name == 12 and k3.farbe == k2.farbe :
                                for k4 in self.karten2 :
                                    if k4.name == 11 and k4.farbe == k3.farbe :
                                        for k5 in self.karten2 :
                                            if k5.name == 10 and k5.farbe == k4.farbe :
                                                bestes = Royal_Flush()
                                                stop = True
                                                self.benutzt.append(k)
                                                self.benutzt.append(k2)
                                                self.benutzt.append(k3)
                                                self.benutzt.append(k4)
                                                self.benutzt.append(k5)
                                                break
                                        if stop :
                                            break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
        if not stop :

            #Straight Flush

            for k in self.karten2 :
                for k2 in self.karten2 :
                    if k2.name == k.name + 1 and k2.farbe == k.farbe :
                        for k3 in self.karten2 :
                            if k3.name == k2.name + 1 and k3.farbe == k2.farbe:
                                for k4 in self.karten2 :
                                    if k4.name == k3.name + 1 and k4.farbe == k3.farbe:
                                        for k5 in self.karten2 :
                                            if k5.name == k4.name + 1 and k5.farbe == k4.farbe:
                                                bestes = Straight_Flush(k5.name)
                                                stop = True
                                                self.benutzt.append(k)
                                                self.benutzt.append(k2)
                                                self.benutzt.append(k3)
                                                self.benutzt.append(k4)
                                                self.benutzt.append(k5)
                                                break
                                        if stop :
                                            break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
            if not stop :

                #Vierling

                for k in self.karten2 :
                    for k2 in self.karten2 :
                        if k2.name == k.name and k2 != k :
                            for k3 in self.karten2 :
                                if k3.name == k2.name and k3 != k2 and k3 != k :
                                    for k4 in self.karten2 :
                                        if k4.name == k3.name and k4 != k3 and k4 != k2 and k4 != k:
                                            bestes = Vierling(k4.name)
                                            stop = True
                                            self.benutzt.append(k)
                                            self.benutzt.append(k2)
                                            self.benutzt.append(k3)
                                            self.benutzt.append(k4)
                                            break
                                    if stop :
                                        break
                            if stop :
                                break
                    if stop :
                        break
                if not stop :

                    #Full House

                    for k in self.karten2 :
                        for k2 in self.karten2 :
                            if k2.name == k.name and k2 != k :
                                for k3 in self.karten2 :
                                    if k3.name == k2.name and k3 != k2 and k3 != k :
                                        for k4 in self.karten2 :
                                            if k4.name != k.name :
                                                for k5 in self.karten2 :
                                                    if k5.name == k4.name and k5 != k4 :
                                                        bestes = Full_House(k3.name, k5.name)
                                                        stop = True
                                                        self.benutzt.append(k)
                                                        self.benutzt.append(k2)
                                                        self.benutzt.append(k3)
                                                        self.benutzt.append(k4)
                                                        self.benutzt.append(k5)
                                                        break
                                                if stop :
                                                    break
                                        if stop :
                                            break
                                if stop :
                                    break
                        if stop :
                            break
                    if not stop :

                        #Flush

                        for k in self.karten2 :
                            for k2 in self.karten2 :
                                if k2.farbe == k.farbe and k2 != k :
                                    for k3 in self.karten2 :
                                        if k3.farbe == k2.farbe and k3 != k2 and k3 != k :
                                            for k4 in self.karten2 :
                                                if k4.farbe == k3.farbe and k4 != k3 and k4 != k2 and k4 != k :
                                                    for k5 in self.karten2 :
                                                        if k5.farbe == k4.farbe and k5 != k4 and k5 != k3 and k5 != k2 and k5 != k :
                                                            bestes = Flush(k.name, k2.name, k3.name, k4.name, k5.name)
                                                            stop = True
                                                            self.benutzt.append(k)
                                                            self.benutzt.append(k2)
                                                            self.benutzt.append(k3)
                                                            self.benutzt.append(k4)
                                                            self.benutzt.append(k5)
                                                            break
                                                    if stop :
                                                        break
                                            if stop :
                                                break
                                    if stop :
                                        break
                            if stop :
                                break
                        if not stop :

                            #Straße

                            for k in self.karten2 :
                                for k2 in self.karten2 :
                                    if k2.name == k.name + 1 :
                                        for k3 in self.karten2 :
                                            if k3.name == k2.name + 1 :
                                                for k4 in self.karten2 :
                                                    if k4.name == k3.name + 1 :
                                                        for k5 in self.karten2 :
                                                            if k5.name == k4.name + 1 :
                                                                bestes = Strasse(k5.name)
                                                                stop = True
                                                                self.benutzt.append(k)
                                                                self.benutzt.append(k2)
                                                                self.benutzt.append(k3)
                                                                self.benutzt.append(k4)
                                                                self.benutzt.append(k5)
                                                                break
                                                        if stop :
                                                            break
                                                if stop :
                                                    break
                                        if stop :
                                            break
                                if stop :
                                    break
                            if not stop :

                                #Drilling

                                for k in self.karten2 :
                                    for k2 in self.karten2 :
                                        if k2.name == k.name and k2 != k :
                                            for k3 in self.karten2 :
                                                if k3.name == k2.name and k3 != k2 and k3 != k :
                                                    bestes = Drilling(k3.name)
                                                    stop = True
                                                    self.benutzt.append(k)
                                                    self.benutzt.append(k2)
                                                    self.benutzt.append(k3)
                                                    break
                                            if stop :
                                                break
                                    if stop :
                                        break
                                if not stop :

                                    #zwei Paare

                                    for k in self.karten2 :
                                        for k2 in self.karten2 :
                                            if k2.name == k.name and k2 != k :
                                                for k3 in self.karten2 :
                                                    if k3.name != k.name :
                                                        for k4 in self.karten2 :
                                                            if k4.name == k3.name and k4 != k3 :
                                                                bestes = zwei_Paare(k.name, k4.name)
                                                                stop = True
                                                                self.benutzt.append(k)
                                                                self.benutzt.append(k2)
                                                                self.benutzt.append(k3)
                                                                self.benutzt.append(k4)
                                                                break
                                                        if stop :
                                                            break
                                                if stop :
                                                    break
                                        if stop :
                                            break
                                    if not stop :

                                        #Paar

                                        for k in self.karten2 :
                                            for k2 in self.karten2 :
                                                if k2.name == k.name and k2 != k :
                                                    bestes = Paar(k.name)
                                                    stop = True
                                                    self.benutzt.append(k)
                                                    self.benutzt.append(k2)
                                                    break
                                            if stop :
                                                break

        if bestes != None :
            
            #Royal Flush

            if bestes.höhe == 9 :
                if len(mitte) < 5 :
                    l = ["20", "30", "40"]
                    rand = randint(0, 2)
                    if self.geld > int(l[rand]) and self.gesetzt + int(l[rand]) >= geboten :
                        self.setzen = l[rand]
                        self.funk_setzen()
                    else :
                        self.funk_all_in()
                else :
                    if pott < geld_menge / 2 :
                        if geboten > self.gesetzt and self.geld < geboten - self.gesetzt :
                            self.mitgehen()
                        elif geboten > self.gesetzt and self.geld == geboten - self.gesetzt :
                            self.funk_all_in()
                        else :
                            self.checken_folden()
                    else :
                        self.funk_all_in()

            #Straight Flush
            
            elif bestes.höhe == 8 :
                if len(mitte) < 5 :
                    l = ["20", "30", "40"]
                    rand = randint(0, 2)

                    if self.geld > int(l[rand]) and self.gesetzt + int(l[rand]) >= geboten :
                        self.setzen = l[rand]
                        self.funk_setzen()
                    else :
                        self.funk_all_in()
                else :
                    if pott < geld_menge / 2 :
                        if geboten > self.gesetzt and self.geld < geboten - self.gesetzt :
                            self.mitgehen()
                        elif geboten > self.gesetzt and self.geld == geboten - self.gesetzt :
                            self.funk_all_in()
                        else :
                            self.checken_folden()
                    else :
                        self.funk_all_in()

            #Vierling

            elif bestes.höhe == 7 :
                if self.blatt[0] in self.benutzt and self.blatt[1] in self.benutzt :
                    if pott < self.geld / 2 :
                        l = ["30", "40", "50"]
                        self.setzen = l[randint(0, 2)]

                        if int(self.setzen) < self.geld and self.gesetzt + int(l[rand]) >= geboten :
                            self.funk_setzen()
                        else :
                            self.setzen = "0"
                            self.funk_all_in()
                    else :
                        self.funk_all_in()

                elif self.blatt[0] in l or self.blatt[1] in l :
                    if self.gesetzt < geboten :
                        if self.geld > geboten - self.gesetzt :
                            self.mitgehen()
                        elif self.geld == geboten - self.gesetzt :
                            self.funk_all_in()
                        else :
                            self.checken_folden()
                    else :
                        self.checken_folden()

                elif not self.blatt[0] in self.benutzt and not self.blatt[1] in self.benutzt :
                    if self.blatt[0].name >= 10 or self.blatt[1].name >= 10 :
                        if self.blatt[0].name == 14 or self.blatt[1].name == 14 :
                            self.funk_all_in()
                        else :
                            if self.geld > geboten - self.gesetzt :
                                self.mitgehen()
                            else :
                                self.funk_all_in()
                    else :
                        self.checken_folden()

            #Full House

            elif bestes.höhe == 6 :
                if self.blatt[0] in self.benutzt and self.blatt[1] in self.benutzt :
                    if len(mitte) >= 4 :
                        self.funk_all_in()
                    else :
                        l = ["20", "30", "40", "50"]
                        rand = l[randint(0, 3)]

                        if int(rand) < self.geld :
                            self.setzen = rand + geboten - self.gesetzt

                            if int(self.setzen) < self.geld :
                                self.funk_setzen()
                            else :
                                self.funk_all_in()
                        else :
                            self.funk_all_in()

                elif self.blatt[0] in self.benutzt or self.blatt[1] in self.benutzt :
                    l = ["20", "30", "40"]
                    rand = l[randint(0, 2)]

                    if int(rand) < self.geld :
                        self.setzen = rand + geboten - self.gesetzt

                        if int(self.setzen) < self.geld :
                            self.funk_setzen()
                        else :
                            self.funk_all_in()
                    else :
                        self.funk_all_in()

                elif not self.blatt[0] in self.benutzt and not self.blatt[1] in self.benutzt :
                    l = ["30", "40", "50"]
                    rand = l[randint(0, 2)]

                    if int(rand) < self.geld :
                        self.setzen = rand + geboten - self.gesetzt

                        if int(self.setzen) < self.geld :
                            self.funk_setzen()
                        else :
                            self.funk_all_in()
                    else :
                        self.funk_all_in()

            #Flush

            elif bestes.höhe == 5 :
                if self.blatt[0] in self.benutzt and self.blatt[0] in self.benutzt :
                    if not mitte[len(mitte) - 1] in self.benutzt :
                        l = ["30", "40", "50"]
                        rand = l[randint(0, 2)]

                        if int(rand) < self.geld :
                            self.setzen = rand + geboten - self.gesetzt

                            if int(self.setzen) < self.geld :
                                self.funk_setzen()
                            else :
                                self.funk_all_in()
                        else :
                            self.funk_all_in()
                    else :
                        if len(mitte) == 5 :
                            l = ["10", "20", "30"]
                            rand = l[randint(0, 2)]

                            if int(rand) < self.geld :
                                self.setzen = rand + geboten - self.gesetzt

                                if int(self.setzen) < self.geld :
                                    self.funk_setzen()
                                else :
                                    self.funk_all_in()
                            else :
                                self.funk_all_in()
                        else :
                            if geboten > self.gesetzt and self.geld > geboten - self.gesetzt :
                                self.mitgehen()
                            elif geboten > self.gesetzt and self.geld == geboten - self.gesetzt :
                                self.funk_all_in()
                            else :
                                self.checken_folden()

                elif self.blatt[0] in self.benutzt or self.blatt[1] in self.benutzt :
                    if bestes.wert >= 11 :
                        l = ["40", "50"]
                        rand = l[randint(0, 1)]

                        if int(rand) < self.geld :
                            self.setzen = rand + geboten - self.gesetzt

                            if int(self.setzen) < self.geld :
                                self.funk_setzen()
                            else :
                                self.funk_all_in()
                        else :
                            self.funk_all_in()
                    else :
                        if geboten > self.gesetzt and geboten - self.gesetzt <= self.geld / 2 :
                            self.mitgehen()
                        else :
                            self.checken_folden()

                elif not self.blatt[0] in self.benutzt and not self.blatt[1] in self.benutzt :
                    if geboten > self.gesetzt and geboten - self.gesetzt < self.geld :
                        self.mitgehen()
                    else :
                        self.funk_all_in()

            #Straße

            elif bestes.höhe == 4 :
                if self.blatt[0] in self.benutzt and self.blatt[1] in self.benutzt :
                    if self.geld <= 100 :
                        self.funk_all_in()
                    else :
                        l = ["20", "30", "40"]
                        rand = l[randint(0, 2)]

                        if int(rand) < self.geld :
                            self.setzen = rand + geboten - self.gesetzt

                            if int(self.setzen) < self.geld :
                                self.funk_setzen()
                            else :
                                self.funk_all_in()
                        else :
                            self.funk_all_in()

                elif self.blatt[0] in self.benutzt or self.blatt[1] in self.benutzt :
                    if self.geld <= 100 and pott >= 500 :
                        self.funk_all_in()
                    else :
                        l = ["30", "40", "50"]
                        rand = l[randint(0, 2)]

                        if int(rand) < self.geld :
                            self.setzen = rand + geboten - self.gesetzt

                            if int(self.setzen) < self.geld :
                                self.funk_setzen()
                            else :
                                self.funk_all_in()
                        else :
                            self.funk_all_in()

                elif not self.blatt[0] in self.benutzt and not self.blatt[1] in self.benutzt :
                    if bestes.wert >= 10 :
                        l = ["30", "40",  "50"]
                        rand = l[randint(0, 2)]

                        if int(rand) < self.geld :
                            self.setzen = str(int(rand) + geboten - self.gesetzt)

                            if int(self.setzen) < self.geld :
                                self.funk_setzen()
                            else :
                                self.funk_all_in()
                        else :
                            self.funk_all_in()
                    else :
                        if geboten > self.gesetzt and geboten - self.gesetzt < self.geld :
                            self.mitgehen()
                        else :
                            self.funk_all_in()

                #Drilling

                elif bestes.höhe == 3 :
                    print("Drilling")

                    if self.blatt[0] in self.benutzt and self.blatt[1] in self.benutzt :
                        if len(mitte) < 5 :
                            l = ["30", "40"]
                            rand = l[randint(0, 1)]

                            if int(rand) < self.geld :
                                self.setzen = str(int(rand) + geboten - self.gesetzt)

                                if int(self.setzen) < self.geld :
                                    self.funk_setzen()
                                else :
                                    self.funk_all_in()
                            else :
                                self.funk_all_in()
                        else :
                            if self.geld <= 100 :
                                self.funk_all_in()
                            else :
                                self.setzen = str(self.geld / 2 + geboten - self.gesetzt)

                                if int(self.setzen) < self.geld :
                                    self.funk_setzen()
                                else :
                                    self.funk_all_in()

                    elif self.blatt[0] in self.benutzt or self.blatt[1] in self.benutzt :
                        if geboten == self.gesetzt :
                            l = ["10", "20", "30", "40"]
                            rand = l[randint(0, 3)]

                            if int(rand) < self.geld :
                                self.setzen = rand + geboten - self.gesetzt

                                if self.setzen < self.geld :
                                    self.funk_setzen()
                                else :
                                    self.funk_all_in()
                            else :
                                self.funk_all_in()
                        else :
                            self.mitgehen()

                    elif not self.blatt[0] in self.benutzt and not self.blatt[1] in self.benutzt :
                        rand1 = randint(0, 1)

                        if rand1 == 0 :
                            l = ["40", "50"]
                            rand = l[randint(0, 1)]

                            if int(rand) < self.geld :
                                self.setzen = rand + geboten - self.gesetzt

                                if self.setzen < self.geld :
                                    self.funk_setzen()
                                else :
                                    self.funk_all_in()
                            else :
                                self.funk_all_in()

                        elif rand == 1 :
                            if len(mitte) == 5 :
                                if geboten > self.gesetzt :
                                    self.mitgehen()
                                else :
                                    self.checken_folden()
                            else :
                                if geboten - self.gesetzt <= self.geld / 2 :
                                    self.mitgehen()
                                else :
                                    self.checken_folden()

                    #zwei Paare

                    elif bestes.höhe == 2 :
                        if self.blatt[0] in self.benutzt and self.blatt[1] in self.benutzt :
                            if geboten > self.gesetzt :
                                if geboten - self.gesetzt <= self.geld / 2 :
                                    self.mitgehen()
                                else :
                                    self.checken_folden()
                            else :
                                if self.geld >= geld_menge / 2 :
                                    l = ["10", "20"]
                                    rand = l[randint(0, 1)]

                                    if int(rand) < self.geld :
                                        self.setzen = rand + geboten - self.gesetzt

                                        if int(self.setzen) < self.geld :
                                            self.funk_setzen()
                                        else :
                                            self.funk_all_in()
                                    else :
                                        self.funk_all_in()

            else :
                if self.gesetzt == geboten :
                    self.checken_folden()
                else :
                    self.mitgehen()

        else :
            if self.gesetzt == geboten :
                self.checken_folden()
            else :
                self.mitgehen()

spieler = []

f1 = (255, 255, 0)
f2 = (255, 0, 0)
f3 = (0, 255, 0)
f4 = (0, 0, 255)
f5 = (100, 0, 0)
f6 = (0, 0, 150)
f7 = (100, 0, 100)
f8 = (0, 150, 100)
f9 = (150, 70, 170)
f10 = (0, 0, 0)

f = 1
for i in range(anzahl_spieler) :
    if f == 1 :
        s = Spieler(geld_menge, f1, 0, "0")
    elif f == 2 :
        s = Spieler(geld_menge, f2, 0, "0")
    elif f == 3 :
        s = Spieler(geld_menge, f3, 0, "0")
    elif f == 4 :
        s = Spieler(geld_menge, f4, 0, "0")
    elif f == 5 :
        s = Spieler(geld_menge, f5, 0, "0")
    elif f == 6 :
        s = Spieler(geld_menge, f6, 0, "0")
    elif f == 7 :
        s = Spieler(geld_menge, f7, 0, "0")
    elif f == 8 :
        s = Spieler(geld_menge, f8, 0, "0")
    elif f == 9 :
        s = Spieler(geld_menge, f9, 0, "0")
    elif f == 10 :
        s = Spieler(geld_menge, f10, 0, "0")

    f += 1

    spieler.append(s)

for i in range(anzahl_ki) :
    if f == 2 :
        s = Ki(f2)
    elif f == 3 :
        s = Ki(f3)
    elif f == 4 :
        s = Ki(f4)
    elif f == 5 :
        s = Ki(f5)
    elif f == 6 :
        s = Ki(f6)
    elif f == 7 :
        s = Ki(f7)
    elif f == 8 :
        s = Ki(f8)
    elif f == 9 :
        s = Ki(f9)
    elif f == 10 :
        s = Ki(f10)

    f += 1

    spieler.append(s)


felder = []
spieler_felder = [(50,30), (170,30), (290,30), (410,30), (530,30), (650,30), (770,30), (890,30), (1020,30), (1140,30)]
spieler_felder2 = [(50,70), (170,70), (290,70), (410,70), (530,70), (650,70), (770,70), (890,70), (1020,70), (1140,70)]

x = 200
for i in range(5) :
    felder.append((x, 250))
    x += 160

def karten_generieren() :
    k = 51
    for s in spieler :
        s.blatt.clear()
        for i in range(2) :
            rand = randint(0, k)
            s.blatt.append(karten[rand])
            karten.remove(karten[rand])
            k -= 1 
        

def zeichne() :
    screen.blit(tisch, (0,0))

    f = 0 
    for i in spieler :
        textGrund,textKasten = textObjekt(str(i.geld), font, i.farbe)
        textKasten.center = (spieler_felder[f])
        screen.blit(textGrund,textKasten)

        textGrund,textKasten = textObjekt(str(i.gesetzt), font2, i.farbe)
        textKasten.center = (spieler_felder2[f])
        screen.blit(textGrund,textKasten)

        pygame.draw.circle(screen, (0, 0, 0), (spieler_felder[amZug][0], spieler_felder[amZug][1] + 20), 5, 0)
        screen.blit(dealer_b, (spieler_felder2[dealer][0] - 50, spieler_felder2[dealer][1] + 30))

        f += 1 

    f = 0 

    for i in mitte :
        screen.blit(i.bild, (felder[f]))
        f += 1

    spieler[amZug].spieler_zeichnen()

def zeichne_all_in() :
    screen.blit(tisch, (0,0))

    f = 0 
    for i in spieler :
        textGrund,textKasten = textObjekt(str(i.geld), font, i.farbe)
        textKasten.center = (spieler_felder[f])
        screen.blit(textGrund,textKasten)

        textGrund,textKasten = textObjekt(str(i.gesetzt), font2, i.farbe)
        textKasten.center = (spieler_felder2[f])
        screen.blit(textGrund,textKasten)

        pygame.draw.circle(screen, (0, 0, 0), (spieler_felder[amZug][0], spieler_felder[amZug][1] + 20), 5, 0)

        screen.blit(dealer_b, (spieler_felder2[dealer][0] - 50, spieler_felder2[dealer][1] + 30))

        textGrund,textKasten = textObjekt(str(pott), font, (0, 0, 0))
        textKasten.center = (600, 200)
        screen.blit(textGrund,textKasten)

        screen.blit(chip_b, (650,180))

        f += 1 

    f = 0 

    for i in mitte :
        screen.blit(i.bild, (felder[f]))
        f += 1

    x = 0
    for s in spieler :
        if s.imSpiel :
            pygame.draw.line(screen, s.farbe, (x, 671), (x, 800), 2)
            x += 5

            s.blatt[0].x = x

            screen.blit(s.blatt[0].bild, (x, 671))
            x += 155

            s.blatt[1].x = x

            screen.blit(s.blatt[1].bild, (x, 671))
            x += 155
            pygame.draw.line(screen, s.farbe, (x, 671), (x, 800), 2)
            x += 4

def zeichne_gewonnen(gewinner, beste) :
    zeichne_all_in()
    for g in gewinner :
        f = 0
        for k in mitte :
            if k in g.benutzt :
                pygame.draw.rect(screen, g.farbe, (felder[f][0], felder[f][1], 150, 209), 2)

            f += 1

        for kb in g.blatt :
            if kb in g.benutzt :
                pygame.draw.rect(screen, g.farbe, (kb.x, kb.y, 150, 209), 2)

def runde_gewonnen(g=True) :
    global pott

    beste = []
    gewinner = []

    nur_none = True

    for s in spieler :
        if s.imSpiel :
            bestes = None
            liste = mitte + s.blatt
            stop = False

            s.benutzt = []

            s.karten2 = []
            i = 0
        
            while i < len(liste) :
                grösstes = liste[0]
                for x in liste :
                    if x.name > grösstes.name :
                        grösstes = x
                
                s.karten2.append(grösstes)
                liste.remove(grösstes)

            #Royal Flush

            for k in s.karten2 :
                if k.name == 14 :
                    for k2 in s.karten2 :
                        if k2.name == 13 and k2.farbe == k.farbe :
                            for k3 in s.karten2 :
                                if k3.name == 12 and k3.farbe == k2.farbe :
                                    for k4 in s.karten2 :
                                        if k4.name == 11 and k4.farbe == k3.farbe :
                                            for k5 in s.karten2 :
                                                if k5.name == 10 and k5.farbe == k4.farbe :
                                                    bestes = Royal_Flush()
                                                    beste.append(bestes)
                                                    stop = True
                                                    s.benutzt.append(k)
                                                    s.benutzt.append(k2)
                                                    s.benutzt.append(k3)
                                                    s.benutzt.append(k4)
                                                    s.benutzt.append(k5)
                                                    break
                                            if stop :
                                                break
                                    if stop :
                                        break
                            if stop :
                                break
                    if stop :
                        break
            if stop :
                continue

            #Straight Flush

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.name == k.name + 1 and k2.farbe == k.farbe :
                        for k3 in s.karten2 :
                            if k3.name == k2.name + 1 and k3.farbe == k2.farbe:
                                for k4 in s.karten2 :
                                    if k4.name == k3.name + 1 and k4.farbe == k3.farbe:
                                        for k5 in s.karten2 :
                                            if k5.name == k4.name + 1 and k5.farbe == k4.farbe:
                                                bestes = Straight_Flush(k5.name)
                                                beste.append(bestes)
                                                stop = True
                                                s.benutzt.append(k)
                                                s.benutzt.append(k2)
                                                s.benutzt.append(k3)
                                                s.benutzt.append(k4)
                                                s.benutzt.append(k5)
                                                break
                                        if stop :
                                            break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
            if stop :
                continue

            #Vierling

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.name == k.name and k2 != k :
                        for k3 in s.karten2 :
                            if k3.name == k2.name and k3 != k2 and k3 != k :
                                for k4 in s.karten2 :
                                    if k4.name == k3.name and k4 != k3 and k4 != k2 and k4 != k:
                                        bestes = Vierling(k4.name)
                                        beste.append(bestes)
                                        stop = True
                                        s.benutzt.append(k)
                                        s.benutzt.append(k2)
                                        s.benutzt.append(k3)
                                        s.benutzt.append(k4)
                                        break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
            if stop :
                continue

            #Full House

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.name == k.name and k2 != k :
                        for k3 in s.karten2 :
                            if k3.name == k2.name and k3 != k2 and k3 != k :
                                for k4 in s.karten2 :
                                    if k4.name != k.name :
                                        for k5 in s.karten2 :
                                            if k5.name == k4.name and k5 != k4 :
                                                bestes = Full_House(k3.name, k5.name)
                                                beste.append(bestes)
                                                stop = True
                                                s.benutzt.append(k)
                                                s.benutzt.append(k2)
                                                s.benutzt.append(k3)
                                                s.benutzt.append(k4)
                                                s.benutzt.append(k5)
                                                break
                                        if stop :
                                            break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
            if stop :
                continue

            #Flush

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.farbe == k.farbe and k2 != k :
                        for k3 in s.karten2 :
                            if k3.farbe == k2.farbe and k3 != k2 and k3 != k :
                                for k4 in s.karten2 :
                                    if k4.farbe == k3.farbe and k4 != k3 and k4 != k2 and k4 != k :
                                        for k5 in s.karten2 :
                                            if k5.farbe == k4.farbe and k5 != k4 and k5 != k3 and k5 != k2 and k5 != k :
                                                bestes = Flush(k.name, k2.name, k3.name, k4.name, k5.name)
                                                beste.append(bestes)
                                                stop = True
                                                s.benutzt.append(k)
                                                s.benutzt.append(k2)
                                                s.benutzt.append(k3)
                                                s.benutzt.append(k4)
                                                s.benutzt.append(k5)
                                                break
                                        if stop :
                                            break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
            if stop :
                continue

            #Strße

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.name == k.name + 1 :
                        for k3 in s.karten2 :
                            if k3.name == k2.name + 1 :
                                for k4 in s.karten2 :
                                    if k4.name == k3.name + 1 :
                                        for k5 in s.karten2 :
                                            if k5.name == k4.name + 1 :
                                                bestes = Strasse(k5.name)
                                                beste.append(bestes)
                                                stop = True
                                                s.benutzt.append(k)
                                                s.benutzt.append(k2)
                                                s.benutzt.append(k3)
                                                s.benutzt.append(k4)
                                                s.benutzt.append(k5)
                                                break
                                        if stop :
                                            break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
            if stop :
                continue

            #Drilling

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.name == k.name and k2 != k :
                        for k3 in s.karten2 :
                            if k3.name == k2.name and k3 != k2 and k3 != k :
                                bestes = Drilling(k3.name)
                                beste.append(bestes)
                                stop = True
                                s.benutzt.append(k)
                                s.benutzt.append(k2)
                                s.benutzt.append(k3)
                                break
                        if stop :
                            break
                if stop :
                    break
            if stop :
                continue

            #zwei Paare

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.name == k.name and k2 != k :
                        for k3 in s.karten2 :
                            if k3.name != k.name :
                                for k4 in s.karten2 :
                                    if k4.name == k3.name and k4 != k3 :
                                        bestes = zwei_Paare(k.name, k4.name)
                                        beste.append(bestes)
                                        stop = True
                                        s.benutzt.append(k)
                                        s.benutzt.append(k2)
                                        s.benutzt.append(k3)
                                        s.benutzt.append(k4)
                                        break
                                if stop :
                                    break
                        if stop :
                            break
                if stop :
                    break
            if stop :
                continue

            #Paar

            for k in s.karten2 :
                for k2 in s.karten2 :
                    if k2.name == k.name and k2 != k :
                        bestes = Paar(k.name)
                        beste.append(bestes)
                        stop = True
                        s.benutzt.append(k)
                        s.benutzt.append(k2)
                        break
                if stop :
                    break
            if stop :
                continue

            beste.append(None)
        else :
            beste.append("fold")

    #Gewonnen?

    höchste = []
    
    i = 0 
    for b in beste :
        if b != None and b != "fold" :
            if b.höhe == 9 :
                gewinner.append(spieler[i])
            i += 1 

    i = 0 
    if gewinner == [] :
        höchstes = beste[0]

        for b in beste :
            if höchstes == None or höchstes == "fold" :
                höchstes = b
            else :
                break

        for b in beste :
            if b != None and b != "fold" :
                if b.höhe > höchstes.höhe :
                    höchstes = b
                    höchste.clear()
                    höchste.append(höchstes)
                    höchste.append(i)
                elif b.höhe == höchstes.höhe :
                    höchste.append(b)
                    höchste.append(i)

            i += 1
        
        if len(höchste) > 2 :
            for x in höchste :
                i = 0 
                for y in höchste :
                    if x != None and y != None and x != "fold" and y != "fold":
                        try :
                            if x.wert > y.wert :
                                höchste.remove(y)
                                höchste[i] = "löschen"
                                höchste.remove("löschen")
                        except AttributeError :
                            pass 
                        i += 1

        if len(höchste) > 2 :
            for x in höchste :
                i = 0 
                for y in höchste :
                    if x != None and y != None and x != "fold" and y != "fold":
                        try :
                            if x.wert2 > y.wert2 :
                                höchste.remove(y)
                                höchste[i] = "löschen"
                                höchste.remove("löschen")
                        except AttributeError :
                            pass 
                        i += 1

        if len(höchste) > 2 :
            for x in höchste :
                i = 0 
                for y in höchste :
                    if x != None and y != None and x != "fold" and y != "fold":
                        try :
                            if x.wert3 > y.wert3 :
                                höchste.remove(y)
                                höchste[i] = "löschen"
                                höchste.remove("löschen")
                        except AttributeError :
                            pass 
                        i += 1

        if len(höchste) > 2 :
            for x in höchste :
                i = 0 
                for y in höchste :
                    if x != None and y != None and x != "fold" and y != "fold":
                        try :
                            if x.wert4 > y.wert4 :
                                höchste.remove(y)
                                höchste[i] = "löschen"
                                höchste.remove("löschen")
                        except AttributeError :
                            pass 
                        i += 1

        if len(höchste) > 2 :
            for x in höchste :
                i = 0 
                for y in höchste :
                    if x != None and y != None and x != "fold" and y != "fold":
                        try :
                            if x.wert5 > y.wert5 :
                                höchste.remove(y)
                                höchste[i] = "löschen"
                                höchste.remove("löschen")
                        except AttributeError :
                            pass 
                        i += 1

        go1 = True
        while go1 :
            if len(höchste) > 2 :
                i = 0 
                for x in höchste :
                    try :
                        sp = spieler[i]

                        if x != None :
                            m = x.karten_menge
                            while m < 5 :
                                for k in sp.karten2 :
                                    if not k in sp.benutzt :
                                        sp.karte = k
                                        m += 1
                                        break
                                        
                        i += 1

                    except AttributeError :
                        pass 
                    except IndexError :
                        pass

                go2 = True

                for x in spieler :
                    if x.karte == None :
                        go2 = False

                if go2 :
                    i = 0 

                    for x in höchste :
                        try :
                            if spieler[i].karte.name < spieler[i + 1].karte.name :
                                höchste.remove(x)
                                höchste[i] = "löschen"
                                höchste.remove("löschen")
                                nur_none = False
                                break
                            elif spieler[i].karte.name > spieler[i + 1].karte.name :
                                höchste[i + 1] = "löschen"
                                höchste.remove("löschen")
                                
                                höchste[i] = "löschen"
                                höchste.remove("löschen")
                                nur_none = False
                                break
                            else :
                                i += 1 
                        except IndexError :
                            go1 = False
                            break

            if len(höchste) == 2 or len(höchste) == 0 or len(sp.benutzt) == 7 :
                break

        for x in höchste :
            if x != None and x != "fold" :
                nur_none = False

        if len(höchste) > 2 :
            i = 1
            while i < len(höchste) :
                try :
                    if spieler[höchste[i]].imSpiel :
                        gewinner.append(spieler[höchste[i]])
                    i += 2 
                except IndexError :
                    print("Zeile 1257")
                    print(i)
                    print(höchste)

    if nur_none :
        for s in spieler :
            if s.imSpiel :
                gewinner.append(s)

    else :
        if len(höchste) == 2 and höchste[0] == None and höchste[1] == None :
            gewinner.append(spieler[0])
            gewinner.append(spieler[1])

        if gewinner == [] :
            if len(höchste) == 1 :
                gewinner.append(spieler[höchste[0]])
            else :
                try :
                    gewinner.append(spieler[höchste[1]])
                except TypeError :
                    print("Zeile 1277")
                    print(höchste)

    if g :
        zeichne_gewonnen(gewinner, beste)
        pygame.display.update()
        
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT: sys.exit()

            gedrueckt = pygame.key.get_pressed()

            if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER] :
                break

    if len(gewinner) == 1 :
        if gewinner[0].gesetzt2 > 0 :
            gewinner[0].geld += gewinner[0].gesetzt2
            pott -= gewinner[0].gesetzt2
            gewinner[0].imSpiel = False
            return True
        else :
            gewinner[0].geld += int(pott)
            pott = 0
            return False
    else :
        pott -= pott % len(gewinner)
    
        for g in gewinner :
            g.geld += int(pott / len(gewinner))
    
        pott = 0 
        return False


def neue_runde(ge=True) :
    global geboten, pott
    global amZug, dealer
    global first, erst
    global karten, mitte
    global runden
    global small_blind, big_blind

    if ge :
        if not erst :
            g = runde_gewonnen(ge)
            while g :
                g = runde_gewonnen(ge)
        else :
            erst = False

    if len(spieler) >= 6 :
        ok = True
        for s in spieler :
            if not s.war_dealer :
                ok = False
                break

        if ok :
            small_blind *= 2
            big_blind *= 2

            for s in spieler :
                s.war_dealer = False

    elif len(spieler) >= 4 :
        ok = True
        if runden == 1 :
            for s in spieler :
                if not s.war_dealer :
                    ok = False
                    break
            
            if ok :
                small_blind *= 2
                big_blind += 2
        else :
            for s in spieler :
                if not s.war_dealer :
                    ok = False
                    break
            
            if ok :
                runden += 1 
                for s in spieler :
                    s.war_dealer = False
    
    elif len(spieler) < 4 :
        ok = True
        if runden == 2 :
            for s in spieler :
                if not s.war_dealer :
                    ok = False
                    break
            
            if ok :
                small_blind *= 2
                big_blind *= 2 
        else :
            for s in spieler :
                if not s.war_dealer :
                    ok = False
                    break
            
            if ok :
                runden += 1 
                for s in spieler :
                    s.war_dealer = False

    for s in spieler :
        if s.geld == 0 :
            spieler.remove(s)

    gewonnen()

    geboten = big_blind
    pott = 0

    if dealer + 1 < len(spieler) :
        dealer += 1
    else :
        dealer = 0 
    
    spieler[dealer].war_dealer = True

    for s in spieler :
        s.gesetzt2 = 0 
        s.g = 0 
        s.gesetzt = 0
        s.setzen = "0"
        if s.geld > 0 :
            s.imSpiel = True

    stelle = 0 

    if len(spieler) > 2 :
        if dealer + 1 > len(spieler) - 1 :
            spieler[0].gesetzt = small_blind
            spieler[0].geld -= small_blind
            stelle = 1
        else :
            spieler[dealer + 1].gesetzt = small_blind
            spieler[dealer + 1].geld -= small_blind

        if dealer + 2 > len(spieler) - 1 :
            spieler[stelle].gesetzt = big_blind
            spieler[stelle].geld -= big_blind
        else :
            spieler[dealer + 2].gesetzt = big_blind
            spieler[dealer + 2].geld -= big_blind
    else :
        spieler[dealer].gesetzt = small_blind
        spieler[dealer].geld -= small_blind

        if dealer + 1 > len(spieler) - 1 :
            spieler[0].gesetzt = big_blind
            spieler[0].geld -= big_blind
            stelle = 1
        else :
            spieler[dealer + 1].gesetzt = big_blind
            spieler[dealer + 1].geld -= big_blind

    if dealer + 3 > len(spieler) - 1 :
        if len(spieler) == 2 :
            if dealer == 0 :
                amZug = 0 
            else :
                amZug = 1
        else :
            if dealer + 3 == len(spieler) :
                amZug = 0
            elif dealer + 3 == len(spieler) + 1 :
                amZug = 1
            elif dealer + 3 == len(spieler) + 2 :
                amZug = 2
    else :
        amZug = dealer + 3

    first = True

    niedriger.clear()
    karten = [kreuz_Ass, kreuz_König, kreuz_Dame, kreuz_Bube, kreuz_10, kreuz_9, kreuz_8, kreuz_7, kreuz_6, kreuz_5, kreuz_4, kreuz_3, kreuz_2, piek_Ass, piek_König, piek_Dame, piek_Bube, piek_10, piek_9, piek_8, piek_7, piek_6, piek_5, piek_4, piek_3, piek_2, herz_Ass, herz_König, herz_Dame, herz_Bube, herz_10, herz_9, herz_8, herz_7, herz_6, herz_5, herz_4, herz_3, herz_2, caro_Ass, caro_König, caro_Dame, caro_Bube, caro_10, caro_9, caro_8, caro_7, caro_6, caro_5, caro_4, caro_3, caro_2]
    mitte = []

    karten_generieren()

    zeichne()

    screen.blit(karte_geschlossen_b, feld1)
    screen.blit(karte_geschlossen_b, feld2)

    pygame.display.update()

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT: sys.exit()

        gedrueckt = pygame.key.get_pressed()

        if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER] :
            break

def karten_aufdecken() :
    global first

    if first :
        i = 0 
        while i <= 2 :
            rand = randint(0, len(karten) - 1)
            k = karten[rand]
            mitte.append(k)
            karten.remove(k)
            i += 1 
        first = False
    else :
        rand = randint(0, len(karten) - 1)
        k = karten[rand]
        mitte.append(k)
        karten.remove(k)

def rundenende() :
    global pott, geboten

    ok = True

    for s in spieler :
        if s.gesetzt != geboten and s.imSpiel and s.geld > 0 :
            ok = False
            break

    for w in spieler :
        if not w.war_dran :
            ok = False
            break

    if ok :
        if len(mitte) < 5 :
            for i in spieler :
                pott += i.gesetzt
                i.gesetzt = 0
                if i.imSpiel :
                    i.war_dran = False
            
            geboten = 0 

            karten_aufdecken()
        else :
            gewonnen()
            neue_runde()
            for s in spieler :
                s.war_dran = False

def gewonnen() :
    global amZug

    if len(spieler) == 1 :
        amZug = 0 
        zeichne()
        pygame.display.update()

        pygame.time.wait(500)
        
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT: sys.exit()

            gedrueckt = pygame.key.get_pressed()

            for b in gedrueckt :
                if b == 1 :
                   sys.exit()

def funk_all_all_in() :
    global pott

    a = 0 
    for s in spieler :
        if s.imSpiel :
            a += 1 

    for s in spieler :
        pott += s.gesetzt
        s.gesetzt = 0 

    l = []

    for s in spieler :
        l.append(s.blatt[0].bild)
        l.append(s.blatt[1].bild)

    if a > 1 :
        while len(mitte) < 5 :
            karten_aufdecken()
            zeichne_all_in()
            pygame.display.update()

            while True :
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT: sys.exit()
                
                gedrueckt = pygame.key.get_pressed()
                if gedrueckt[pygame.K_RETURN] or gedrueckt[pygame.K_KP_ENTER] :
                    pygame.time.wait(300)
                    break
    
        neue_runde()
    else :
        neue_runde(False)
    

feld1 = (350,671)
feld2 = (510,671)

dealer = -1

small_blind = 5
big_blind = 10

runden = 0 

first = True
erst = True
all_all_in = False

mitte = []
niedriger = []

neue_runde()

go = True
while go :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN :
        spieler[amZug].mausklick()

    for s in spieler :
        if s.geld > 0 and s.imSpiel :
            for s2 in spieler :
                if s2.geld > 0 and s2.imSpiel and s2 != s :
                    all_all_in = False

    for s in spieler :
        if s.gesetzt != geboten and s.imSpiel and s.geld > 0 :
            all_all_in = False

    if all_all_in :
        funk_all_all_in()

    zeichne()
    spieler[amZug].tippen()
    rundenende()
    pygame.display.update()

    if spieler[amZug].art == "Ki" :
        spieler[amZug].machen()

    if not spieler[amZug].imSpiel or spieler[amZug].geld == 0 :
        if amZug + 1 < len(spieler) :
            amZug += 1 
        else :
            amZug = 0

    all_all_in = True