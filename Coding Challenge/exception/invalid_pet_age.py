class InvalidAge(Exception):
    def __init__(self, message="Age of pet should be positive"):
        super().__init__(message)