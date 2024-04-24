import random
import string
from time import sleep


def generate_verify_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))


def generate_invite_cod():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


def send_verify_sms(message):
    print(message)
    sleep(2)
