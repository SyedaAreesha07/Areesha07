from .user import User

class Mentor(User):
    def __init__(self, username, email, expertise):
        super().__init__(username, email)
        self._expertise = expertise

    def __str__(self):
        return f"Mentor: {self._username}, Expert in {self._expertise} ({self._email})"

    def role(self):
        return "Mentor"

    def answer_question(self, question):
        return f"{self._username} answers: {question}"
