class ServiceError(Exception):
    def __init__(self, detail, status_code: int = 400):
        self.detail = detail
        self.status_code = status_code
        super().__init__(detail)
