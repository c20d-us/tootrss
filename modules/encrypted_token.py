"""
A wrapper class for decrypting Fernet-encrypted tokens
"""
from cryptography.fernet import Fernet, InvalidToken


class EncryptedToken:
    """
    EncryptedToken class
    """

    def __init__(self, fernet_key, encrypted_token):
        self._F = None
        self._token = encrypted_token
        try:
            self._F = Fernet(fernet_key)
        except TypeError:
            raise Exception(
                f"The fernet key was invalid: {fernet_key}"
            )

    def decrypt(self):
        decrypted_token = None
        if self._F and self._token:
            try:
                decrypted_token = self._F.decrypt(self._token).decode("utf-8")
            except InvalidToken:
                raise Exception(
                    f"The encrypted token was invalid: {self._token=}"
                )
        return decrypted_token
