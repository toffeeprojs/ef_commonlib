from pydantic_extra_types.coordinate import Coordinate
from typing import Annotated, Self
from pydantic import Field, BaseModel, model_validator
from decimal import Decimal
from .utils import DisableLogic, DataTimeField
from .utils.enums import UserRole, ExchangeType


class User(DisableLogic):
    id: int
    location: Coordinate
    is_pined: bool = False
    first_name: Annotated[str, Field(max_length=64)]
    last_name: Annotated[str, Field(max_length=64)] | None = None
    username: Annotated[str, Field(max_length=32)] | None = None
    display_name: Annotated[str, Field(max_length=64)] | None = None
    role: UserRole = UserRole.member


class Currency(BaseModel):
    code: Annotated[str, Field(min_length=3, max_length=5, pattern=r"^[A-Z0-9]{3,5}$")]
    rate: Annotated[Decimal, Field(max_digits=15, decimal_places=6)]
    comment: Annotated[str, Field(min_length=8, max_length=128)] | None = None
    is_disabled: bool = False


class Exchange(DisableLogic):
    user_id: int
    currency_give: Annotated[
        str, Field(min_length=3, max_length=5, pattern=r"^[A-Z0-9]{3,5}$")
    ]
    currency_get: Annotated[
        str, Field(min_length=3, max_length=5, pattern=r"^[A-Z0-9]{3,5}$")
    ]
    exch_type: ExchangeType
    rate: Annotated[Decimal, Field(max_digits=15, decimal_places=6)]
    comment: Annotated[str, Field(max_length=512)] | None = None
    is_pined: bool = False

    @model_validator(mode="after")
    def _give_get_check(self) -> Self:
        if self.currency_give == self.currency_get:
            raise ValueError()
        return self


class DatabaseUpdate(DataTimeField):
    database_name: str
    table_name: str
    data_key: dict[str, str]
    updated_data: dict[str, str]


class HandlerCall(DataTimeField):
    service_name: str
    handler_name: str
    handler_args: dict[str, str]


__all__ = ["User", "Currency", "Exchange", "DatabaseUpdate", "HandlerCall"]
