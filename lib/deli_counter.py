
katz_deli = []

def line(deli):
    res = 'The line is currently empty.'
    if deli:
        res = 'The line is currently:'
        for i,name in enumerate(deli):
            res += (f' {i + 1}. {name}')
    print (res)

def take_a_number(deli, name):
    deli.append(name)
    print(f'Welcome, {name}. You are number {len(deli)} in line.')

def now_serving(deli):
    if deli:
        print(f'Currently serving {deli.pop(0)}.')
    else:
        print('There is nobody waiting to be served!')



    

