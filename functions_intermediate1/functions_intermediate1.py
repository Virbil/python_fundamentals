import random

def randInt(min='', max=''):
    if min < 0 or max < 0:
        return "Min and max must be greater 0"
    num = random.random()
    if min == '' and max == '':
        num = round(random.random() * 100)
    elif min == '' and max != '':
        num = round(random.random() * max)
    elif min != '' and max == '':
        num = round(random.randrange(min, 100))
    elif min != '' and max != '':
        if min > max:
            return "Min must be smaller than Max"
        else:
            num = round(random.randrange(min, max))
    return num

# print(randInt())
# print(randInt(max=13))
# print(randInt(min=50))
# print(randInt(min=50, max=500))
# print(randInt(-4))
# print(randInt(min=14, max=-4))
print(randInt(min=4, max=2))