import Dice

b = int(input('횟수 입력: '))
a = Dice.Probability(b)
a.calc_probability()
a.print_probability()