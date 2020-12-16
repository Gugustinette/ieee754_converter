# Init
# IEEE754 Converter - Encode / EN
# Author : Augustin MERCIER "Gugustinette"

#   Mode Set
#   1 = Decimal Input
#   2 = Binary Input
mode = 1

#   Denormalized mode
#   True : On
#   False : Off

denorm = True

#   Number of bytes settings
#   bytes_total : total number of bytes
#   bytes_expo : number of bytes dedicated to exponent

bytes_total = 32
bytes_expo = 8

# CODE / DO NOT TOUCH
bytes_mantisse = bytes_total - bytes_expo - 1

expo_value = 0

def GetIntAtIndex(nb, i) : # Return digit number i of a given value (input : decimal / output : decimal)
    x = nb % 10**i
    x -= nb % 10**(i - 1)
    x = x / 10**(i - 1)
    return x

def LenInt(nb) : # Return the len of a given number as int (input : decimal / output : decimal)
    x = 0
    while nb > 0 :
        nb = nb // 10
        x += 1
    return x

def ToBinaryDecimal(nb_input) : # Return the binary form of a given value (input : decimal / output : string)
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

def ToDecimalBinary(bin_input) : # Return the value of a given binary (input : string / output : decimal)
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

def SignOf(bin_input) : # Return the sign bit of a binary number (input : string / output : decimal)
    if bin_input[0] == "-" :
        return bin_input.replace("-", ""), 1
    else :
        return bin_input, 0

def DeleteZeroOf(bin_input) : # Delete useless zeros at the beginning of a binary (input : string / output : string)
    index = 0
    new_bin_x = ""
    while bin_input[index] == "0" :
        index += 1
    for n in range(index, len(bin_input)) :
        new_bin_x = new_bin_x + bin_input[n]
    return new_bin_x

def ExponantOf(bin_input) : # Return the IEEE754 exponent of a given binary (input : string / output : string)
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

def Denorm_Exponant() : # Return denormalized exponant
    global bytes_expo, expo_value
    expo = ""
    for i in range(bytes_expo) :
        expo += "0"
    expo_value = 1 - (2**(bytes_expo - 1) - 1)
    return expo

def MantisseOf(bin_input) : # Return the IEEE754 mantisse of a given binary (input : string / output : string)
    global bytes_mantisse, x, expo_value
    temp_x = abs(x)
    mantisse = ""
    if bin_input[0] == "." or denorm :
        if denorm :
            i = 0
            power = abs(expo_value) + 1
            if temp_x == 2**expo_value :
                i = temp_x
            while i != temp_x :
                if i + (2**-power) > temp_x :
                    mantisse = mantisse + "0"
                else :
                    mantisse = mantisse + "1"
                    i += (2**-power)
                power += 1
        else :
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

def ValueFromInput(str_input) : # Return given value of form "6.35E-39"
    for i in range(len(str_input)) :
        if str_input[i] == "E" or str_input[i] == "e" :
            power_pos = i
            i = len(str_input)
    power_value = int(str_input[power_pos + 2:])
    final_value = float(str_input[0:power_pos]) * (10 ** -power_value)
    return final_value

if mode == 1 : # Decimal Input
    if denorm :
        str_input_x = str(input("Enter decimal value (denormalized, ex : 6.35e-39) : "))
        x = ValueFromInput(str_input_x)
    else :
        x = float(input("Enter decimal value (int or float) : "))

    print("Decimal value : " + str(x))

    if x > 0 :
        sign_x = 0
    else :
        sign_x = 1

    x = abs(x)

    bin_x = ToBinaryDecimal(x)

    bin_x = DeleteZeroOf(bin_x)

    bin_x = bin_x.replace("-", "")
else :
    if mode == 2 : # Binary Input
        bin_x = str(input("Enter binary as expected format : 10.01 / -10.01 / 0.01 / .01 / -0.01 / -.01 /... : "))

        print(bin_x)

        bin_x = DeleteZeroOf(bin_x)

        x = ToDecimalBinary(bin_x)

        print("Decimal value : " + str(x))

        bin_x, sign_x = SignOf(bin_x)

if sign_x == 1 :
    print("Binary value : -" + bin_x)
else :
    print("Binary value : " + bin_x)

print("Absolute binary value : " + bin_x)

if denorm :
    expo_x = Denorm_Exponant()
else :
    expo_x = ExponantOf(bin_x)

mant_x = MantisseOf(bin_x)

print("Sign bit : " + str(sign_x))

print("Exponent value : " + str(expo_value))

print("Exponent bits : " + expo_x)

if denorm :
    print("Mantisse value : " + "0." + mant_x)
else :
    print("Mantisse value : " + "1." + mant_x)

print("Mantisse bits : " + mant_x)

print("")

print("IEEE754 Binary of Number : ")

print(str(sign_x) + "  /  " + expo_x + "  /  " + mant_x)

print("")

print(str(sign_x) + expo_x + mant_x)
