import secrets

DEFAULT_LENGTH = 14
CHAR_POOL = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%^&*()-_=+[]{};:'\",./?`~"
)

def generate_password(length: int = DEFAULT_LENGTH) -> str:

    if length < 6:
        length = DEFAULT_LENGTH
    return ''.join(secrets.choice(CHAR_POOL) for _ in range(length))


for x in range(5):
    print(generate_password(15))


