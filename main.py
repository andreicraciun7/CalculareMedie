lista_nume = []
lista_note_romana = []
lista_note_matematica = []
lista_note_optional = []

while True:
    adauga_nume = input("\n Adăugați un nume în listă.\nPentru a trece la pasul următor, tastați -done-.")
    if adauga_nume == "done":
        break
    lista_nume.append(adauga_nume)

    nota_romana = float(input("Nota la limba română:"))
    while nota_romana<1 or nota_romana > 10:
        print("Nota introdusă este invalidă.")
        nota_romana = float(input("Introduceți o valoare cuprinsă între 1 și 10:"))
    lista_note_romana.append(nota_romana)

    nota_matematica = float(input("Nota la matematică:"))
    while nota_matematica<1 or nota_matematica > 10:
        print("Nota introdusă este invalidă.")
        nota_matematica = float(input("Introduceți o valoare cuprinsă între 1 și 10:"))
    lista_note_matematica.append(nota_matematica)

    nota_optional = float(input("Nota la materia opțională:"))
    while nota_optional<1 or nota_optional > 10:
        print("Nota introdusă este invalidă.")
        nota_optional = float(input("Introduceți o valoare cuprinsă între 1 și 10:"))
    lista_note_optional.append(nota_optional)

while True:
    verifica_media = input("\n Introduceți numele unei persoane pentru a vedea media notelor și situația promovării.\n Pentru a termina procesul, tastați -done-.")
    if verifica_media == "done":
        break
    if verifica_media not in lista_nume:
        print("Persoana nu se află pe listă.")
    else:
        x = int(lista_nume.index(verifica_media))
        media_notelor = (lista_note_matematica[x] + lista_note_romana[x] + lista_note_optional[x]) / 3
        y = round(media_notelor, 2)
        print("Media obținută este: " + str(y))
        if media_notelor < 6:
            print("Picat. Media de promovare este minim 6.")
        else:
            if lista_note_matematica[x] >= 5:
                pass
            else:
                print("Picat. Nota minima de trecere este 5.")
                break
            if lista_note_romana[x] >= 5:
                pass
            else:
                print("Picat. Nota minima de trecere este 5.")
                break
            if lista_note_optional[x] >= 5:
                pass
            else:
                print("Picat. Nota minima de trecere este 5.")
                break
            print("Promovat.")