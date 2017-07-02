

ITEMS = [
    {"name":"soggy cardboard", "value":1, "desc":"less than completely useless"},
    {"name":"dry cardboard", "value":2, "desc":"completely useless"},
    {"name":"hardened flower petal", "value":3, "desc":"or you could call it a dead flower petal"},
    {"name":"disappointment potion", "value":11, "desc":"it doesn't work"},
    {"name":"potion of thirst-quenching", "value":10, "desc":"it's called water"},
    {"name":"hollow rock", "value":5, "desc":"there's nothing inside"},
    {"name":"artificial cloud generator", "value":15, "desc":"it boils water"},
    {"name":"sharpened blade of grass", "value":6, "desc":"disclaimer, use a different sword, this one breaks easily"},
    {"name":"troll skin", "value":21, "desc":"fresh from the cheese grater"},
    {"name":"grilled worm steak", "value":25, "desc":"tastes just as good as normal steak"},
    {"name":"moldy piece of cake", "value":14, "desc":"eat at your own risk"},
    {"name":"canned walmart bag", "value":10, "desc":"walmart bags carry groceries, this carries walmart bags!"},
    {"name":"bottled water bottle", "value":9, "desc":"just in case you spill it"},
    {"name":"beaned beef", "value":13, "desc":"beef filled with beans"},
    {"name":"nutty squirrel", "value":27, "desc":"normal squirrel, only eats acorns"},
    {"name":"slug butter", "value":23, "desc":"rich and creamy"},
    {"name":"cat juice", "value":31, "desc":"what is it? think of squeezing lemons"},
    {"name":"crushed eyeball soup", "value":26, "desc":"it takes precision to crush eyeballs"},
    {"name":"old cheese", "value":30, "desc":"this cheese is ready for the slaughterhouse"},
    {"name":"young cheese", "value":34, "desc":"don't eat it yet, it's just a baby!"},
    {"name":"flour patch kids", "value":36, "desc":"for flour-y people, not sour-y people!"},
    {"name":"canned artificial flavoring", "value":42, "desc":"tastes like chicken! Or anything, really"},
    {"name":"empty recycling box", "value":33, "desc":"you have to find a way to make people fill it"},
    {"name":"book of spells", "value":35, "desc":"#1 wizard recommended spellbook"},
    {"name":"normal toilet seat", "value":40, "desc":"you were either relieved or confused when you saw the word 'normal' before toilet seat (or possibly unhappy, in which case you must be very bored)"},
    {"name":"godly piece of cake", "value":64, "desc":"use it wisely"},
    {"name":"golden toilet seat", "value":102, "desc":"you thought it was real gold! HA"},
    {"name":"unicorn sprinkles", "value":121, "desc":"no unicorns were harmed in the making of these sprinkles"},
    {"name":"100 dalmatians", "value":101, "desc":"we didn't have room for that last one"},
    {"name":"radioactive kitten paw", "value":120, "desc":"contains small amount of uranium"},
    {"name":"3000-year-old water", "value":3000, "desc":"NEWEST WATER IN THE UNIVERSE"},
    {"name":"weasel stomping boots", "value":631, "desc":"titanium soles, automagically detects weasels and brings you to them"},
    {"name":"sparkling gemstone water", "value":420, "desc":"melted gemstones + water"},
    {"name":"gold from the end of the rainbow", "value":777, "desc":"a rainbow was monitored and tracked carefully (by lunatics) to locate this gold"},
    {"name":"blue swedish fish", "value":19.99, "desc":"this color of swedish fish is nearly impossible to find in the wild"},
    {"name":"letter cube", "value":26, "desc":"it has all the letters"},
    {"name":"completed number cube", "value":123, "desc":"it has all the numbers"},
    {"name":"sentient toilet seat", "value":111, "desc":"I'd be nice to it if I were you"},
    {"name":"all-seeing toilet seat", "value":666, "desc":"now it can see you even when you aren't sitting on it"},
    {"name":"fancy squirrel", "value":420, "desc":"sometimes eats things more expensive than acorns (you'd better keep track of its poop)"},
    {"name":"gold ring", "value":79, "desc":"it's a ring made of gold"},
    {"name":"unicorn poop", "value":23.22, "desc":"I found a piece of chocolate! my unicorn dropped it"},
    {"name":"time machine", "value":77403, "desc":"now you just have to find the keys"},
    {"name":"fancy feast", "value":2+2, "desc":"gives your cats superpowers"},
    {"name":"dodo bird", "value":1662, "desc":"as dead as a dodo"}
]
# template: {"name":"", "value":1, "desc":""},

SHOPNAMES = [
    "NAME's Shop Stop",
    "NAME's Garage",
    "NAME Marketing",
    "NAME World",
    "NAME's ITEM Palace",
    "Easy NAME",
    "NAME Express",
    "ITEM Express",
    "Best ITEMs",
    "NAME's ITEMs",
    "ITEM House",
    "ITEM Store",
    "ITEMs Now",
    "NAME's ITEM Store",
    "NAME's ITEM Stand",
    "ITEM World",
    "NAME ITEMs",
    "NAME's Better ITEMs",
    "NAME's ITEM Sale",
    "ITEMs R Us"
]

