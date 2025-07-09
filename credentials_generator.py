import random
import string


def generate_credentials():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(length):
        allowed_chars = string.ascii_lowercase + string.digits + "._%+-"
        first_part = ''.join(random.choice(allowed_chars) for _ in range(length))
        email = f"{first_part}@test.com"
        return email

    user_credentials = []

    first_name = generate_random_string(10)
    last_name = generate_random_string(10)
    username = generate_random_string(10)
    email = generate_random_email(10)
    password = generate_random_string(10)

    user_credentials = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password
    }

    return user_credentials