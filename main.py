from fastapi import FastAPI, HTTPException, Query, Path
from services.products import add_product, get_all_products,delete_product
from schema.product import Product
from uuid import uuid4,UUID
from datetime import datetime
app = FastAPI()

@app.get("/")
def root():
    return {"message": "welcome to fastapi"}

@app.get("/products")
def list_products(

    name: str=Query(
        default=None
        ,max_length=100,
        min_length=1),
        sort_by: str = Query(default=None),
        order:str=Query(default="asc")
        ):
    
    products=get_all_products()
    if name:
        needle=name.strip().lower()
        products=[p for p in products if needle in p.get("name","").lower()]

        if not products:
            raise HTTPException(status_code=404,detail=f"no product found matching name={name}")
        
    if sort_by == "price":
        if order=="dsc":
           products = sorted(products, key=lambda p: p["price"],reverse=True)
        products = sorted(products, key=lambda p: p["price"])
    total=len(products)

    return {
        "total":total,
        "products":products
    }

@app.get("/products/{product_id}")
def get_product_by_id(product_id:str=Path(
    min_length=36,
    max_length=36,
    example="28282"
)):
    product=get_all_products()

    for p in product:
        if p["id"]==product_id:
            return product
        
    raise HTTPException(status_code=404,detail="product not found")


@app.post("/products", status_code=201)
def create_products(product: Product):
    product_dict = product.model_dump(mode="json")
    product_dict["id"] = str(uuid4())
    product_dict["created_at"] = datetime.utcnow().isoformat() + "Z"
    try:
        created = add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return created

@app.delete("/products/{product_id}")
def remove_product(product_id:UUID=Path(description="product id")):
    try:
        deleted=delete_product(str(product_id))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return deleted



