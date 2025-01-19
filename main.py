import turtle
import json

from tkinter import messagebox

from healthboard import Healthboard


heroes_list = ["Aqua", "Sylvanus", "Ignis", "Aurum", "Terr"]

with open("data.json", encoding="utf-8") as data:
    heroes_abilities = json.load(data)

# Spunem utilizatorului detalii despre joc
print(
    "În Tărâmul Elementelor, o lume fermecată și plină de magie, cele cinci elemente - Apa, Lemnul, Focul, Metalul "
    "și Pământul - coexistă în armonie. Dar echilibrul fragil al acestei lumi este amenințat de o forță întunecată "
    "și misterioasă, cunoscută sub numele de Mistica Umbră.")

print(
    "Pentru a restabili armonia și lumina în Tărâmul Elementelor, eroii noștri - Aqua, Sylvanus, Ignis, Aurum și Terr"
    "a - pornesc într-o aventură îndrăzneață pentru a înfrunta Mistica Umbră și a aduce înapoi lumină și echilibru.")

print("Pe drum te vei întâlni cu inamici și va trebui să te ferești de ei, sau să lupți cu aceștia.")
print("Scopul tău este să ajungi la lumină și înapoi, și să rămâi în viață. Astfel vei restabili echilibrul în "
      "Tărâmul Elementelor.\nMult succes!")

# Punem jucătorul să își aleagă un erou
chosen_hero = input(f"Alege-ți eroul cu care vrei să joci ({heroes_list}): ")

while chosen_hero not in heroes_list:
    chosen_hero = input(f"Acest erou nu exista. Te rog sa alegi altul ({heroes_list}): ")

print(f"Eroul pe care l-ai ales este: {chosen_hero}.")
# Îi comunicăm jucătorului abilitățile pe care le are eroul ales
print(f"Acesta are următoarele abilități: {heroes_abilities[chosen_hero]}.")

print("START JOC!")

healthboard = Healthboard()


# Definim funcția pentru fundături
def dead_end():
    messagebox.showerror("Fundătură", "Ai ajuns într-o fundătură.")

    healthboard.game_over()


# Definim funcția pentru duelurile cu monștrii
def monster_duel():
    messagebox.showinfo("Monstru", "Ai pierdut 50% viață în duelul cu monstrul.")
    healthboard.health -= 50
    healthboard.update_healthboard()


# Definim funcția pentru consumarea abilitățiilor
def consume_ability(ability):
    if ability == "first":
        messagebox.showinfo("Abilitate consumată", "Ți-ai consumat prima abilitate."
                                                   f"\n{heroes_abilities[chosen_hero][0]}")

    elif ability == "second":
        messagebox.showinfo("Abilitate consumată", "Ți-ai consumat a doua abilitate."
                                                   f"\n{heroes_abilities[chosen_hero][1]}")


# Inițializăm ecranul turtle
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("În căutarea Luminii în Labirintul Umbrelor")

screen.bgpic("maze.gif")

turtle.speed(999)

turtle.penup()

turtle.goto(x=85, y=75)
turtle.color("red")
turtle.setheading(180)
turtle.pendown()
turtle.circle(5)

turtle.penup()
turtle.color("green")

turtle.goto(-90, -70)
turtle.setheading(90)

turtle.speed(1)
turtle.setheading(0)

turtle.forward(80)

turtle.setheading(90)
turtle.forward(15)

# Întrebăm utilizatorul ce vrea să facă în continuare, iar pe baza asta se întâmplă ceva anume
response = messagebox.askquestion("Răscruce de drum", "Ai ajuns la o răscruce. Vrei să alegi partea stângă? "
                                                      "Nu uita că acolo se poate afla o capcană, un monstru, sau poate "
                                                      "soluția pe care o cauți.")

