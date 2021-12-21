password = "test321"
yourpassword = input('What\'s your password: ')


def password_check():
    try:
        if yourpassword == password:
            print('Valid Password')
        else:
            print('Invalid Password')
    except ValueError as err:
        raise err


password_check()
