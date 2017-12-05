from vsys.models.user import User
from vsys.models.database import MongoDatabase

from bson import ObjectId

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

            if user_inserted:
                user_to_insert['success'] = True
                user_to_insert['_id'] = str(user_to_insert['_id'])
                return user_to_insert

            errors['user_not_iserted'] = True
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

    def get_users(self):
        users = list(self.db.users.find({}))
        for user in users:
            user['_id'] = str(user.get('_id'))
            user['password'] = ""
        return users

    def get_user(self, user_id):
        user_id = ObjectId(user_id)  
        user_db = self.db.users.find_one({"_id": user_id})
        user = User(user_db['first_name'], user_db['last_name'], user_db['email'], user_db['password'])
        user.id = str(user_db.get('_id'))
        return user

    def edit_user(self, user):
        errors = self.validate(user)
        if not errors:
            user_json = {
                            "first_name": user.first_name, 
                            "last_name": user.last_name, 
                            "email": user.email,
                            "password": user.password
                        }
            self.db.users.update({"_id": ObjectId(user.id)}, {'$set': user_json})
            return user_json

        return {'errors': errors}

    def delete_user(self, user):
        self.db.users.remove({"_id": ObjectId(user.id)})
        return {'success': True}
