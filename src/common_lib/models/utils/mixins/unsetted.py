from pydantic import BaseModel, model_validator
from typing import Self


class UnsettedValidator(BaseModel):
    _PRIMARY_KEYS: set[str] = set()

    @model_validator(mode="after")
    def _unsetted_fields_validate(self) -> Self:
        private_attr_val = getattr(self, '_PRIMARY_KEYS', set())
        if not self.model_dump(
            exclude_unset=True,
            exclude=private_attr_val,
        ):
            raise TypeError()
        return self


__all__ = ["UnsettedValidator"]
