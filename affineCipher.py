import sys, cryptmath, random, string

SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + ''.join([str(i) for i in range(10)]) + ' !?.'

def main():
    myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    key = getRandomKey()
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    return encryptMessage(keyA, keyB)

def getKeyParts(key):
    keyA, keyB = divmod(key, len(SYMBOLS))
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if keyA is 1. Choose a different key.')
    elif keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if keyB is 0. Choose a different key.')
    elif keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit(f'KeyA must be greater than 0 and KeyB must be between 0 and {len(SYMBOLS)}.')
    elif cryptmath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit(f'KeyA {keyA} and the symbol set size {len(SYMBOLS)} are not relatively prime. Choose a different key.')

def encryptMessage(key,  message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfkeyA = cryptmath.findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfkeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptmath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

if __name__ == '__main__':
    print(main())
