import tkinter as tk
import random

class GokspelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gokspel")

        # een label voor de uitleg
        self.uitleg_label = tk.Label(root, text="Raad het getal tussen 1 en 100!", font=("Arial", 14))
        self.uitleg_label.pack(pady=10)

        # juiste getal wordt hier opgeslagen
        self.gekozen_getal = random.randint(1, 100)

        # een label voor de score en pogingen
        self.score_label = tk.Label(root, text="Aantal pogingen: 0", font=("Arial", 12))
        self.score_label.pack()

        # een tekstvak voor de invoer van de gebruiker
        self.invoer = tk.Entry(root, font=("Arial", 14))
        self.invoer.pack(pady=10)

        # een knop om de gok te doen
        self.gok_button = tk.Button(root, text="Gok!", font=("Arial", 14), command=self.controleren)
        self.gok_button.pack(pady=5)

        # Resultaat 
        self.resultaat_label = tk.Label(root, text="", font=("Arial", 14))
        self.resultaat_label.pack(pady=10)

        # Aantal pogingen
        self.pogingen = 0

    def controleren(self):
        try:
            # het aantal pogingen
            self.pogingen += 1
            self.score_label.config(text=f"Aantal pogingen: {self.pogingen}")

            # de ingevoerde gok
            gok = int(self.invoer.get())

            # Controleer of de gok goed is
            if gok < 1 or gok > 100:
                self.resultaat_label.config(text="Voer een getal tussen 1 en 100 in!")
            elif gok < self.gekozen_getal:
                self.resultaat_label.config(text="Te laag! Probeer een hoger getal.")
            elif gok > self.gekozen_getal:
                self.resultaat_label.config(text="Te hoog! Probeer een lager getal.")
            else:
                self.resultaat_label.config(text=f"Gefeliciteerd! Je hebt het getal {self.gekozen_getal} geraden!")
                self.gok_button.config(state=tk.DISABLED)  # Zet de knop uit na het winnen
        except ValueError:
            self.resultaat_label.config(text="Ongeldige invoer. Voer een getal in!")

root = tk.Tk()
app = GokspelApp(root)

root.mainloop()