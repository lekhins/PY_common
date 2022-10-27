counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)