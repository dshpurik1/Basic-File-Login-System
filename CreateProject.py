
def encrypt(secret_info):

    encrypt_storage = []
    secret_info = list(secret_info)
    for character in secret_info:
        temp = ord(character) 
        encrypt_storage.append(temp)
    secret_info = ''
    for num in encrypt_storage:
        secret_info += str(num) + ' '
        
    return secret_info
    
def decrypt(secret_info):
    secret_info = secret_info.split()
    decrypted_line = ''
    for numbers in secret_info:
        decrypted_char = chr(int(numbers))
        decrypted_line += decrypted_char
        
    return decrypted_line

def check_choice():
    print('[1] YES')
    print('[2] NO')
    choice = input('CHOICE> ')

    if choice == '1' or choice == '2':
        return choice
    else:
        print('Incorrect option! Try again.')
        return check_choice()
    
def input_message():
    message = input('SECRET MESSAGE> ')
    print('Cool, your account named', "'" + user + "'", 'will store this message:')
    print('\n"' + message + '"\n')
    print('Does that sound good with you?')
    choice = check_choice()
    if choice == '1':
        return message
    else:
        print('Alright, how about you type a new message?')
        return input_message()

print('Welcome to the your PersonalVault™!')
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
print('Are you a new user?')
choice = check_choice()    

with open('data.txt', 'r') as data:
    info = data.readlines()

users = []; passes = []; secret_data = []
n = 1

while n in range(len(info)):
    for j in range(3):
        if j == 0:
            decrypted = decrypt(info[n].strip())
            users.append(decrypted)
        elif j == 1:
            decrypted = decrypt(info[n + 1].strip())
            passes.append(decrypted)
        else:
            decrypted = decrypt(info[n + 2].strip())
            secret_data.append(decrypted)
    n += 3
    
print('***************************************************************')

if choice == '1':

    condition = True
    print('Alrighty then, lets create you a new account.')
    print('Please enter the username you would like.')
    while condition == True:
        n = 0
        user = input('USERNAME> ')
        for test_case in users:
            n += 1
            if test_case == user:
                print("'" + user + "'", 'is currently taken. Try another username.')
                break
            if n == len(users):
                condition = False

    print('Now enter your password and confirm it.')
    password = ''; confirm = ' '
    while password != confirm:
        password = input('PASSWORD> ')
        confirm = input('CONFIRM> ')
        if password == confirm:
            break
        print('Your passwords do not match. Please retype and confirm your password')

    print('***************************************************************')
    print('Sweet! You now have a safe account that can store a message.')
    print('How about you type that message now to store it for later.')
    message = input_message()
    
    with open('data.txt', 'a') as data:
        data.write('\n')
        data.write(encrypt(user))
        data.write('\n')
        data.write(encrypt(password))
        data.write('\n')
        data.write(encrypt(message))
        
else:
    print('Please enter your username and password.')
    condition = False
    while condition == False:
        user = input('USERNAME> ')
        password = input('PASSWORD> ')
        i = 0
        for test_user in users:
            i += 1
            if test_user == user:
                if passes[i - 1] == password:
                    condition = True
                    break
            if i == len(users) and condition == False:
                print("Invalid usernmae or password. Try again.")
    print('***************************************************************')
    print('Welcome back', user, 'to your PersonalVault™.')
    print('Here is the current message in your account:')
    print('\n"' + secret_data[i - 1] + '"')
    print('\nWould you like to change your secret message?')
    choice = check_choice()
    if choice == '1':
        print('Alright, how about you type a new message?')
        message = input_message()
        i *= 3
        info[i] = encrypt(message) + '\n'
        with open('data.txt', 'w') as data:
            data.writelines(info)

with open('data.txt', 'r') as info:
    data = info.readlines()
updated_list = ''
updated_list = updated_list.join(data)
updated_list = updated_list.strip('\n')
file = open('data.txt', 'w')
with open('data.txt', 'w') as info:
    info.write('\n')
    info.write(updated_list)

print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
print('Thank you', user, 'for using PersonalVault™!')
