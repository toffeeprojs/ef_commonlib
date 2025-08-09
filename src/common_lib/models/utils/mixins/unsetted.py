from pydantic import BaseModel, PrivateAttr, model_validator
from typing import Self


class UnsettedValidator(BaseModel):
    _PRIMARY_KEYS: set[str] = PrivateAttr(set())

    @model_validator(mode="after")
    def _unsetted_fields_validate(self) -> Self:
        private_attr_val = self._PRIMARY_KEYS.get_default()
        if not self.model_dump(
            exclude_unset=True,
            exclude=private_attr_val,
        ):
            raise TypeError()
        return self


__all__ = ["UnsettedValidator"]
