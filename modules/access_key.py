"""
A wrapper class for encrypted access keys
"""
import settings as S
from cryptography.fernet import Fernet, InvalidToken
from datetime import datetime


class AccessKey:
    """
    AccessKey class
    """

    def __init__(self):
        self._F = None
        try:
            self._F = Fernet(S.FERNET_KEY)
        except TypeError:
            raise Exception(f"{datetime.now()}: The fernet key was invalid {S.FERNET_KEY=}")
            
    def decrypt(self, encrypted_key=None):
        decrypted_key = None
        if self._F and encrypted_key:
            try:
                decrypted_key = self._F.decrypt(encrypted_key).decode('utf-8')
            except InvalidToken:
                raise Exception(f"{datetime.now()}: The token was invalid in {encrypted_key=}")
        return decrypted_key