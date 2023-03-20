from dataclasses import fields
from typing import Any
from pydantic.dataclasses import dataclass


@dataclass
class BaseModel:
    # Does not work:
    # return tuple(f for f in fields.values() if f._field_type is _FIELD)
    #                             ^^^^^^^^^^^^^
    # AttributeError: 'NoneType' object has no attribute 'values'
    def to_dict(self, exclude: tuple[str, ...] = tuple()) -> dict[str, Any]:
        return {field.name: getattr(self, field.name) for field in fields(self) if field.name not in exclude}
