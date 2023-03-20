from sqlalchemy import Column, DateTime, func


class TimeStamp:
    created_at = Column(
        "created_at",
        DateTime,
        nullable=False,
        server_default=func.now(),
    )

    updated_at = Column(
        "updated_at",
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now()
    )
