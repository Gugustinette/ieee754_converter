# Init
# IEEE754 Converter - Decode / FR
# Author : Augustin MERCIER "Gugustinette"

#   Réglages du nombre de bits
#   bytes_total : nombre total de bits
#   bytes_expo : nombre de bits dédiés à l'exposant

bytes_total = 32
bytes_expo = 8

#   Mode dénormalisée
#   True : Activé
#   False : Désactivé

denorm = False


# CODE / NE PAS TOUCHER
bytes_mantisse = bytes_total - bytes_expo - 1

expo_value = 0

def GetIntAtIndex(nb, i) : # Renvoie le chiffre à l'index i de la valeur nb (entrée : décimal, décimal / sortie : décimal)
    x = nb % 10**i
    x -= nb % 10**(i - 1)
    x = x / 10**(i - 1)
    return x

def LenInt(nb) : # Renvoie la longueur d'un entier (entrée : decimal / sortie : décimal)
    x = 0
    while nb > 0 :
        nb = nb // 10
        x += 1
    return x

def ToBinaryDecimal(nb_input) : # Renvoie la forme binaire d'un entier ou flottant (entrée : decimal / sortie : string)
    global x
    binary_nb = ""
    nb = nb_input
    binary_nb = bin(int(nb)).replace("0b", "")
    new_nb = nb - int(nb)
    if new_nb != 0 : # Means the number is a float
        nb = new_nb
        binary_nb = binary_nb + "."
        while nb != 0 :
            nb *= 2
            if nb >= 1 :
                binary_nb = binary_nb + "1"
                nb -= 1
            else :
                binary_nb = binary_nb + "0"
    return binary_nb

def ToDecimalBinary(bin_input) : # Renvoie la forme décimale d'un nombre binaire (entrée : string / sortie : decimal)
    y = 0
    if bin_input[0] == "-" :
        sign = -1
    else :
        sign = 1
    bin_input = bin_input.replace("-", "")
    if "." in bin_input :
        point_index = 0
        while bin_input[point_index] != "." :
            point_index += 1
    else :
        point_index = len(bin_input)
    for i in range(0, point_index) :
        if bin_input[i] == "1" :
            y += 2**(point_index - 1 - i)
    for i in range(point_index + 1, len(bin_input)) :
        if bin_input[i] == "1" :
            y += 2**-(i - point_index)
    y = y * sign
    return y

def SignOf(bin_input) : # Renvoie le bit de signe d'un nombre binaire (entrée : string / sortie : decimal)
    if bin_input[0] == "1" :
        return bin_input, 1
    else :
        return bin_input, 0

def ExponantOf(bin_input) : # Renvoie la valeur de l'exposant IEEE754 donné (entrée : string / sortie : decimal)
    global bytes_expo, denorm
    if denorm :
        y = 1 - (2**(bytes_expo-1) - 1)
    else :
        power = 0
        y = 0
        if bin_input[0] == "1" :
            y = ToDecimalBinary(bin_input[1:len(bin_input)])
            y += 1
        else :
            for i in range(len(bin_input) - 1, 0, -1) :
                if bin_input[i] == "1" :
                    y += 2**power
                power += 1
            y -= 2**(bytes_expo-1) - 1
    return y

def ValueFrom(bin_input) : # Renvoie la valeur décimale absolue, en prenant la mantisse en paramètre (entrée : string / sortie : decimal)
    global expo_value, denorm
    if denorm :
        y = 0
    else :
        y = 2**expo_value
    for i in range(0, len(bin_input)) :
        if bin_input[i] == "1" :
            y += (2**expo_value) * (2**-(i+1))
    return y

bin_x = str(input("Entrer nombre binaire encodé en IEEE754 : "))

bin_x, sign_x = SignOf(bin_x)

expo_x = bin_x[1:bytes_expo + 1]

mant_x = bin_x[bytes_expo + 1:len(bin_x)]

if denorm :
    print("Forme Binaire IEEE754 du nombre (dénormalisé) : ")
else :
    print("Forme Binaire IEEE754 du nombre : ")
print("")

print(str(sign_x) + expo_x + mant_x)

print("")

print(str(sign_x) + "  /  " + expo_x + "  /  " + mant_x)

print("")

expo_value = ExponantOf(expo_x)

if denorm :
    mant_str = "0." + mant_x
else :
    mant_str = "1." + mant_x

x = ValueFrom(mant_x)

bin_x = ToBinaryDecimal(x)

if sign_x == 1 :
    print("Bit de signe : " + str(sign_x) + " donc valeur négative")
else :
    print("Bit de signe : " + str(sign_x) + " donc valeur positive")

print("Bits d'exposant : " + expo_x)

print("Valeur de l'exposant : " + str(expo_value))

print("Bits de mantisse : " + mant_x)

print("Valeur de la mantisse : " + mant_str)

if sign_x == 1 :
    print("Valeur binaire : -" + bin_x)
else :
    print("Valeur binaire : " + bin_x)

print("Valeur binaire absolue : " + bin_x.replace("-", ""))

if sign_x == 0 :
    print("Valeur décimale : " + str(x))
else :
    print("Valeur décimale : -" + str(x))