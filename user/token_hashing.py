import hashlib


def hashing_password(password):
    """
    Hashes a given password using the SHA-256 algorithm.

    Args:
        password (str): The plain text password to be hashed.

    Returns:
        str: The hashed password as a hexadecimal string.

    Example:
        >>> hashing_password('mysecretpassword')
        '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd4312167c4ba3c1195'
    """
    p = hashlib.sha256()
    p.update(password.encode("utf-8"))
    hashed_pass = p.hexdigest()
    return hashed_pass
