

from itertools import product

from src.agent_eval.environment.product import Product


class MockStore:
    def __init__(self):
        self.products = [
            Product(
                product_id="laptop_001",
                name="Lenovo IdeaPad",
                category="laptop",
                price=55000,
                ram_gb=16,
                stock=5
            ),

            # Add the remaining four Product objects here.
            Product(
                product_id="laptop_002",
                name="Dell Inspiron",
                category="laptop",
                price=60000,
                ram_gb=16,
                stock=3
            ),
            Product(
                product_id="laptop_003",
                name="HP Pavilion",
                category="laptop",
                price=50000,
                ram_gb=8,
                stock=7
            ),
            Product(
                product_id="laptop_004",
                name="Asus VivoBook",
                category="laptop",
                price=45000,
                ram_gb=16,
                stock=2
            ),
            Product(
                product_id="laptop_005",
                name="Acer Aspire",
                category="laptop",
                price=48000,
                ram_gb=8,
                stock=4
            )
        ]

        self.cart = {}

    def search_products(self,category: str | None = None,max_price: float | None = None,min_ram: int | None = None,)->list[Product]:
        search_products = []
        for product in self.products:
            if category and product.category != category:
                continue
            if max_price is not None and product.price > max_price:
                continue
            if min_ram is not None and product.ram_gb < min_ram:
                continue
            search_products.append(product)

        return search_products

    def get_product_details(self,product_id:str)->Product | None:
        for product in self.products:
            if(product.product_id==product_id):
                return product
        return None

    def add_to_cart(self,product_id:str,quantity:int)->bool:
        product=self.get_product_details(product_id)
        if(product and product.stock>=quantity):
            if product_id in self.cart:
                self.cart[product_id]+=quantity
            else:
                self.cart[product_id]=quantity
            product.stock-=quantity
            return { 
                "success": True,
                "message": "Product added to cart",
                "product_id": product_id,
                "quantity": quantity
            }
        return {
            "success": False,
            "message": "Product not available or insufficient stock",
            "product_id": product_id,
            "quantity": quantity
        }

    def checkout(self)->dict:
        if not self.cart:
            return {
                "success": False,
                "message": "Cart is empty"
            }

        total_amount=0
        for product_id,quantity in self.cart.items():
            product=self.get_product_details(product_id)
            if product:
                total_amount+=product.price*quantity

        purchased_items = [
            {
                "product_id": product_id,
                "quantity": quantity,
            }
            for product_id, quantity in self.cart.items()
        ]

        self.cart.clear()
        return {
            "success": True,
            "message": "Checkout successful",
            "total_amount": total_amount,
            "purchased_items": purchased_items
        }
    

