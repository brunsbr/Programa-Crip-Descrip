def encrypt(sentence):

    result = []

    for letter in sentence:
        
        l = ord(letter) - 200
        result.append(l)

    print("Este é seu texto criptografado:")

    for numbers in result:
        print(numbers, end='' )
        print(" ",  end='')

    print()

    decrypt(result)


def decrypt(result):


    end_string = ""

    for numbers in result:

        l = int(numbers)
        l =  l + 200
        l = chr(l)
        end_string = end_string + l

    print("Seu Texto descriptografado é: ")
    print(end_string)


def main():

    s = input("Digite o texto que você quer encriptar: ")
    encrypt(s)

if __name__=='__main__':
    main()
	
