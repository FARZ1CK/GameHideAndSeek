import random
from time import sleep as s

print("""Прятки""")
hide = 0
game = 0
seeker = 0
while True:
    if game == 0:
        print("""
            1)Кровать
            2)Шкаф
            3)За дверью
            4)За шторами
            Введите номер:
            """)
        hide = int(input())
        if hide == 1:
            game = 1
            print("Вы выбрали: "+str(1))
        if hide == 2:
            print("Вы выбрали: "+str(2))
            game = 1
        if hide == 3:
            print("Вы выбрали: "+str(3))
            game = 1
        if hide == 4:
            print("Вы выбрали: "+str(4))
            game = 1
    if game == 1:
        s(3)
        print("Охотник вышел искать")
        seeker = random.randint(1, 4)
        print("Охотник выбрал:"+str(seeker))
        s(2)
        if seeker == hide:
            game = 2
        else:
            seeker1 = random.randint(1, 4)
            s(2)
            print("Охотник выбрал:" + str(seeker1))
            s(3)
            if seeker1 == hide:
                game = 2
            else:
                print("You win!")
                s(3)
                break


    if game == 2:
        print("Lose")
        s(3)
        break
