import detectEnglish, vigenereCipher

def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenereDictionay(ciphertext)

    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackVigenereDictionay(ciphertext):
    fo = open('./CrackingCodesFiles/dictionary.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            print('Possible encryption break:')
            print(f'Key {str(word)}: {decryptedText[:100]}')
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')
            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()
