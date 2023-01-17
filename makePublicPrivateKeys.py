import random, sys, os, primeNum, cryptmath

def main():
    print('Making key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('Key files made.')

def generateKey(keySize):
    p = 0
    q = 0
    print('Generating p prime...')
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p * q

    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptmath.gcd(e, (p - 1)) == 1:
            break
    print('Calculating d that is mod inverse of e...')
    d = cryptmath.findModInverse(e, (p-1)*(q-1))
    publickey = (n, e)
    privatekey = (n, d)
    print('Public key:', publickey)
    print('Private key:', privatekey)
    return (publickey, privatekey)

def makeKeyFiles(name, keySize):
    if os.path.exists(f'{name}_pubkey.txt') or os.path.exists(f'{name}_privkey.txt'):
        sys.exit(f'Warning: The file {name}_pubkey.txt or {name}_privkey.txt already exists! User a different name or delete these files are return this program.')
    publicKey, privateKey = generateKey(keySize)
    fo = open(f'{name}_pubkey.txt', 'w')
    fo.write(f'{keySize},{publicKey[0]},{publicKey[1]}')
    fo.close()

    fo = open(f'{name}_privkey.txt', 'w')
    fo.write(f'{keySize},{privateKey[0]},{privateKey[1]}')
    fo.close()

if __name__=='__main__':
    main()
