class ApplicationError(Exception):
    """アプリケーション全体で使う共通のエラーベース"""

    status_code = 400  # デフォルトは 400 Bad Request

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class NotFoundError(ApplicationError):
    status_code = 404


class AlreadyExistsError(ApplicationError):
    status_code = 400


class RecordOperationError(ApplicationError):
    status_code = 500


class InvalidDataError(ApplicationError):
    status_code = 400
