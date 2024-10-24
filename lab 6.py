#Artem Rospotniuk (kalledus13)
#Lab 6 Groups 10
def encode(password):
    encoded_password = ""
    for i in range(len(password)):
        encoded_password += str((3 + int(password[i])) % 10)
    return encoded_password
#Vignesh Nanduri decoding
def decode(encoded_pass):
    decoded_pass = ''
    for i in encoded_password:
        decoded_pass += str((int(i) - 3) % 10)
    return decoded_pass = ''

def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    user_option = int(input('\nPlease enter an option: '))
    prompt = True
    while prompt:
        if user_option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            continue_menu = True
        elif user_option == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {password}.")
            continue_menu = True
        elif user_option == 3:
            prompt = False
            continue_menu = False
        while continue_menu:
            if user_option == 1:
                password = input('Please enter your password to encode: ')
                print('Your password has been encoded and stored!')
                continue_menu = True
            elif user_option == 2:
                print(f"The encoded password is {encode(password)}, and the original password is {password}.")
                continue_menu = True
            elif user_option == 3:
                prompt = False
                continue_menu = False

if __name__ == '__main__':
    main()
