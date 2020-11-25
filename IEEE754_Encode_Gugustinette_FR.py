# Init
# IEEE754 Converter - Decode / FR
# Author : Augustin MERCIER "Gugustinette"

#   Changement du mode
#   1 = Entrée Décimale
#   2 = Entrée Binaire
mode = 1

#   Réglages du nombre de bits
#   bytes_total : nombre total de bits
#   bytes_expo : nombre de bits dédiés à l'exposant

bytes_total = 16
bytes_expo = 5



# CODE / NE PAS TOUCHER
bytes_mantisse = bytes_total - bytes_expo - 1

expo_value = 0

def GetIntAtIndex(nb, i) : # Renvoie le chiffre à l'index i de la valeur nb (entrée : décimal, décimal / sortie : décimal)
    x = nb % 10**i
    x -= nb % 10**(i - 1)
    x = x / 10**(i - 1)
    return x

def LenInt(nb) : # Renvoie la longueur d'un entier (entrée : décimal / sortie : décimal)
    x = 0
    while nb > 0 :
        nb = nb // 10
        x += 1
    return x

def ToBinaryDecimal(nb_input) : # Renvoie la forme binaire d'un entier ou flottant (entrée : décimal / sortie : string)
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

def ToDecimalBinary(bin_input) : # Renvoie la forme décimale d'un nombre binaire (entrée : string / sortie : décimal)
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

def SignOf(bin_input) : # Renvoie le bit de signe d'un nombre binaire (entrée : string / sortie : int)
    if bin_input[0] == "-" :
        return bin_input.replace("-", ""), 1
    else :
        return bin_input, 0

def DeleteZeroOf(bin_input) : # Supprime les 0 inutiles au début d'un nombre binaire (entrée : string / sortie : string)
    index = 0
    new_bin_x = ""
    while bin_input[index] == "0" :
        index += 1
    for n in range(index, len(bin_input)) :
        new_bin_x = new_bin_x + bin_input[n]
    return new_bin_x

def ExponantOf(bin_input) : # Renvoie l'exposant IEEE754 d'un nombre binaire (entrée : string / sortie : string)
    global bytes_expo, expo_value
    expo = 0
    if bin_input[0] == "." :
        i = 0
        while bin_input[i + 1] != "1" :
            expo -= 1
            i += 1
        expo_value = expo - 1
        expo_str = bin(2**(bytes_expo - 1) + expo - 2).replace("0b", "")
    else :
        while bin_input[expo + 1] != "." and expo + 1 < len(bin_input) - 1 :
            expo += 1
        if expo + 1 < len(bin_input) - 1 :
            expo -= 1
        expo_value = expo + 1
        expo_str = bin(2**(bytes_expo - 1) + expo).replace("0b", "")
    while len(expo_str) < bytes_expo :
        expo_str = "0" + expo_str
    return expo_str

def MantisseOf(bin_input) : # Renvoie la mantisse du nombre binaire donné (entrée : string / sortie : string)
    global bytes_mantisse, x, expo_value
    temp_x = abs(x)
    mantisse = ""
    if bin_input[0] == "." :
        i = (2**expo_value)
        power = 1
        if (i == 2**-power) :
            power = 2
        while i != temp_x :
            if i + (2**-power) > temp_x :
                mantisse = mantisse + "0"
            else :
                mantisse = mantisse + "1"
                i += (2**-power)
            power += 1
    else :
        bin_input = bin_input.replace(".", "")
        for i in range(1, len(bin_input)) :
            mantisse = mantisse + bin_input[i]
    while len(mantisse) < bytes_mantisse :
        mantisse = mantisse + "0"
    return mantisse

if mode == 1 : # Entrée sous forme de décimal
    x = float(input("Entrer valeur décimal (entier ou flottant) : "))

    print("Valeur décimale : " + str(x))

    if x > 0 :
        sign_x = 0
    else :
        sign_x = 1

    x = abs(x)

    bin_x = ToBinaryDecimal(x)

    bin_x = DeleteZeroOf(bin_x)

    bin_x = bin_x.replace("-", "")
else :
    if mode == 2 : # Entrée sous forme binaire
        bin_x = str(input("Entrer une valeur binaire avec le bon format : 10.01 / -10.01 / 0.01 / .01 / -0.01 / -.01 /... : "))

        print(bin_x)

        bin_x = DeleteZeroOf(bin_x)

        x = ToDecimalBinary(bin_x)

        print("Valeur décimale : " + str(x))

        bin_x, sign_x = SignOf(bin_x)

if sign_x == 1 :
    print("Valeur binaire : -" + bin_x)
else :
    print("Valeur binaire : " + bin_x)

print("Valeur binaire absolue : " + bin_x)

expo_x = ExponantOf(bin_x)

mant_x = MantisseOf(bin_x)

print("Bit de signe : " + str(sign_x))

print("Valeur de l'exposant : " + str(expo_value))

print("Bits d'exposant : " + expo_x)

print("Valeur de la mantisse : " + "1." + mant_x)

print("Bits de mantisse : " + mant_x)

print("")

print("Forme Binaire IEEE754 du nombre :")

print(str(sign_x) + "  /  " + expo_x + "  /  " + mant_x)

print("")

print(str(sign_x) + expo_x + mant_x)