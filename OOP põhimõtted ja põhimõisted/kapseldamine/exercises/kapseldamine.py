"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, student_id):
        self.__name = name
        self.__id = student_id
        self.__status = "Active"
        
    def get_id(self):
        return self.__id
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_status(self, status):
        allowed_statuses = ['Active', 'Expelled', 'Finished', 'Inactive']
        if status in allowed_statuses:
            self.__status = status
    def get_status(self):
        return self.__status