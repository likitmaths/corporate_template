a = 1
b = 2

print('method 1 : a = ' + str(a) + ', b = ' + str(b) ) # concatenate
print('method 2 : a = %d, b = %d'%(a,b)) # %
print('method 3 : a = {}, b = {}'.format(a,b))  # format
print(f'method 4 : a = {a}, b = {b}')   # f string

print(f'sum of {a} and {b} = {a+b}')

print(f' {a} multiply {b} = {a*b}')

print(f' {a} divide {b} = {a/b}')

print(f' {a} mod {b} = {a%b}')
