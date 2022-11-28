import os, sys, time, transpositionEncrypt, transpositionDecrypt 

def main():
    inputFilename = './CrackingCodesFiles/frankenstein.txt'
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt'
    if not os.path.exists(inputFilename):
        print(f'The file {inputFilename} does not exist. Quitting...')
        sys.exit()
    if os.path.exists(outputFilename):
        print(f'This will overwrite the file {outputFilename}. (C)ontinue or (Q)uite?')
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    print(f'{myMode.title()}ing...')

    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
        totalTime = round(time.time() - startTime, 2)
        print(f'{myMode.title()} time: {totalTime} seconds')
        outputFileObj = open(outputFilename, 'w')
        outputFileObj.write(translated)
        outputFileObj.close()
        
        print(f'Done {myMode} {inputFilename} ({len(content)} characters).')
        print(f'{myMode.title()} file in {outputFilename}.')

if __name__ == '__main__':
    main()
