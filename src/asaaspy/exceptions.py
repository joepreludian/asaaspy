class AsaasClientError(Exception):
    def __init__(self, message: str, status_code: int, details: dict = None):
        self.message = message
        self.status_code = status_code
        self.details = details

    def __str__(self):
        return_message = f"HTTP {self.status_code}"

        if self.message:
            return_message += f": {self.message}"

        if self.details:
            return_message += f": {self.details}"

        return return_message
