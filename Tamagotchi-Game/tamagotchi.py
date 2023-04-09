import os
import threading
import inquirer
import time
import sched

class Tamagotchi:
    age = 0
    bored = 0
    food = 100
    exhausted = 0
    alive = True
    
    def __init__(self) -> None:
        question = [
            inquirer.Text('name', message = 'What is your pets name? ')
        ]
        answer = inquirer.prompt(question)
        self.name = answer.get('name')
        
    def activity_eat(self):
        self.food = self.food + 12
        return ('Eating...', 3.25)
    
    def activity_drink(self):
        self.food = self.food + 1
        return ('Drinking...', 2.5)
    
    def activity_workout(self):
        self.food = self.food - 6
        self.bored = self.bored - 10
        self.exhausted = self.exhausted + 20
        return ("Working out...", 6)
    
    def activity_play(self):
        self.food = self.food - 10
        self.bored = self.bored - 20
        self.exhausted = self.exhausted + 10
        return ("Playing...", 4)
    
    def activity_sleep(self):
        self.exhausted = 0
        self.food = 20
        return('Sleeping...', 10)
    
    def pass_time(self):
        self.age = self.age + 0.3
        self.food = self.food - 5
        self.exhausted = self.exhausted + 0.5
        self.bored = self.bored + 3
        
        if self.food < -20 or self.exhausted >= 100:
            self.alive = False
            
    def status(self):
        print(
            f"""
Name : {self.name}
Age : {self.age}
Food : {self.food}
Bored : {self.bored}
Exhausted : {self.exhausted}
-----------            
            """
        )
    def clear(self):
        if os.name == "nt":
            a = os.system("cls")
        else:
            a = os.system("clear")
            
    def run(self):
        self.clear()
        self.status()
        question = [
            inquirer.List(
                'activity',
                message = 'Choose an option',
                choices = ['Eat', 'Drink', 'Play', 'Sleep', 'Workout'],
            ),
        ]
        answer = inquirer.prompt(question)
        activity_name = 'activity_{}'.format(answer.get('activity')).lower()
        activity = getattr(self, activity_name, lambda: 'Invalid Activity')
        (status, sleep) = activity()
        print(status)
        time.sleep(sleep)
        
    
            
            
def main():
    tamagotchi = Tamagotchi()
    
    s = sched.scheduler(time.time, time.sleep)
    
    def run(sc):
        tamagotchi.pass_time()
        if tamagotchi.alive:
            s.enter(10, 1, run, (sc,))
            
    s.enter(10, 1, run, (s,))
    t = threading.Thread(target=s.run)
    t.start()
    
    while tamagotchi.alive:
        tamagotchi.run()
        
    print(f'{tamagotchi.name} Had Died :(')
    
if __name__ == '__main__':
    main()