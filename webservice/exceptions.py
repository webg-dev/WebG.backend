from fastapi import HTTPException


class WebPageDoesNotExist(HTTPException):
    def __init__(self, _id: str):
        super().__init__(
            status_code=404,
            detail=f'No web page exists in database with id: {_id}'
        )
