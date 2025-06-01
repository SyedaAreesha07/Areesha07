from .user import User

class Intern(User):
    def __init__(self, username, email, university):
        super().__init__(username, email)
        self._university = university

    def __str__(self):
        return f"Intern: {self._username} from {self._university} ({self._email})"

    def role(self):
        return "Intern"

    def ask_question(self, question):
        return f"{self._username} asks: {question}"
