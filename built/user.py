class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email
        self.validate_email()

    def validate_email(self):
        if "@" not in self._email or "." not in self._email:
            raise ValueError(f"Invalid email address: {self._email}")

    def __str__(self):
        return f"User: {self._username} ({self._email})"

    def __len__(self):
        return len(self._username)

    def role(self):
        return "User"

    def send_message(self, message):
        return f"{self._username} sends: {message}"
