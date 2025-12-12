class AgeException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PhoneException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CpfException(Exception):
    def __init__(self, message):
        super().__init__(message)

class DateException(Exception):
    def __init__(self, message):
        super().__init__(message)
