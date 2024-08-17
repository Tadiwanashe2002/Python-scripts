marks = int(input('Enter your mark    '))

if marks > 100:
    print('You enter a valid mark')
elif marks >= 70:
    print('You pass with A')
elif marks >=60:
    print('You passed with B')
elif marks >=50:
    print('You passed with C')
elif marks >=40:
    print(' You have a D')
else:
    print('fail')
