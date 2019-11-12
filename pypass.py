import random
import requests

alphabet_uppercase = [chr(x) for x in range(65, 90)]
alphabet_lowercase = [chr(x) for x in range(97, 122)]
digits = [str(x) for x in range(10)]
special_symbols = [chr(x) for x in range(33, 47)] + [chr(x) for x in range(
    58, 64)] + [chr(x) for x in range(91, 96)] + [chr(x) for x in range(123, 126)]

password_complexity = {
    'all_upper': alphabet_uppercase,
    'all_lower': alphabet_lowercase,
    'alphabet': alphabet_lowercase+alphabet_uppercase,
    'all_upper_with_digits': alphabet_uppercase + digits,
    'all_lower_with_digits': alphabet_lowercase + digits,
    'digits_and_alphabet_ci': alphabet_lowercase + alphabet_uppercase + digits,
    'mixed': alphabet_lowercase + alphabet_uppercase + digits + special_symbols
}

# Check remote dictionary whether password is a real word


def not_a_word(password):
    if password.isalpha():
        r = requests.get('https://www.infoplease.com/dictionary/' + password)
        return r.status_code == 404
    else:
        return True


def generate_password(length, complexity):
    charset = password_complexity[complexity]
    password = ""
    for _ in range(length):
        password += charset[random.randint(0, len(charset)-1)]
    if not_a_word(password):
        return password

# Test case
print generate_password(12, 'all_upper')
