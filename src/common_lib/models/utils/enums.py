from enum import StrEnum


class ExchangeType(StrEnum):
    fixed = "FIXED"
    basic_margin = "BASIC_MARGIN"
    percent_margin = "PERCENT_MARGIN"


class UserRole(StrEnum):
    member = "MEMBER"
    moderator = "MODERATOR"
    administrator = "ADMINISTRATOR"


__all__ = ["ExchangeType", "UserRole"]
