def times2(x):
    return x*2

seq = [1, 2, 3, 4, 5]

new_seq = list(map(times2, seq))

t = lambda var: var*2

print(t(60))

print( list(filter(lambda num: num%2 == 0, seq)) )

print(new_seq)

planet = "Earth"
diameter = 12742
print('The diameter of {a} is {b} kilometers'.format(a = planet, b = diameter))