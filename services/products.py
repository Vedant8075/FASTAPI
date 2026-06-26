import json
from pathlib import Path
from typing import Dict, List

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "products.json"

def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_products(products: List[Dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=2)


def get_all_products() -> List[Dict]:
    return load_products()


def add_product(product: Dict) -> Dict:
    products = get_all_products()
    if any (p["sku"]== product["sku"] for p in products):
        raise ValueError("sku already exists")
    
    products.append(product)
    save_products(products)
    return product
    
def delete_product(id:str)->None:
    products=get_all_products()
    for ind,p in enumerate(products):
        if p["id"]==str(id):
            deleted=products.pop(ind)
            save_products(products)
            return {"message":"product deleted succesfully",
                    "data":deleted}
