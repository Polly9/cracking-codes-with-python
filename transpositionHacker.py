import detectEnglish, transpositionDecrypt

def main():
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    decryptText = hackTransposition(myMessage)
    print(decryptText)

def hackTransposition(message):
    print('Hacking...')
    for key in range(1, len(message)):
        print(f'Trying key #{key}...')
        decryptText = transpositionDecrypt.decryptMessage(key, message)
        if detectEnglish.isEnglish(decryptText):
            print()
            print('Possible encryption hack:')
            print(f'Key #{key}: {decryptText[:100]}')
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptText
    print('Failed to hack encryption.')
    return None

if __name__ == '__main__':
    main()
