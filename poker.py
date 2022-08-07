class Card():
    
    image_dict = {"Maça": "S", "Karo": "D", "Kupa": "H", "Sinek": "C"}
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def image_file(self):
        if self.number != 1 and self.number < 11:
            image = pygame.image.load(f"PNG/{self.number}{self.image_dict[self.type]}.png")
            image = pygame.transform.scale(image, (104, 159))
            return image
        elif self.number == 1:
            image = pygame.image.load(f"PNG/A{self.image_dict[self.type]}.png")
            image = pygame.transform.scale(image, (104, 159))
            return image
        elif self.number == 11:
            image = pygame.image.load(f"PNG/J{self.image_dict[self.type]}.png")
            image = pygame.transform.scale(image, (104, 159))
            return image
        elif self.number == 12:
            image = pygame.image.load(f"PNG/Q{self.image_dict[self.type]}.png")
            image = pygame.transform.scale(image, (104, 159))
            return image
        elif self.number == 13:
            image = pygame.image.load(f"PNG/K{self.image_dict[self.type]}.png")
            image = pygame.transform.scale(image, (104, 159))
            return image

    def print(self):
        print(self.type, self.number)
    def getstr(self):
        if self.number < 11 and self.number != 1:
            return self.type + " " + str(self.number)
        elif self.number == 11:
            return self.type + " J"
        elif self.number == 1:
            return self.type + " A"
        elif self.number == 12:
            return self.type + " Q"
        elif self.number == 13:
            return self.type + " K"

class Deck():
    cards = []
    def __init__(self):
        for i in range(13):
            self.cards.append(Card("Maça", i+1))
        for i in range(13):
            self.cards.append(Card("Kupa", i+1))
        for i in range(13):
            self.cards.append(Card("Sinek", i+1))
        for i in range(13):
            self.cards.append(Card("Karo", i+1))
    def drawCards(self, n):
        cardsDrawn = []
        for i in range(n):
            from random import randint
            random = randint(0, len(self.cards)-i-1)
            cardsDrawn.append(self.cards.pop(random))
        return cardsDrawn
    def print(self):
        for i in range(len(self.cards)):
            self.cards[i].print()
class Besli():
    cards = []
    def __init__(self, deck):
        self.cards = deck.drawCards(5)
    def print(self):
        for i in range(len(self.cards)):
            self.cards[i].print()
class El():
    cards = []
    def __init__(self, deck):
        self.cards = deck.drawCards(2)
    def print(self):
        for i in range(len(self.cards)):
            self.cards[i].print()     
class Yedili():
    pairValue = 0
    secondPairValue = 0
    straightValue = 0
    def __init__(self, besli, el):
        self.cards = []
        self.cardValues = []
        self.cards.extend(besli.cards)
        self.cards.extend(el.cards)
        for card in self.cards:
            self.cardValues.append(card.number)
    def changecards(self, cards):
        self.cardValues = []
        for i in range(7):
            self.cards[i] = cards[i]
            self.cardValues.append(cards[i].number)
    def flush(self):
        macacount = 0
        kupacount = 0
        karocount = 0
        sinekcount = 0
        for card in self.cards:
            if card.type == "Maça":
                macacount += 1
            elif card.type == "Kupa":
                kupacount += 1
            elif card.type == "Karo":
                karocount += 1
            elif card.type == "Sinek":
                sinekcount += 1
        return macacount >= 5 or kupacount >= 5 or karocount >= 5 or sinekcount >= 5
    def straight(self):
        straight = 0
        straightas = 0
        for j in range(9):
            for i in range(5):
                if i+j+1 in self.cardValues:
                    potentialStraightValue = i+j+1
                    straight += 1
                if straight == 5:
                    self.straightValue = potentialStraightValue
                    return "Normal straight"
            straight = 0
        for i in range(10,14):
            if i in self.cardValues:
                straightas += 1
            if straightas == 4 and 1 in self.cardValues:
                return "Royal straight"
        return "Yok"
    def value(self):
        numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in self.cards:
            number = card.number
            numbers[number - 1] += 1
        if self.flush() and self.straight() == "Royal straight":
            return 9
        elif self.flush() and self.straight() == "Normal straight":
            return 8
        elif 4 in numbers:
            self.pairValue = numbers.index(4) + 1
            return 7
        elif 3 in numbers and 2 in numbers:
            self.pairValue = numbers.index(3) + 1
            return 6
        elif self.flush():
            return 5
        elif self.straight() == "Royal straight" or self.straight() == "Normal straight":
            return 4
        elif 3 in numbers:
            self.pairValue = numbers.index(3) + 1
            return 3
        elif 2 in numbers:
            potpairvalue1 = numbers.index(2)
            numbers.remove(2)
            if 2 in numbers:
                potpairvalue2 = numbers.index(2)
                self.pairValue = max(potpairvalue1, potpairvalue2)
                self.secondPairValue = min(potpairvalue1, potpairvalue2)
                return 2
            else:
                self.pairValue = potpairvalue1
                return 1
        else:
            return 0
    def getValue(self):
        values = ["Nothing", "Pair", "Deux Pairs", "Three of a kind", "Straight", 
        "Flush", "Full House", "Four of a kind", "Straight Flush", "Royal Flush"]
        return values[self.value()]
    def print(self):
        for i in range(len(self.cards)):
            self.cards[i].print()
    def getstr(self, a, b):
        str = ""
        for i in range(a, b):
            str += self.cards[i].getstr()
            str += "\n"
        return str
def compareNumbers(num1, num2):
    if num1 > num2:
        return 1
    elif num2 > num1:
        return 2
    else:
        return 0
