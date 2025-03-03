

print("With this scirpt you can generate a file with your custom quotes\n and encrypt it so they aren't as easy to see for the person who the quotes are for")
print("Choose an option and enter the according number:")
print("[0] enter quote by quote\n[1] import quotes seperated by a defined delimiter e.g. \\n")

menuNum = input()
quoteList = list()
if input == "0":
    print("Enter as many quotes as you want, then enter s to stop entering")
    i = 0
    while(True):
        i += 1
        print("Enter a quote:")
        print(str(i) + ": ", end="")
        bufferQuote = input()
        if bufferQuote == "s":
            break
        quoteList.append(bufferQuote)
elif input == "1":
    print("Enter a list of quotes seperated by a specified delimiter:")
    userList = input()
    print("Enter the delimiter:")
    delimiter = input()
    quoteList = userList.split(delimiter)

print(quoteList)