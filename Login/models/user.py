class User(object):
    def __init__(self, username='', password=''):
        self.user = username
        self.passw = password
        self.labels = {
            'username': 'Username : ',
            'password': 'Password : '
        }

    def setUsername(self, username):
        self.user = username
    
    def setPassword(self, password):
        self.passw = password
    
    def authenticate(self):
        if self.user == 'hanifan' and self.passw == 'flask':
            return True
        else:
            return False