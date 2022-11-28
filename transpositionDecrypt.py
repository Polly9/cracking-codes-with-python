import math

def main():
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8
    print(decryptMessage(key, message))

def decryptMessage(key, message):
    N = len(message)
    rows = key
    cols = int(math.ceil(N / rows))
    plainText = [''] * cols
    rems = cols * rows - N  # 余り
    
    col = 0
    row = 0 # 行数
    for symbol in message:
        plainText[col] += symbol
        col += 1
        if (col == cols) or (col == cols - 1 and row >= rows - rems):
            col = 0
            row += 1
    return ''.join(plainText)

if __name__ == '__main__':
    main()
