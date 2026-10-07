import uuid
from datetime import datetime, timezone
from decimal import Decimal
from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class PriceObservation(Base):
    __tablename__ = "price_observations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    variant_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("product_variants.id"),
        nullable=False,
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        # ISO currency codes such as NGN, USD, GBP
        # are only 3 characters, but keeping some room
        # makes the database less restrictive.
        String(3),
        nullable=False,
    )

    availability: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    observed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    variant: Mapped["ProductVariant"] = relationship(
        back_populates="price_observations",
    )