GREETINGS = [
    '''"What's up, customer?" NAME said, "Not my prices!"''',
    '''"What a lovely day," NAME said, "to buy my ITEMs!"''',
]

GREETINGS1 = [
    '''"What do you want?" NAME grumbled. ''',
    '''"Okay, you came to my shop," NAME shrugged. ''',
    '''"My name's NAME," said NAME. ''',
    '''"I'm NAME," said NAME. ''',
    '''"Hello human, welcome to SHOP, where I sell things to people!" NAME said, ''',
    '''"What a lovely day," said NAME. ''',
    '''"Fine day to buy from me!" NAME exclaimed. ''',
    '''"Good day, customer," NAME said cheerfully. ''',
    '''"Hello!" said NAME. ''',
    '''"A beautiful customer has come!!" NAME yelped happily. '''
]
GREETINGS2 = [
    '''"Gimme money."''',
    '''"Got any money?"''',
    '''"I'm rather hungry, and if I can't buy food, you're the next choice."''',
    '''"How much you gonna pay?"''',
    '''"Buy my ITEMs today!"''',
    '''"You should probably give me some money!"''',
    '''"Came for the ITEM, did ya?"''',
    '''"Welcome to SHOP!"''',
]


# Too many offers
TMO = [
    '''NAME: "One price, you idiot"''',
    '''NAME mocked you, "I think one price should do,"''',
    '''NAME: "The price is a very confusing subject, yes?"''',
    '''NAME sighed, "Only one price is needed"''',
    '''NAME: "Uhhh.. wat?"''',
    '''NAME: "Sorry?"''',
    '''NAME: "What you say?"''',
    '''NAME: "What was that?"'''
]

# Not enough offers
NEO = [
    '''NAME: "Give me a price, you imbecile!"''',
    '''NAME: "A price??!"''',
    '''NAME: "Offer your price!"''',
    '''NAME: "What price would you like?"''',
    '''NAME: "You like my ITEM? I'll give it to you cheap!"''',
    '''NAME: "How may I help you, and how much money can I get from you?"''',
    '''NAME smiled: "What's your offer?"'''
]

# Hint at trader's mood
MOODHINT = [
    '''"I'm angry!!"''',
    '''"are you an idiot?!"''',
    '''"or you'll get nothing."''',
    '''"it's a good day to buy a ITEM!"''',
    '''"I'm starting to like you."''',
    '''"you are a fine sir!"''',
    '''smiling, "I knew you were going to be one of the good ones!"'''
]

# Accept the offer
ACCEPT1 = [
    "NAME nodded. ",
    "NAME smiled. ",
    "NAME grinned. ",
    "NAME clapped. "
]
ACCEPT2 = [
    '''"I'll accept that"''',
    '''"That's about right!"''',
    '''"I'll take it!"''',
    '''"Thanks for buying at SHOP!"''',
    '''"Have a great day!"'''
]

# Deny the offer
DENY1 = [
    "NAME snarled. ",
    "NAME scoffed. ",
    "NAME frowned and narrowed his eyes. ",
    "NAME disagreed. ",
    "NAME shook his head. ",
    "NAME thought. ",
    "NAME hesitated. "
]
DENY2 = [
    '''"Outrageous! Get out!"''',
    '''"You think I'm dumb?"''',
    '''"I don't think so."''',
    '''"$COMPROMISE, nothing more, nothing less."''',
    '''"I will take $COMPROMISE."''',
    '''"How about $COMPROMISE?"''',
    '''"I'm thinking $COMPROMISE?"''',
    '''"What about $COMPROMISE?"'''
]


# Player decides to leave
LEAVE = [
    '''"You want nothing?", he said, "Good riddens! Leave at once!"''',
    '''NAME: "Begone then, human!"''',
    '''"What?" he stammered, "b-but how could you not desire my beautiful ITEM?!"''',
    '''NAME: "Goodbye!"''',
    '''NAME: "Come back soon!"''',
    '''NAME smiled, "Hope to see you again!"''',
    '''NAME: "Don't leave, friend! NOOOOOOO!"'''
]

NOTENOUGHMONEY = [
    '''NAME: "You idiot! You don't have enough money!"''',
    '''NAME: "You can't afford that! Get out!"''',
    '''NAME: "You're gonna need more money to buy that"''',
    '''NAME: "Sorry, you don't have enough gold for that"''',
    '''NAME: "Oh, you need more gold to buy that. Sorry!"'''
]

# Player keeps saying the same offer
STREAK = [
    '''NAME: "Give me a better offer or you're out!"''',
    '''NAME: "How many times are you gonna offer the same price?!"''',
    '''NAME: "You know, just saying the same offer over again won't work,"''',
    '''NAME: "That's the same offer as last time!"''',
    '''NAME: "You already said that!"''',
    '''NAME: "You're gonna have to offer something other than $OFFER,"'''
]