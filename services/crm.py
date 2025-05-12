class CRM:
    def __init__(self):
        self.customers = []

    def create_profile(self, name, email):
        profile = {'name': name, 'email': email}
        self.customers.append(profile)
        return profile

    def get_all_profiles(self):
        return self.customers