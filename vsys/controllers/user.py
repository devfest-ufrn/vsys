from vsys.models.database import MongoDatabase

class UserController(object):
    
    def __init__(self):
        self.db = MongoDatabase().instance()
    
    def register(self, user):
        errors = self.validate(user)
        if not errors:
            user_to_insert = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'password': user.password
            }
            user_inserted = self.db.users.insert(user_to_insert)
            user.id = user_inserted

        return errors

    def validate(self, user):
        errors = {}
        if not user.first_name:
            errors['empty_first_name'] = True
        if not user.last_name:
            errors['empty_last_name']= True
        if not user.email:
            errors['empty_email'] = True
        if not user.password:
            errors['empty_password'] = True

        return errors