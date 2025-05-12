import hashlib

class AuthService:
    def __init__(self):
        self.users = {'admin': self._hash('admin123')}

    def _hash(self, pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()

    def authenticate(self, username, password):
        return self.users.get(username) == self._hash(password)