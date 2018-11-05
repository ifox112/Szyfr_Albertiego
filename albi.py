from collections import deque


def convert(s):
    new = ""
    for x in s:
        new += x
    return new


def encrypting(text, key):
    row = deque([])
    alf = []
    j = 97
    for i in range(26):
        row.append(chr(j))
        alf.append(chr(j))
        j += 1
    l = -1
    ctext = []
    for x in range(len(text)):
        l += 1
        for i in range(len(alf)):
            if text[l] == alf[i]:
                row.rotate(-1 * key)
                ctext.append(row[i])
    return convert(ctext)


def decrypting(text, key):
    row = deque([])
    alf = []
    j = 97
    for i in range(26):
        row.append(chr(j))
        alf.append(chr(j))
        j += 1
    dtext = []
    l = -1
    for x in range(len(text)):
        l += 1
        for i in range(len(alf)):
            if text[l] == alf[i]:
                row.rotate(key)
                dtext.append(row[i])
    return convert(dtext)


print("Kryptosystem realizujący szyf Albiego\n")
k = int(input("Wprowadz klucz szyfrowania: "))
text = input("Wprowadz tekst do zaszyfrowania: ")

crypted = encrypting(text, k)
print("\nTekst zaszyfrowany: ", crypted)
decrypted = decrypting(crypted , k)
print("Tekst odszyfrowany: ", decrypted)


input()

#KACZOROWSKI BARTOSZ
