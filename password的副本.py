minilength = 4

def main():
    password = get_password(minilength)
    print_asterisks(password)

def get_password(mini):
    password = input("Enter password of at least {} characters: ".format(mini))
    while len(password) < mini:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(mini))
    return password

def print_asterisks(sequence):
    print('*' * len(sequence))


main()