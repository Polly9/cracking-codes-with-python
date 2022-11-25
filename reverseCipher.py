def main():
    print('↓insert text↓')
    text = input()
    print(reverse_cipher(text))

def reverse_cipher(text):
    """
    入力した文字列を逆順で返す
    """
    translated = ''
    span = len(text)
    for i in range(span - 1, -1, -1):
        translated += text[i]
    return translated

if __name__ == '__main__':
    main()
