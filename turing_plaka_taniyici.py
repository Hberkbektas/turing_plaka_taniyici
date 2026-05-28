# Turing Makinesi ile Araç Plaka Formatı Tanıyıcı
# Format: NNLLNNN

import string

# Bant oluştur
girdi = input("Plaka giriniz: ")

# Bandın sonuna boşluk karakteri ekleniyor
tape = list(girdi + " ")

# Başlangıç değerleri
state = "q0"
head = 0

digits = "0123456789"
letters = string.ascii_uppercase

print("\n--- Turing Makinesi Başladı ---\n")

while True:

    symbol = tape[head]

    print(f"Durum: {state}")
    print(f"Okunan sembol: {symbol}")
    print(f"Kafa konumu: {head}")
    print(f"Bant: {''.join(tape)}")
    print("--------------------------")

    # q0 → ilk rakam
    if state == "q0":
        if symbol in digits:
            state = "q1"
            head += 1
        else:
            state = "qRED"

    # q1 → ikinci rakam
    elif state == "q1":
        if symbol in digits:
            state = "q2"
            head += 1
        else:
            state = "qRED"

    # q2 → ilk harf
    elif state == "q2":
        if symbol in letters:
            state = "q3"
            head += 1
        else:
            state = "qRED"

    # q3 → ikinci harf
    elif state == "q3":
        if symbol in letters:
            state = "q4"
            head += 1
        else:
            state = "qRED"

    # q4 → ilk rakam
    elif state == "q4":
        if symbol in digits:
            state = "q5"
            head += 1
        else:
            state = "qRED"

    # q5 → ikinci rakam
    elif state == "q5":
        if symbol in digits:
            state = "q6"
            head += 1
        else:
            state = "qRED"

    # q6 → üçüncü rakam
    elif state == "q6":
        if symbol in digits:
            state = "q7"
            head += 1
        else:
            state = "qRED"

    # q7 → kabul kontrolü
    elif state == "q7":
        if symbol == " ":
            print("\nSONUÇ: KABUL")
            break
        else:
            state = "qRED"

    # RED durumu
    elif state == "qRED":
        print("\nSONUÇ: RED")
        break
    