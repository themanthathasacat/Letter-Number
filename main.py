def encrypt(m, key):
    encrypted = []
    i = 0
    for s in m:
        s = chr(ord(s) + key[i])
        encrypted.append(s)
        i = i + 1
    return encrypted

def decrypt(m, key):
    decrypted = []
    i = 0
    for s in m:
        s = chr(ord(s) - key[i])
        decrypted.append(s)
        i = i + 1
    return decrypted





if __name__ == '__main__':
    original  = ['c', 'a', 't', 'i', 'n', 't', 'h', 'a', 't']
    keys = [5,    4,   1,   3,   1,  10,   9,   2,   1, 4, 2, 1, 7]
    result = encrypt(oroginal, keys)
    for y in result:
        print(y)
    print("\nDecrypting:\n")
    secret = decrypt(result, keys)
    for y in secret:
        print(y)





