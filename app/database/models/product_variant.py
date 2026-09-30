import uuid
from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String

from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False,
    )

    source_variant_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    product: Mapped["Product"] = relationship(
        back_populates="variants",
    )

    price_observations: Mapped[list["PriceObservation"]] = relationship(
        back_populates="variant",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "source_variant_id",
            name="uq_variant_product_source_variant_id",
        ),
    )