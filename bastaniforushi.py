# bastani forushi
class BastaniForushi:
    total_weight = 0
    fridge = {
        'bastani chocolate' : 0,
        'bastani fruity' : 0,
        'bastani musical' : 0,
        'bastani yakhi' : 0
        }
    bank = 0

    def __init__(self):
        pass

    def buy(self, name, amount):
        self.name = name
        self.amount = amount
        
        if self.total_weight <= 200000:
            if self.name == 'c':
                b1 = BastaniChocolate()
                self.total_weight += b1.weight * self.amount
                self.fridge[f'{b1.__repr__()}'] += self.amount
            elif self.name == 'f':
                b1 = BastaniFruity()
                self.total_weight += b1.weight * self.amount
                self.fridge[f'{b1.__repr__()}'] += self.amount
            elif self.name == 'm':
                b1 = BastaniMusical()
                self.total_weight += b1.weight * self.amount
                self.fridge[f'{b1.__repr__()}'] += self.amount
            else:
                b1 = BastaniYakhi()
                self.total_weight += b1.weight * self.amount
                self.fridge[f'{b1.__repr__()}'] += self.amount
        else:
            print('anbar gonjayesh nadarad!')

    def sell(self, name, amount):
        self.name = name
        self.amount = amount

        if self.name == 'c':
            b1 = BastaniChocolate()
            if self.amount <= self.fridge['bastani chocolate']:
                self.fridge['bastani chocolate'] -= self.amount
                self.bank += b1.price * self.amount * 20 / 100
                print('bastani forukhte shod!')
                    
        elif self.name == 'f':
            b1 = BastaniFruity()
            if self.amount <= self.fridge['bastani fruity']:
                self.fridge['bastani fruity'] -= self.amount
                self.bank += b1.price * self.amount * 20 / 100
                print('bastani forukhte shod!')
        elif self.name == 'm':
            b1 = BastaniMusical()
            i = input('aya music pakhsh shavad? y/n: ')
            if i == 'y':
                print('Music')
            if self.amount <= self.fridge['bastani musical']:
                self.fridge['bastani musical'] -= self.amount *2
                self.bank += b1.price * self.amount * 20 / 100
                print('bastani forukhte shod!')
        else:
            b1 = BastaniYakhi()
            if self.amount <= self.fridge['bastani yakhi']:
                self.fridge['bastani yakhi'] -= self.amount
                self.bank += b1.price * self.amount * 20 / 100
                print('bastani forukhte shod!')
            



class Bastani:

    def __init__(self):
        self.weight = 0
        self.price = 0

    def __repr__(self):
        return 'bastani'


class BastaniChocolate(Bastani):

    def __init__(self):
        self.weight = 100
        self.price = 10

    def __repr__(self):
        return 'bastani chocolate'


class BastaniFruity(Bastani):

    def __init__(self):
        self.weight = 55
        self.price = 7

    def __repr__(self):
        return 'bastani fruity'


class BastaniMusical(Bastani):

    def __init__(self):
        self.weight = 200
        self.price = 15

    def __repr__(self):
        return 'bastani musical'


class BastaniYakhi(Bastani):

    def __init__(self):
        self.weight = 40
        self.price = 3

    def __repr__(self):
        return 'bastani yakhi'





