class AdoptionException(Exception):
    def __init__(self, message="Adoption error !!"):
        super().__init__(message)