from fastapi import FastAPI
from app.services.collection_service import collect_market_data


app = FastAPI(
    title="Market Lens",
    description="AI-powered market intelligence platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/v1/collect")
def collect_products():
    products, failed_sources = collect_market_data()

    return {
        "products": products,
        "failed_sources": failed_sources,
    }