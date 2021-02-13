items = [2, 36, 25, 9]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break
else: #no break
    items.append(divisor)
    found = divisor

print(f'{items} contain {found} which is a multiple of {divisor}')