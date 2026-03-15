class CoffeeMachine:

    def make_coffee(self):
        self.boil_water()
        self.add_coffee()
        self.pour_in_cup()
        print("Coffee is ready")

    def boil_water(self):
        print("Boiling water")

    def add_coffee(self):
        print("Adding coffee powder")

    def pour_in_cup(self):
        print("Pouring into cup")

machine = CoffeeMachine()
machine.make_coffee()