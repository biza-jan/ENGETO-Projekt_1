# Main code / to co se bude pouzivat v celem kodu, tj. oddelovace, specialni znaky...
separator = '-' * 35
Title = 0
Upper = 0
Lower = 0
Numeric = 0
Temp = 0
SumNum = 0

# Login / prihlaseni
USERS = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# input username and password / zadani uzivatele a hesla + kontrola uzivatele
# 1. Vyžádá si od uživatele přihlašovací jméno a heslo.
# 2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
username = input('username: ')
password = input('password: ')


if USERS.get(username) == password:
    print(separator)
elif not USERS.get(username) == password:
    print('Username or password is wrong!')
    exit()
else:
    print('Something is wrong. Contact support!')
    exit()

# Welcome user / uvitani uzivatele
# 3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.
print('Welcome to the app,', username)
print('We have 3 text to be analyzed')
print(separator)

# Main program / vlastni program k analyze

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
# user choice no. of text / vyber textu
# 4. Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
choice = int(input('Enter a number btw. 1 and 3 to select: '))
if choice <= 3 and choice >= 1:
    pass
else:
    print('Your choice is not available')
    exit()
print(separator)

# 5. Pro vybraný text spočítá následující statistiky:
if choice == int(1):
    TEXT = TEXTS[0]
elif choice == int(2):
    TEXT = TEXTS[1]
elif choice == int(3):
    TEXT = TEXTS[2]
else:
    print('Something is wrong')

# pocet slov
Count_words = int(len(TEXT.split()))
# počet slov začínajících velkým písmenem,
for Word in TEXT.split():
    if Word.istitle():
        Title = Title + 1
# počet slov psaných velkými písmeny,
    elif Word.isupper():
        Upper = Upper + 1
# počet slov psaných malými písmeny,
    elif Word.islower():
        Lower = Lower + 1
# počet čísel (ne cifer),
    elif Word.isnumeric():
        Numeric = Numeric + 1
    else:
        pass
# sumu všech čísel (ne cifer) v textu.
for Word in TEXT.split():
    if (Word.isnumeric()):
        Temp += Word
    else:
        SumNum += int(Temp)
        Temp = '0'

print('There are', Count_words, 'words in the selected text.')
print('There are', Title, 'titlecase words.')
print('There are', Upper, 'uppercase words.')
print('There are', Lower, 'lowercase words.')
print('There are', Numeric, 'numeric strings.')
print('The sum of all the numbers', SumNum)
print(separator)

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:

# ocistim o znaky ,.?! atd.
TEXT = TEXT.translate({ord(c): None for c in ',.?!'})

# vytvorim list s delkami slov
TEXT_graph = []
for x in TEXT.split():
    word_length = len(x)
    TEXT_graph.append(word_length)

# z listu vytvorim slovnik
i = TEXT_graph
TEXT_graph_dict = {x:i.count(x) for x in i}

# seradim slovnik
TEXT_graph_dict_sort = sorted(TEXT_graph_dict.items())

# vytisknu slovnik do grafu
print('LEN| OCCURENCES        |NR.')
print(separator)
LEN = ''
OCC = ''
NR = ''
for k, v in TEXT_graph_dict_sort:
    LEN = '{:<2}'.format(k)
    OCC = '{:<17}'.format('*' * v)
    NR = '{:<2}'.format(v)
    print(LEN, '|', OCC, '|', NR)

# code by Jan Biza in 26th June 2021
# code in PyCharm / Python 3.9