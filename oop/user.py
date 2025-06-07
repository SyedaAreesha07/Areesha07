class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.role = None

    def assign_role(self, role):
        self.role = role

    def login(self):
        self._log_action("logged in")

    def perform_task(self, task):
        self._log_action(f"performed task: {task}")

    def _log_action(self, action):
        if self.role:
            self.role.log(self.username, action)
        else:
            print(f"{self.username} has no role assigned.")
