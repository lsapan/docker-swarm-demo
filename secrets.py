import os


class SecretNotFoundError(IOError):
    pass


def secret_path(name):
    """
    Returns the path to a secret in the docker container.
    """
    secret_path = f'/run/secrets/{name}'
    if not os.path.isfile(secret_path):
        raise SecretNotFoundError(name)
    return secret_path


def secret(name, strip=True):
    """
    Returns the value of a secret from the docker container.
    """
    with open(secret_path(name), 'r') as f:
        val = f.read()
        if strip:
            val = val.strip()
        return val
