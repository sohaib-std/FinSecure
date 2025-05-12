class Compliance:
    def __init__(self):
        self.logs = []

    def log_action(self, action):
        self.logs.append(action)

    def get_logs(self):
        return self.logs