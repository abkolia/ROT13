def rot13(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answ = ''

    for i in word:
        if i in alphabet:
            idx = alphabet.index(i)
            if idx >= 26:
                if idx < 39:
                    a_idx = idx + 13
                    answ += alphabet[a_idx]
                else:
                    a_idx = idx - 13
                    answ += alphabet[a_idx]
            else:
                if idx < 13:
                    a_idx = idx + 13
                    answ += alphabet[a_idx]
                else:
                    a_idx = idx - 13
                    answ += alphabet[a_idx]
        else:
            answ += i
    return answ
print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))