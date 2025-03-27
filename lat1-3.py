
max = None

while True :
    a = input("input angka = ")
    if a.lower() == "exit" :
        break
    b = float(a)
    if max is None or b > max :
        max = b
if max is not None :
    print(f"angka terbesar yang anda input adalah {max}")
else :
    print("error")


