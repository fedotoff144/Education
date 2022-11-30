# Task 2
#Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and ⋁ - or ¬ - not

print('Проверка истинности утверждения:')

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            comparison = (not (x or y or z)) == ((not x) and (not y) and (not z))
            print(f"{x}, {y}, {z} - ¬({x} ⋁ {y} ⋁ {z}) = (¬{x} ⋀ ¬{y} ⋀ ¬{z})) = {comparison}")

