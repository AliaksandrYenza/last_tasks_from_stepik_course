#https://stepik.org/lesson/3380/step/2?unit=963

def input_value():
    #print('1 - real string\n2-current\n3-')
    real = input()
    current = input()
    encrypt = input()
    unencrypt = input()
    return real, current, encrypt, unencrypt

def create_unencrypt_dict(real, current):
    unecnrypt_dict = {}
    if len(real) == len(current):
        for i in range(len(real)):
            unecnrypt_dict[real[i]] = current[i]

    return (unecnrypt_dict)

def translater(dict,encrypt,unencrypt ):
    encrypt_res=unencrypt_res = ''
    for i in range(len(encrypt)):
        encrypt_res += dict[encrypt[i]]
    print(encrypt_res)
    new_distionary = {value: key for key, value in dict.items()}
    for i in range(len(unencrypt)):
        unencrypt_res += new_distionary[unencrypt[i]]
    print(unencrypt_res)

if __name__ == '__main__':
    real, current, encrypt, unencrypt = input_value()
    dict = create_unencrypt_dict(real,current)
    translater(dict, encrypt,unencrypt)
