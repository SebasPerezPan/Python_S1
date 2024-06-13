for x in "Hola":
    print(x)

a = "Hola"
print(len(a))
count = 0
for i in range (len("banana")):
    print("banana" [i])
    if("banana"[i] == "a"):
        count += 1
        
print(f"La letra a se repite {count} veces.")

txt = "Prueba de boleano con cadena en python."
if "Prueba" in txt:
    print("Si. Se encuentra.")
    
print(txt[10:17])
print(txt[:10])
print(txt[10:])
print(txt[10:-7])
print(txt.split(" "))
print(txt.replace("a" ,"x"))
print(txt.upper())
print(txt.lower())
txt.index



print(txt.index("con"))



palindromo = input("Palabra.")
extension = len(palindromo) 
pal_check = True

for i in range (int(len(palindromo)/2)):
    if palindromo[i] != (palindromo[len(palindromo) - 1 - i]):
        pal_check = False
    print(palindromo[i])
    
    
        
print(f"La palabra {palindromo} es {pal_check}")

