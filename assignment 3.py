import random
import string


def generate_random_string(length=8, digits_subset="0123456789", letters_subset=string.ascii_letters):
    allowed_chars = digits_subset + letters_subset

    result = ''.join(random.choice(allowed_chars) for _ in range(length))
    return result


if __name__ == "__main__":
    # Subset: only digits 1,2,3 and letters A,B,C
    digits = "123"
    letters = "ABC"

    random_string = generate_random_string(10, digits_subset=digits, letters_subset=letters)
    print("Random String:", random_string)
