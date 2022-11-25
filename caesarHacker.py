import string

def caesarHacker(cipher):
    SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + string.digits + ' !?.'
    for KEY in range(len(SYMBOLS)):
        translated = ''
        for c in cipher:
            if not c in SYMBOLS:
                translated += c
            else:
                symbolIndex = str.find(SYMBOLS, c)
                translatedIndex = symbolIndex + KEY
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)
                translated += SYMBOLS[translatedIndex]
        print(translated, KEY)

if __name__ == '__main__':
    cipher = 'GUVfxVfxZlxfRPeRgxZRffNTR0'
    caesarHacker(cipher)
