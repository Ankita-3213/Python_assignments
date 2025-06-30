class NullReferenceException(Exception):
    def __init__(self, message="Missing information as name, age or breed. "):
        super().__init__(message)