def compareHighCard(list1, list2):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    for i in range(len(list1)):
        if compareNumbers(list1[i], list2[i]) != 0:
            return compareNumbers(list1[i], list2[i])
def compareYedilis(bir, iki):
    if bir.value() > iki.value():
        return 1
    elif iki.value() > bir.value():
        return 2
    elif bir.value() == iki.value():
        if bir.value() == 0:
            return compareHighCard(bir.cardValues, iki.cardValues)
        elif bir.value() == 1 or bir.value() == 3 or bir.value() == 6 or bir.value() == 7:
            if compareNumbers(bir.pairValue, iki.pairValue) != 0:
                return compareNumbers(bir.pairValue, iki.pairValue)
            else:
                return compareHighCard(bir.cardValues, iki.cardValues)
        elif bir.value() == 2:
            if compareNumbers(bir.pairValue, iki.pairValue) != 0:
                return compareNumbers(bir.pairValue, iki.pairValue)
            elif compareNumbers(bir.secondPairValue, iki.secondPairValue) != 0:
                return compareNumbers(bir.secondPairValue, iki.secondPairValue)
            else:
                return compareHighCard(bir.cardValues, iki.cardValues)
        elif bir.value() == 4 or bir.value() == 8:
            if compareNumbers(bir.straightValue, iki.straightValue) != 0:
                return compareNumbers(bir.straightValue, iki.straightValue)
            else:
                return compareHighCard(bir.cardValues, iki.cardValues)
        elif bir.value() == 5:
            return compareHighCard(bir.cardValues, iki.cardValues)
    else:
        return 0
"""
changedCards1 = [Card("Maça", 4), Card("Kupa", 3), Card("Sinek", 10), Card("Karo", 6), 
Card("Maça", 5), Card("Maça", 1), Card("Maça", 2)]
changedCards2 = [Card("Maça", 4), Card("Kupa", 3), Card("Sinek", 10), Card("Karo", 6), 
Card("Maça", 5), Card("Maça", 5), Card("Maça", 9)]
"""
yedili1 = 0
yedili2 = 0
el1 = 0
el2 = 0
besli = 0
deck = 0
def dagit():
    global deck
    deck = Deck()
    global besli
    besli = Besli(deck)
    global el1
    el1 = El(deck)
    global el2
    el2 = El(deck)
    global yedili1
    yedili1 = Yedili(besli, el2)
    global yedili2
    yedili2 = Yedili(besli, el1)

valuelist = [0,0,0,0,0,0,0,0,0,0]
for i in range(10000):
    dagit()
    valuelist[yedili1.value()] += 1
print(valuelist)

import sys, pygame
pygame.init()
size = width, height = 820, 580
screen = pygame.display.set_mode(size)
green = 5, 105, 19
white = 255, 255, 255
lacivert = 10, 41, 142
font = pygame.font.SysFont('MS PMincho', 25, True, False)
#pygame.mixer.music.load("Tico Tico.mp3")
#pygame.mixer.music.play(-1)
dagit()
image1 = el1.cards[0].image_file()
image2 = el1.cards[1].image_file()
card1 = besli.cards[0].image_file()
card2 = besli.cards[1].image_file()
card3 = besli.cards[2].image_file()
card4 = besli.cards[3].image_file()
card5 = besli.cards[4].image_file()
opcard1 = el2.cards[0].image_file()
opcard2 = el2.cards[1].image_file()
text1 = font.render(f"You have: {yedili2.getValue()}", True, white)
text2 = font.render(f"Opponent has: {yedili1.getValue()}", True, white)
text3 = font.render("You win!", True, white)
text4 = font.render("You lose!", True, white)
text5 = font.render("It's a draw!", True, white)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > 720 and pygame.mouse.get_pos()[1] > 530:
                dagit()
                image1 = el1.cards[0].image_file()
                image2 = el1.cards[1].image_file()
                card1 = besli.cards[0].image_file()
                card2 = besli.cards[1].image_file()
                card3 = besli.cards[2].image_file()
                card4 = besli.cards[3].image_file()
                card5 = besli.cards[4].image_file()
                opcard1 = el2.cards[0].image_file()
                opcard2 = el2.cards[1].image_file()
                text1 = font.render(f"You have: {yedili2.getValue()}", True, white)
                text2 = font.render(f"Opponent has: {yedili1.getValue()}", True, white)
                text3 = font.render("You win!", True, white)
                text4 = font.render("You lose!", True, white)
                text5 = font.render("It's a draw!", True, white)
    screen.fill(green)
    
    screen.blit(image1, [305, 421])
    screen.blit(image2, [410, 421])
    
    screen.blit(card1, [150, 210])
    screen.blit(card2, [255, 210])
    screen.blit(card3, [360, 210])
    screen.blit(card4, [465, 210])
    screen.blit(card5, [570, 210])

    screen.blit(opcard1, [305, 0])
    screen.blit(opcard2, [410, 0])

    screen.blit(text1, [530, 450])
    screen.blit(text2, [530, 30])
    
    if compareYedilis(yedili1, yedili2) == 2:
        screen.blit(text3, [700, 250])
    elif compareYedilis(yedili1, yedili2) == 1:
        screen.blit(text4, [700, 250])
    elif compareYedilis(yedili1, yedili2) == 0:
        screen.blit(text5, [700, 250])
    pygame.draw.rect(screen, lacivert, (720, 530, 100, 50))
    refresh = font.render("Refresh", False, white)
    screen.blit(refresh, [735, 545])

    pygame.display.flip()

