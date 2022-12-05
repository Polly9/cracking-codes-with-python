import affineCipher, detectEnglish, cryptmath

SILENT_MODE = False

def main():
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    hackedMessage = hackerAffine(myMessage)

    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackerAffine(message):
    print('Hacking...')

    for key in range(len(affineCipher.SYMBOLS) ** 2): # SYMBOLS ** 2 -> keyAの総数 × keyBの総数
        keyA, _ = affineCipher.getKeyParts(key)
        if cryptmath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue
        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print(f'Tired key {key}... {decryptedText[:40]}')
        if detectEnglish.isEnglish(decryptedText):
            print('Possible encryption hack:')
            print(f'Key: {key}')
            print('Derypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()
