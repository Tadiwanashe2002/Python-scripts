
attempts =3
while attempts>0:

    savedPassword = 'svovera'
    password = input('Enter your pass')
    if password == savedPassword:
        print('connected')
        break
    else:
        print('wrong password , Try again')
        attempts  = attempts-1
        print(f'You have {attempts} left')
