from pydantic_extra_types.coordinate import Coordinate
from typing import Annotated
from pydantic import Field
from decimal import Decimal
from .items import User, Currency, Exchange
from .utils import UnsettedValidator
from .utils.enums import UserRole, ExchangeType


class UserUpdate(User, UnsettedValidator):
    _PRIMARY_KEYS = {"id"}

    location: Coordinate | None = None
    is_pined: bool | None = None
    first_name: Annotated[str, Field(max_length=64)] | None = None
    role: UserRole | None = None


class CurrencyUpdate(Currency, UnsettedValidator):
    _PRIMARY_KEYS = {"code"}

    rate: Annotated[Decimal, Field(max_digits=15, decimal_places=6)] | None = None
    is_disabled: bool | None = None


class ExchangeUpdate(Exchange, UnsettedValidator):
    _PRIMARY_KEYS = {"user_id", "currency_give", "currency_get"}

    exch_type: ExchangeType | None = None
    rate: Annotated[Decimal, Field(max_digits=15, decimal_places=6)] | None = None
    is_pined: bool | None = None


__all__ = ["UserUpdate", "CurrencyUpdate", "ExchangeUpdate"]
