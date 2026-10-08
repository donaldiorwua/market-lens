from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.collection_service import collect_market_data


app = FastAPI()


@app.get("/api/v1/collect")
def collect(db: Session = Depends(get_db)):
    products, failed_sources = collect_market_data(db)

    return {
        "products": products,
        "failed_sources": failed_sources,
    }
