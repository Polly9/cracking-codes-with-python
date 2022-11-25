def main():
    message = 'Common sense is not so common.'
    key = 8
    ciphertext = encryptMessage(key, message)
    print(ciphertext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key

    # 8文字飛ばしで文字をjoinしていく
    for col in range(key):
        currentIndex = col
        while currentIndex < len(message):
            ciphertext[col] += message[currentIndex]
            currentIndex += key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
