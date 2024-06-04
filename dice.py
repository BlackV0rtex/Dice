import random
# задаём переменные со строчками для кубика
dot_em="|         |"
dot_1l="| X       |"
dot_1r="|       X |"
dot_1c="|    X    |"
dot_2 ="| X     X |"

# задаём while для повторения действия
while True:
    chislo = random.randint(1, 6)
    print("-----------")
    ## Печатаем кубик по строкам
    if (chislo == 1):
        print(dot_em)
        print(dot_1c)
        print(dot_em)
    elif (chislo == 2):
        print(dot_1r)
        print(dot_em)
        print(dot_1l)
    elif (chislo == 3):
        print(dot_1r)
        print(dot_1c)
        print(dot_1l)
    elif (chislo == 4):
        print(dot_2)
        print(dot_em)
        print(dot_2)
    elif (chislo == 5):
        print(dot_2)
        print(dot_1c)
        print(dot_2)
    elif (chislo == 6):
        print(dot_2)
        print(dot_2)
        print(dot_2)
    print("-----------")
# Спрашиваем человека повторить ли программу
    repeat = input("начать занаво? ( N - для выхода, любая клавиша - для повторения:  ")
    #если нет то делаем брейк (иначе на любую клавишу можно начать занаво лол (это встроенно))
    if (repeat == "N" or repeat == "n"):
        break