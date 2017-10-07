file = open("texto.txt", 'r')
word = file.read()
#word = 's IP. Sin'
NewWord = ''

print("Texto Original: ")
print(word)

for c in word:
    if(ord(c) < 200):
        ascii = str(ord(c))
        c = ''
        if(len(ascii) > 2):
            c += ascii[0]
        c += ascii[-1] + ascii[-2]
    n = int(c) + 33
    #print('ASCII Cifrado: ' + str(n))
    NewWord += chr(n)

print("\nTexto Cifrado: ")
print(NewWord)

word = ''

for c in NewWord:
    n = int(ord(c)) - 33
    c = str(n)
    if (n < 10):
        c = '0' + str(n)
    #print('Original: ' + c)
    if(n < 200):
        ascii = str(c)
        c = ''
        if(len(ascii) == 3):
            c += ascii[0]
        c += ascii[-1] + ascii[-2]
    #print('Ascii Nuevo: ' + c)
    #print('Nuevo: ' + chr(int(c)))
    word += chr(int(c))

print("\nTexto Descifrado: ")
print(word)
