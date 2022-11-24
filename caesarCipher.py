import string

def caesarCipher(message, key, mode):
    SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + string.digits + ' !?.'
    translated = ''
    for symbol in message :
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

if __name__ == '__main__':
    message = 'This is my secret message.'
    key = 13
    mode = 'decrypt'
    caesarCipher(message, key, mode)

