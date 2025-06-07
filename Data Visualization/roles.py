class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def perform_action(self):
        return f"{self.name} performs a general action."


class Intern(User):
    def perform_action(self):
        return f"{self.name} is completing intern tasks."


class Mentor(User):
    def perform_action(self):
        return f"{self.name} is mentoring interns."


class Admin:
    def __init__(self, user: User):
        self.user = user

    def perform_admin_action(self):
        return f"{self.user.name} (Admin) is managing the platform."


class HR:
    def __init__(self, user: User):
        self.user = user

    def perform_hr_action(self):
        return f"{self.user.name} (HR) is reviewing applications."
