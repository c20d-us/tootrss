"""
A module for handling Fernet-encrypted tokens
"""
from cryptography.fernet import Fernet


class EncryptedToken:
    """
    A class to manage tokens encrypted with Fernet

    Parameters
    ----------
    fernet_key : str
        The Fernet key that was used to encrypt the token
    encrypted_token : str
        The Fernet-encrypted token that will be decrypted, utf-8 encoded

    Methods
    -------
    decrypt()
        Decrypts the Fernet-encrypted token
    """

    def __init__(self, fernet_key: str, encrypted_token: str) -> None:
        """
        The initializer

        Raises
        ------
        Exception:
            If the Fernet key is not valid, a generic Exception is raised
        """
        self._F = None
        self._token = encrypted_token
        try:
            self._F = Fernet(fernet_key)
        except:
            raise Exception(
                f"The supplied fernet key was invalid: {fernet_key}"
            )

    def decrypt(self) -> str:
        """
        Decrypt the Fernet-encrypted token.
        
        Parameters
        ----------
        None

        Returns
        -------
        str: The unencrypted token

        Raises
        ______
        Exception:
            If the encrypted token is not valid, a generic Exception is raised

        """
        decrypted_token = None
        try:
            decrypted_token = self._F.decrypt(self._token).decode("utf-8")
        except:
            raise Exception(
                f"The encrypted token was invalid: {self._token=}"
            )
        return decrypted_token