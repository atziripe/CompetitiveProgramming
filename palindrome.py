igual, aux = 0, 0
texto = input("Enter palindrome: ")
for index in reversed(range(0, len(texto))):
  if texto[index].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("Palindrome")
else:
  print("Not palindrome")
