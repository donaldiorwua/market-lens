from datetime import datetime, timezone
from decimal import Decimal
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class RawProductData(BaseModel):
    product_name: str
    price:   Decimal
    currency: str
    location: str
    source: str
    availability: bool
    scraped_at: datetime

def utc_now():
    return datetime.now(timezone.utc)

class ProductData(BaseModel):
    product_id: UUID = Field(default_factory=uuid4)
    product_name: str
    price: Decimal
    currency: str
    location: str
    source: str
    availability: bool
    scraped_at: datetime = Field(default_factory=utc_now)
