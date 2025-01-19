from turtle import Turtle
from tkinter import messagebox

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Healthboard(Turtle):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.color("black")
        self.penup()
        self.goto(-2, 130)
        self.hideturtle()
        self.update_healthboard()
        self.game_finished = False

    def update_healthboard(self):
        self.clear()
        self.write(f"Health: {self.health}%", align=ALIGNMENT, font=FONT)

        if self.health <= 0:
            self.game_over()

            messagebox.showerror("GAME OVER", "Jocul s-a terminat deoarece ai rămas fără viață.")

    def game_over(self):
        self.game_finished = True
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
