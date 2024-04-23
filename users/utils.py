import random
import string


def generate_verify_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))


def generate_invite_cod():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
