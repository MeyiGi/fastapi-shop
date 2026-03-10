from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .config import settings
from .routes import product_router, cart_router, category_router
from .database import init_db
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],   
)

app.mount('/status', StaticFiles(directory=settings.static_dir), name="static")

app.include_router(product_router)
app.include_router(cart_router)
app.include_router(category_router)

@app.on_event('startup')
def on_startapp():
    init_db()

@app.get('/')
def root():
    return {
        "messsage" : "Welcome to fastapi shop API",
        "docs" : "api/docs"
    }

@app.get("/health")
def health_check():
    return {"status" : "ok"}