# pet.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # starting at a moderate level
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} ate some food. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} took a nap. Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play. Let them sleep.")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(self.happiness + 2, 10)
            self.energy = max(self.energy - 1, 0)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")