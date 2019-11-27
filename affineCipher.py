def encode(coprimeKey, shiftKey, alphabet, message):

    if gcd(coprimeKey, len(alphabet)) != 1:
        raise Exception("CoprimeKey must be coprime to the length of the alphabet")
    
    encodedMessage = ''

    for char in message:
        oldValue = alphabet.index(char)
        newValue = ((coprimeKey * oldValue) + shiftKey) % len(alphabet)
        encodedMessage += alphabet[newValue]

    return encodedMessage

def decode(coprimeKey, shiftKey, alphabet, message):
    
    decodedMessage = ''
    decodeKey = modularMultiplicativeInverse(coprimeKey, len(alphabet))

    for char in message:
        oldValue = alphabet.index(char)
        newValue = (decodeKey * (oldValue - shiftKey)) % len(alphabet)
        decodedMessage += alphabet[newValue]

    return decodedMessage

def bruteForceCrack(shiftKeyCeiling, alphabet, message):
    
    coprimeKeys = generateCoprimeKeys(alphabet)
    shiftKey = 0

    for key in coprimeKeys:
        while shiftKey < shiftKeyCeiling:
            print 'Decode Attempt ' + str(key) + ',' + str(shiftKey) + ': ' + str(decode(key, shiftKey, alphabet, message))
            shiftKey += 1
        shiftKey = 0

def modularMultiplicativeInverse(a, m):

    a = a % m

    for i in range(1, m):
        if ((a * i) % m) == 1:
            return i

    return 1

def gcd(a, b):

    i = 2
    gcd = 1

    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1

    return gcd

def generateCoprimeKeys(alphabet):

    i = 2
    coprimeKeys = [1]

    while i <= len(alphabet):
        if gcd(i, len(alphabet)) == 1:
            coprimeKeys.append(i)
        i += 1

    return coprimeKeys

"""a = pn + r
b = qn + r

a-b = kn

k = p-q

assume a = b (mod n)

a x p + b = r (mod 26)
a x q + b = s (mod 26)

b = s - qa (mod 26)
ap + s - qa = r (mod 26)
a = ((r - s) / (p-q)) (mod 26)

a = (r - b) / p (mod 26)
b = s - ((qr - qb) / p) (mod 26)
pb = ps - (qr - qb) (mod 26)
pb = ps - qr + qb (mod 26)
b(p-q) = ps - qr (mod 26)
b = ((ps - qr) / p-q) (mod 26)"""


