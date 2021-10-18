class Employee:
    def __init__(self,id,name,phone):
        self.__id = id
        self.__name = name
        self.__phone = phone
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getPhone(self):
        return self.__phone
