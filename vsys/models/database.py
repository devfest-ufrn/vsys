from pymongo import MongoClient

class MongoDatabase():
    """ 
        "Singleton"
    """
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self._database = MongoClient()

    def instance(self):
        return self._database.vsys