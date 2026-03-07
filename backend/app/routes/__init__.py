from .products import router as product_router
from .cart import router as cart_router
from .categories import router as category_router

__all__ = ["product_router", "cart_router", "category_router"]