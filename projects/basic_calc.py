# GNB - 1st - 🔨 Basic Calculator

numero_1 = float(input("Give me one number:"))
numero_2 = float(input("Give me another number:"))

add = round(numero_1 + numero_2, 2)
sub = round(numero_1 - numero_2, 2)
multi = round(numero_1 * numero_2, 2)
div = round(numero_1 / numero_2, 2)
floor_div= round(numero_1 // numero_2, 2)
mod = round(numero_1 % numero_2, 2)
expo = round(numero_1 ** numero_2, 2)

print(f"{numero_1} + {numero_2} = {add}")
print(f"{numero_1} - {numero_2} = {sub}")
print(f"{numero_1} x {numero_2} = {multi}")
print(f"{numero_1} / {numero_2} = {div}")
print(f"{numero_1} // {numero_2} = {floor_div}")
print(f"{numero_1} % {numero_2} = {mod}")
print(f"{numero_1} ** {numero_2} = {expo}")