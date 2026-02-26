"""Securitas Direct API exceptions."""


class SecuritasDirectError(Exception):
    """Base class for Securitas Direct errors."""


class APIError(SecuritasDirectError):
    """Exception raised when API fails."""


class LoginError(SecuritasDirectError):
    """Exception raised when login fails."""


class AuthError(LoginError):
    """Exception raised when API denies access."""


class TokenRefreshError(LoginError):
    """Exception raised when the token needs refreshing."""


class Login2FAError(LoginError):
    """Exception raised when a 2FA authentication is needed."""


class ArmWithOpenSensorsError(SecuritasDirectError):
    """Raised when arming is blocked by open sensors but forcing is allowed."""

    def __init__(
        self, message: str, exceptions_number: int, exceptions_reference_id: str
    ) -> None:
        super().__init__(message)
        self.exceptions_number = exceptions_number
        self.exceptions_reference_id = exceptions_reference_id
