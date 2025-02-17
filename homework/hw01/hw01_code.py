

def heron(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    print(area)

heron(5, 12, 13)

number = 7
color = 'red'
print ('Your favorite number is', number, 'and your favorite color is', color, '.')

age = input('How old are you?')
print('In 10 years you will be', age+10, 'years old')