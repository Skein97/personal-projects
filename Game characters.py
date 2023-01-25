class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attacking with 1 out of {self.arrows}')
        self.arrows = self.arrows - 1

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('Ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self,name, power)
        Archer.__init__(self, name, arrows)

# archer1 = Archer('Robin', 100)
# archer1.attack()
# archer1.check_arrows()

