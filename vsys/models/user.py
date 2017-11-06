class User():
    
    def __init__(self, first_name, last_name, email, password, address):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._id = None

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        self._password = value
        