if response == "yes":
    turtle.setheading(180)
    turtle.forward(60)

    turtle.setheading(90)

    response = messagebox.askquestion("Monstru", "Un monstru ți-a ieșit în cale, e pregătit să-ți sugă "
                                                 "sângele, sau cel puțin să lupte până la moarte. "
                                                 "Dorești să folosești prima abilitate?\n\nAbilitățile tale: "
                                                 f"{heroes_abilities[chosen_hero]}")

    if response == "yes":
        first_ability_consumed = True

        consume_ability("first")

    else:
        first_ability_consumed = False

        monster_duel()

    turtle.forward(15)

    turtle.setheading(180)
    turtle.forward(15)

    turtle.setheading(90)
    turtle.forward(15)

    turtle.setheading(0)
    turtle.forward(10)

    turtle.setheading(90)
    turtle.forward(65)

    turtle.setheading(0)
    turtle.forward(20)

    response = messagebox.askquestion("Răscruce de drum", "Vrei să mergi tot în față? Acolo ar putea fi "
                                                          "un monstru, o fundătură, sau chiar lumina magică pe care o "
                                                          "cauți.")

    if response == "yes":
        dead_end()

    else:
        if first_ability_consumed:
            response = messagebox.askquestion("Monstru", "Ai dat de un monstru cu 3 mâini și 6 ochi."
                                                         " Vrei să folosești a doua abilitate? ")

        else:
            response = messagebox.askquestion("Monstru", "Tocmai ți-a ieșit în față un monstru fioros cu "
                                                         "solzi întunecați, colți ascuțiți și ochi aprinși în flăcări. "
                                                         "Vrei să folosești prima abilitate? ")

        if response == "yes":
            if first_ability_consumed:
                second_ability_consumed = True

                consume_ability("second")

            else:
                second_ability_consumed = False
                first_ability_consumed = True

                consume_ability("first")

        else:
            monster_duel()

        if not healthboard.game_finished:
            turtle.setheading(-90)
            turtle.forward(45)

            turtle.setheading(0)
            turtle.forward(30)

            dead_end()

else:
    turtle.setheading(0)
    turtle.forward(20)

    turtle.setheading(90)
    turtle.forward(15)

    turtle.setheading(180)
    turtle.forward(20)

    turtle.setheading(90)
    turtle.forward(15)

    turtle.setheading(0)
    turtle.forward(15)

    turtle.setheading(90)
    turtle.forward(15)

    response = messagebox.askquestion("Monstru", "Tocmai ai dat de un monstru cu 6 capete. Vrei să-ți folosești prima "
                                      f"abilitate?\n\n Abilitățile tale: {heroes_abilities[chosen_hero]}")

    if response == "yes":
        first_ability_consumed = True

        consume_ability("first")

    else:
        first_ability_consumed = False

        monster_duel()

    turtle.forward(15)

    turtle.setheading(180)
    turtle.forward(15)

    turtle.setheading(90)
    turtle.forward(20)

    response = messagebox.askquestion("Răscruce", "Vrei să mergi la stânga?")

    if response == "yes":
        dead_end()

    else:
        turtle.setheading(0)
        turtle.forward(30)

    response = messagebox.askquestion("Răscruce", "Vrei să mergi în față?")

    if response == "yes":
        dead_end()

    else:
        turtle.setheading(90)
        turtle.forward(15)

        if first_ability_consumed:
            response = messagebox.askquestion("Monstru", "Ai dat de un monstru periculos care vrea să îți "
                                                         "taie picioarele și mâinile cu scopul de a te opri.\n"
                                                         "Vrei să îți folosești a doua abilitate?")

            if response == "yes":
                second_ability_consumed = True

                consume_ability("second")

            else:
                second_ability_consumed = False

                monster_duel()

        else:
            response = messagebox.askquestion("Monstru", "Ai dat de un monstru periculos care vrea să îți "
                                                         "taie picioarele și mâinile cu scopul de a te opri.\n"
                                                         "Vrei să îți folosești prima abilitate?")

            if response == "yes":
                first_ability_consumed = True

                consume_ability("first")

            else:
                first_ability_consumed = False

                monster_duel()

        turtle.setheading(180)
        turtle.forward(10)

        turtle.setheading(90)
        turtle.forward(30)

        turtle.setheading(0)
        turtle.forward(10)

        turtle.setheading(-90)
        turtle.forward(15)

        turtle.setheading(0)
        turtle.forward(20)

        turtle.setheading(90)
        turtle.forward(15)

        turtle.setheading(0)
        turtle.forward(40)

        messagebox.showinfo("Ai ajuns!", "Ai găsit lumina magică. Aceasta te-a ajutat să dai din nou viață"
                                         " pe Tărâmul Elementelor, astfel scăpând de Mistica Umbră.")

        healthboard.game_over()

screen.exitonclick()
