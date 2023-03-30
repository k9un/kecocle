import random

class Dice:
    def __init__(self):
        pass
        
    def roll():
        return random.randint(1, 6)
        
class Probability:
    def __init__(self, n):
        self.n = n
        self.a = []
        self.b = [0] * 6
        self.c = [0] * 6
        for i in range(self.n):
            self.a.append(Dice.roll())
            
    def calc_probability(self):
        for i in range(6):
            self.c[i] = self.a.count(i+1)
            self.b[i] = self.a.count(i+1) / self.n
         
    def print_probability(self):
        print("총횟수 : %d"%(self.n))
        for i in range(6):
            print("주사위 %d: %d 비율: %f" % ( i+1, self.c[i], self.b[i]))