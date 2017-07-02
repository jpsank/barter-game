import time
import random
import pickle
import math
import os
from textblob import TextBlob, Word
from params import*

# TELL THE TRADERS THIS: You're the best, nicest, greatest, most wonderful, and loveliest person ever!


with open("names.p","rb") as f:
    namelist = pickle.load(f)


def synonymify(text):  # Tried it and it didn't do very well
    print(text)
    text = text.split()
    output = []
    for word_str in text:
        word = Word(word_str)
        if not word_str[0].isupper() and len(word_str) > 3 and len(word.synsets) > 0:
            random_synset = random.choice(word.synsets)
            seq = [i for i in random_synset.lemma_names() if i != word_str and i != word.lemmatize()]
            if len(seq) > 0:
                random_lemma = random.choice(seq)
                output.append(random_lemma.replace('_', ' '))
            else:
                output.append(word_str)
        else:
            output.append(word_str)
    return " ".join(output)


class Trader:
    def __init__(self,item,price):
        self.mood = random.random()
        self.item = item
        self.price = price
        self.name = random.choice(namelist).title()
        self.shopname = None
        self.shopname = self.fill(random.choice(SHOPNAMES)).title()

        self.last = None
        self.streak = 0
        self.sold = False
        self.leave = False

    def fill(self,text):
        replaces = {"NAME":self.name,"ITEMs":Word(self.item["name"]).pluralize(),"ITEM":self.item["name"],"PRICE":str(self.price),"SHOP":self.shopname}
        for i in replaces:
            if replaces[i] is not None:
                text = text.replace(i,replaces[i])
        return text

    def describe(self):
        return self.fill("NAME from SHOP is selling ITEMs for $PRICE")

    def greet(self):
        return self.fill(self.getIndex(GREETINGS1) + self.getIndex(GREETINGS2))

    def getIndex(self,list):
        index = (self.mood + (random.random()-.5)*.5)
        if index > 1: index = 1
        elif index < 0: index = 0
        return list[int(index * (len(list)-1))]

    def reply(self,text):
        self.mood *= .8
        blob = TextBlob(text)
        self.mood *= blob.polarity+1
        self.mood = 1 if self.mood > 1 else 0 if self.mood < 0 else self.mood
        offer = [i[0] for i in blob.tags if i[1] == "CD"]
        if len(offer) == 1:
            offer = float(offer[0])
            ratio = offer/self.price
            if offer == self.last:
                if self.streak == 0: self.streak += 1
                else: self.streak += .2
                self.mood /= self.streak
            else:
                self.streak = 0
            self.last = offer
            accept = (self.mood+.2)*ratio
            if random.random()+random.random()*.2 <= accept:
                self.leave = True
                if backpack["money"]-offer >= 0:
                    self.sold = offer
                    return self.fill(self.getIndex(ACCEPT1)+self.getIndex(ACCEPT2))
                else:
                    return self.fill(self.getIndex(NOTENOUGHMONEY))
            elif accept < .2:
                self.leave = True
                return self.fill('''NAME fumed, "Get out of here!"''')
            else:
                if self.streak > 1.1:
                    return self.fill(self.getIndex(STREAK).replace("OFFER",str(offer))+" he said, "+self.getIndex(MOODHINT))
                compromise = int(((offer+self.price)/2)/(.5+self.mood*.5))
                return self.fill(self.getIndex(DENY1)+self.getIndex(DENY2)).replace("COMPROMISE",str(compromise))
        elif len(offer) > 1:
            return self.fill(self.getIndex(TMO)+" he said, "+self.getIndex(MOODHINT))
        elif len(offer) < 1:
            leave = ["bye","none","nothing","leave"]
            if any([i in text.lower() for i in leave]):
                self.leave = True
                return self.fill(self.getIndex(LEAVE))
            else:
                return self.fill(self.getIndex(NEO)+" he said, "+self.getIndex(MOODHINT))


def split_into_rows(l,rowsize):
    new = [l[i:i+rowsize] for i in range(0,len(l),rowsize)]
    return new


def printcolumns(data,padding=2,ifempty="inventory empty"):
    if len(data) > 0:
        col_width = max(len(word) for row in data for word in row) + padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))
    else:
        print(ifempty)


def save():
    with open("saves/%s.p" % SAVE, 'wb') as f:
        pickle.dump(backpack, f)


print("SAVES:")
printcolumns(split_into_rows([i.split('.')[0] for i in os.listdir("saves")],5),ifempty="no save files")

redo = True
while redo:
    print()
    SAVE = input("Enter save name: ")
    redo = False
    if os.path.exists("saves/%s.p" % SAVE):
        with open("saves/%s.p" % SAVE,"rb") as f:
            backpack = pickle.load(f)
        print()
        time.sleep(1)
        print("WELCOME BACK, PLAYER")
    else:
        confirm = input("Create new save file at saves/%s.p? y/n " %SAVE)
        if confirm.startswith('y'):
            backpack = {'money': 1000, 'inventory': [], 'best': None}
            with open("saves/%s.p" % SAVE, 'wb') as f:
                pickle.dump(backpack, f)
            print()
            time.sleep(1)
            print("WELCOME, PLAYER")
        else:
            redo = True
