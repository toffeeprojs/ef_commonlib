from pydantic import BaseModel, Field, model_validator
from typing import Annotated, Self


class DisableLogic(BaseModel):
    is_disabled: bool = False
    disable_comment: Annotated[str, Field(min_length=8, max_length=256)] | None = None

    @model_validator(mode="after")
    def disable_logic_validate(self) -> Self:
        if (self.is_disabled is True and self.disable_comment is None) or (
            self.is_disabled is False and self.disable_comment is not None
        ):
            raise ValueError()
        return self


__all__ = ["DisableLogic"]
