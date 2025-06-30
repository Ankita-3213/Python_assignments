class FileHandlingException(Exception):
    def __init__(self, message = "Error occured while handling file."):
        super().__init__(message)