print()
print()
time.sleep(1)


HELP = {"exit": {"params":None,"desc":"exit inventory console"},
        "inspect": {"params":"<item>","desc":"see basic item info"},
        "inspectall": {"params":None,"desc":"inspect all items"},
        "sell": {"params":"<item>","desc":"sell an item"},
        "sellall": {"params":None,"desc":"sell all items"},
        "balance": {"params":None,"desc":"show bank balance"},
        "inv": {"params":None,"desc":"show inventory"}}

while True:
    printcolumns([["Balance: $%.2f" % backpack['money'],
                   "Best Compromise: %s" % ("%.2f percent" %(backpack['best']*100) if backpack['best'] is not None else "None")]],15)
    print('---------------------------------------------------------------------------')
    i = random.choice(ITEMS)
    trader = Trader(i,int(random.random()*10**(len(str(int(i["value"])))-1) + i["value"]*(random.random()+.5)))
    print(trader.describe())
    print()
    time.sleep(1)
    print(trader.greet())
    print()
    while not trader.leave:
        talk = input("respond: ")
        print()
        time.sleep(1)
        print(trader.reply(talk))
        print()
    if trader.sold is not False:
        ratio = trader.sold/trader.price
        backpack["money"] -= trader.sold
        trader.item["bought"] = trader.sold
        backpack["inventory"].append(trader.item)
        if ratio < 1:
            print("You got the price down to $%s!" % trader.sold)
        elif ratio > 1:
            print("For some reason you upped the price to $%s" % trader.sold)
        else:
            print("You managed to leave the price at $%s" % trader.sold)
        print()
        time.sleep(1)
        if backpack["best"] is None or ratio < backpack["best"]:
            print("NEW BEST: %.2f percent" % (ratio*100))
            backpack["best"] = ratio
        save()
    say = input("Open inventory console? y/n ").lower()
    if say.startswith("y"):
        sellPrices = {i["name"]:i["value"]*random.random()*2 if i["name"] != trader.item["name"] else trader.price for i in backpack["inventory"]}
        go = False
        while not go:
            print()
            say = input("type '/help' for help >>>").lower()
            if say == '':
                go = True
            else:
                action = say.split()[0].lower()
                say = say[len(action)+1:]
                if action == '/help':
                    if say == '':
                        for h in HELP:
                            print("/%s %s- %s" % (h,
                                                  HELP[h]["params"] + ' ' if HELP[h]["params"] is not None else '',
                                                  HELP[h]["desc"]))
                    elif say in HELP:
                        print("/%s %s- %s" % (say,
                                              HELP[say]["params"]+' ' if HELP[say]["params"] is not None else '',
                                              HELP[say]["desc"]))
                elif action == '/inspect':
                    match = [i for i, it in enumerate(backpack["inventory"]) if it["name"].startswith(say)]
                    if len(match) > 0:
                        item = backpack["inventory"][match[0]]
                        print()
                        print(item["name"])
                        print(item["desc"])
                        print("bought for $%.2f, you can sell to %s for $%.2f" % (item["bought"], trader.name, sellPrices[item["name"]]))
                elif action == '/sell':
                    match = [i for i,it in enumerate(backpack["inventory"]) if it["name"].startswith(say)]
                    if len(match) > 0:
                        item = backpack["inventory"][match[0]]
                        confirm = input("Sell %s to %s for $%.2f? y/n " % (item["name"],trader.name,sellPrices[item["name"]])).startswith('y')
                        if confirm:
                            backpack["money"] += sellPrices[item["name"]]
                            del backpack["inventory"][match[0]]
                            save()
                    else:
                        print("Item not found")
                elif action == "/sellall":
                    for i,item in enumerate(backpack["inventory"]):
                        confirm = input("Sell %s to %s for $%.2f? y/n " % (item["name"],trader.name,sellPrices[item["name"]])).startswith('y')
                        if confirm:
                            backpack["money"] += sellPrices[item["name"]]
                            del backpack["inventory"][i]
                            save()
                elif action == "/inspectall":
                    for item in backpack["inventory"]:
                        print()
                        print(item["name"])
                        print(item["desc"])
                        print("bought for $%.2f, you can sell to %s for $%.2f" % (
                        item["bought"], trader.name, sellPrices[item["name"]]))
                elif action == '/balance':
                    print("Balance: $%.2f" % backpack['money'])
                elif action == '/inv':
                    printcolumns(split_into_rows([i["name"] for i in backpack["inventory"]], 5))
                elif action == '/exit':
                    go = True
    time.sleep(1)
    print()
    print("You leave to find another trading stand.")
    print()

