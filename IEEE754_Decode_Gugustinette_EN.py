# Init
# IEEE754 Converter - Decode / EN
# Author : Augustin MERCIER "Gugustinette"

#   Number of bytes settings
#   bytes_total : total number of bytes
#   bytes_expo : number of bytes dedicated to exponent

bytes_total = 32
bytes_expo = 8

#   Denormalized mode
#   True : On
#   False : Off

denorm = False


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
    if bin_input[0] == "1" :
        return bin_input, 1
    else :
        return bin_input, 0

def ExponantOf(bin_input) : # Return the value of the given IEEE754 exponent (input : string / output : decimal)
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

def ValueFrom(bin_input) : # Return the absolute value of the IEEE754 number using it's mantisse (input : string / output : decimal)
    global expo_value, denorm
    if denorm :
        y = 0
    else :
        y = 2**expo_value
    for i in range(0, len(bin_input)) :
        if bin_input[i] == "1" :
            y += (2**expo_value) * (2**-(i+1))
    return y

bin_x = str(input("Enter IEEE754 binary : "))

bin_x, sign_x = SignOf(bin_x)

expo_x = bin_x[1:bytes_expo + 1]

mant_x = bin_x[bytes_expo + 1:len(bin_x)]

if denorm :
    print("Binary IEEE754 (denormalized) :")
else :
    print("Binary IEEE754 :")
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
    print("Sign bit : " + str(sign_x) + " so value is negative")
else :
    print("Sign bit : " + str(sign_x) + " so value is positive")

print("Exponent bits : " + expo_x)

print("Exponant value : " + str(expo_value))

print("Mantisse bits : " + mant_x)

print("Mantisse value : 1." + mant_str)

if sign_x == 1 :
    print("Binary value : -" + bin_x)
else :
    print("Binary value : " + bin_x)

print("Absolute binary value : " + bin_x.replace("-", ""))

if sign_x == 0 :
    print("Decimal value : " + str(x))
else :
    print("Decimal value : -" + str(x))