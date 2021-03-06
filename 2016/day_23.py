commands = []
while True:
    try:
        commands.append(input().split())
    except:
        break

values = {'a': 7, 'b': 0, 'c': 0, 'd': 0}


i = 0
while i < len(commands):
    command = commands[i]

    if command[0] == 'cpy':
        from_reg = command[1]
        to_reg = command[2]

        try:
            values[to_reg] = int(from_reg)
        except:
            values[to_reg] = values[from_reg]
        i += 1
        continue

    if command[0] == 'inc':
        from_reg = command[1]
        values[from_reg] += 1
        i += 1
        continue

    if command[0] == 'dec':
        from_reg = command[1]
        values[from_reg] -= 1
        i += 1
        continue

    if command[0] == 'jnz':
        from_reg = command[1]
        to_reg = command[2]

        try:
            x = int(from_reg)
        except:
            x = values[from_reg]

        try:
            y = int(to_reg)
        except:
            y = values[to_reg]

        if x != 0:
            i += y
        else:
            i += 1

        continue

    if command[0] == 'tgl':
        try:
            x = int(command[1])
        except:
            x = values[command[1]]

        if i+x < 0 or i+x >= len(commands):
            i += 1
            continue

        change_command = commands[i+x]
        if len(change_command) == 3:
            if change_command[0] == 'jnz':
                change_command[0] = 'cpy'
            else:
                change_command[0] = 'jnz'
        else:
            if change_command[0] == 'inc':
                change_command[0] = 'dec'
            else:
                change_command[0] = 'inc'

        commands[i+x] = change_command
        i += 1
        continue

print('#1:', values['a'])

# It turns out that the program outputs a! plus some constant.
# To calculate the constant substract 7! from part 1 result.
print('#2:', 2*3*4*5*6*7*8*9*10*11*12+5460)
