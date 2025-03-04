

def encrypt(text, key=1):
    encryptedList = list()
    for char in text:
        charBuffer = chr((ord(char) + key) % 1114000)
        encryptedList.append(charBuffer)
    encryptedText = "".join(encryptedList)
    return encryptedText

def decrypt(text, key=1):
    return encrypt(text, -key)

def getKey(encryptedText, realText):
    
    for i in range(5000000):
        if (i % 50000) == 0:
            percent = i / 50000
            
            print("\r" + str(percent) +" %", end="", flush=True)
        decryptedList = list()
        try:
            for char in encryptedText:
                charBuffer = chr((ord(char) - i) % 1114000)
                decryptedList.append(charBuffer)
            decryptedText = "".join(decryptedList)
            if decryptedText == realText:
                print("\nThe used Key is:")
                return i
        except:
            print("\n##Overflow##\n i= ", end="")
            print(i)
            break

    return "\n#Not found"

if __name__ == "__main__":
    while(True):
        

        print("Choose an option: \n  [0] encrypt\n  [1] decrypt\n  [2] get key\n  [q] quit\nEnter the character:")

        menuNum = input()

        if menuNum == "q":
            break
        
        elif menuNum == "2":
            print("!!This only works for positve number keys!!")
            print("Enter encrypted text:")
            encryptedText = input()
            print("Enter decrypted text:")
            decryptedText = input()
            key = getKey(encryptedText, decryptedText)
            print(key)
        else:
            print("Enter key:")
            key = int(input())

            if menuNum == "0":
                print("Enter text:")
                userText = input()
                text = encrypt(userText, key)

            else:
                print("Enter text:")
                userText = input()
                text = decrypt(userText, key)

            print("#######################\n" +
                    text +
                "\n#######################")
