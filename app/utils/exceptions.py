from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)

class ConflictException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=409, detail=detail)

class NotificationFailedException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)
 