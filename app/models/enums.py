import enum


class RoleType(enum.Enum):
    user = "user"
    # admin = "admin"


class ConditionType(enum.StrEnum):
    poor = "Poor"
    good = "Good"
    very_good = "Very Good"
    excellent = "Excellent"
    near_mint = "Near Mint"
    mint = "Mint"
