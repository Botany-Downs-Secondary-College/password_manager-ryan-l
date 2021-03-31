import random
encription_key = ["]","a","9","b","+","c",".","8","d","7","e","f",",","g","6","-","h","i","j","[",":",'"',"k","l","5","@","m","4","'","n","o","p","3","q"," ","r","2","s","{","t","u","v","1","w","/","0","x","y","}","z","="]


def loop_encription(number):
    while number > len(encription_key)-1:
        number = number - len(encription_key)
    while number <0:
        number = number + len(encription_key)
    return number


def encript(string):
    global encription_key
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random.shuffle(alphabet)  
    number = [9,8,7,6,5,4,3,2,1,0]
    random.shuffle(number) 
    specil = [",","'","[","]","{","}",'"',":","=","+","-","@",".","/"," "]
    random.shuffle(specil) 
    encription = ""
    for i in range(len(encription_key)):
        if encription_key[i].isdigit() == True:
            encription= encription +str(number[len(number)-1])
            number = number[:-1]
        elif encription_key[i].isalpha() == True:
            encription = encription + alphabet[len(alphabet)-1]
            alphabet = alphabet[:-1]
        else:
            encription = encription + specil[len(specil)-1]
            specil = specil[:-1]
    encrip_string = encription
    for i in range(len(string)):
        if string[i] not in encription:
            encrip_string = encrip_string + string[i]
        for x in range(len(encription)):
            if string[i] == encription_key[x]:
                encrip_string = encrip_string + encription[loop_encription(x+i)]
    return encrip_string


def unencript(encrip_string):
    global encription_key
    encription = encrip_string[0:len(encription_key)]
    string = encrip_string[len(encription_key):len(encrip_string)]
    unencrip_string = ""
    for i in range(len(string)):
        if string[i] not in encription:
            unencrip_string = unencrip_string + string[i]
        for x in range(len(encription_key)):
            if string[i] == encription[x]:
                unencrip_string = unencrip_string + encription_key[loop_encription(x-i)]
    return unencrip_string

print(encript("why"))