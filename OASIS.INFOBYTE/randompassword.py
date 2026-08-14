import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase


    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Random Password Generator ===\n")

    while True:
        try:
            length = int(input("Enter password length (recommended 8-16): "))
            if length < 4:
                print("Password too short! Minimum length is 4.\n")
                continue
            break
        except ValueError:
            print("Please enter a valid number.\n")


    use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols (!@#$ etc.)? (yes/no): ").lower() == 'yes'


    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nYour generated password is:\n{password}")

    again = input("\nGenerate another password? (yes/no): ").lower()
    if again == 'yes':
        main()


if __name__ == "__main__":
    main()