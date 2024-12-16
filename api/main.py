from models import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import create_db_and_tables
from config.seed import seed
from config.cors import origins, allow_credentials, allow_methods, allow_headers
from routers import categories, coupons, markets

async def lifespan(app: FastAPI):
    create_db_and_tables()
    seed()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=allow_credentials,
    allow_methods=allow_methods,
    allow_headers=allow_headers,
)

app.include_router(categories.router)
app.include_router(coupons.router)
app.include_router(markets.router)

@app.get("/")
def health():
    return {"health": "healthy"}