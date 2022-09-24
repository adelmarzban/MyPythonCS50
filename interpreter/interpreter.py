calc = input("Expression:")
a = calc.split()

x = int(a[0])
y = str(a[1])
z = float(a[2])

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    print("not defined operator")

print(result)
