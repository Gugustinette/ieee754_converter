# IEEE754_converter
Simple IEEE754 Converter in Python / One file for encoding, one file for decoding

# EN ReadME

In both files, you need to specify the total number of bytes, and number of bytes dedicated to exponent

These 2 values are in the first lines of each files, called "bytes_total" and "bytes_expo"

Encode file also needs you to specify the mode which will be used.
There are 2 modes :

  1 - Decimal Input, which takes a decimal number on run, int or float, no matter
  
  2 - Binary Input, which takes a binary number on run, either int or float, negative or positive,...
  
 All you need to do is to change the variable called "mode" to 1 or 2, depending on the mode you want to use.
 
 Decode file only has one mode, it just takes one IEEE754 binary on run
 
 ## Denormalized value :
 
 ### For encoding :
 Denormalized encoding only support binary input at the moment, do not try to use the decimal input with this mode
 
 You need to specify either if the variable called "denorm" is True or False, at the beginning of the file
 - True for denormalized
 - False for normalized

 ### For decoding :
 
 You need to specify either if the variable called "denorm" is True or False, at the beginning of the file
 - True for denormalized
 - False for normalized
 
 Thanks.
 
 # FR ReadME
 
 Les deux fichiers nécessitent de spécifier le nombre total de bits ainsi que le nombre de bits dédiés à l'exposant
 
 Ces 2 valeurs se trouvent dans les premières lignes du fichiers, elles sont respectivement appelées "bytes_total" et "bytes_expo"
 
 Le fichier d'encodage nécessite aussi le choix du mode.
 Il y a 2 modes :
 
 1 - Entrée décimale, qui prend un nombre décimal en entrée, entier ou flottant, positif ou négatif, sans distinction
 
 2 - Entrée binaire, qui prend un nombre binaire en entrée, encore une fois, entier ou flottant, positif ou négatif,...
 
 Il faut juste choisir le mode en modifiant la variable "mode" se trouvant elle aussi au début du fichier
 
 Le fichier de décodage n'a qu'un mode, et ne demande que d'entrer le nombre sous la forme IEEE754 lors du lancement du programme
 
 ## Valeur dénormalisée :
 
 ### Pour l'encodage :
 L'encodage dénormalisé n'est supporté qu'avec l'entrée d'une valeur binaire pour le moment, n'essayez pas d'utiliser l'entrée décimale avec ce mode
 
 Il faut spécifier l'état du booléen au début du fichier, "True" ou "False"
 - True pour dénormalisé
 - False pour normalisé
 
 ### Pour le décodage :
 
 Il faut spécifier l'état du booléen au début du fichier, "True" ou "False"
 - True pour dénormalisé
 - False pour normalisé
 
 Merci.
 
 Augustin MERCIER "Gugustinette"
