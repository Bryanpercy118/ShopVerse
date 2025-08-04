import httpx

PRODUCT_SERVICE_URL = "http://localhost:8002" 

def get_product_by_id(product_id: int) -> dict:
    try:
        response = httpx.get(f"{PRODUCT_SERVICE_URL}/internal/products/{product_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as exc:
        print(f"Error al consultar producto {product_id}: {exc.response.status_code}")
        return None
