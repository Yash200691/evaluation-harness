from src.agent_eval.environment.mock_store import MockStore


class ToolRouter:
    def __init__(self, store:MockStore):
        self.store = store

    def execute(self,tool_name:str,arguments:dict)->dict:
        if tool_name=="search_products":
            category = arguments.get("category")
            max_price = arguments.get("max_price")
            min_ram = arguments.get("min_ram")
            products = self.store.search_products(category=category,max_price=max_price,min_ram=min_ram)
            return {"products":[product.dict() for product in products]}
        elif tool_name=="get_product_details":
            product_id=arguments.get("product_id")
            product=self.store.get_product_details(product_id=product_id)
            if product:
                return {"product":product.dict()}
            else:
                return {"error":"Product not found"}
        elif tool_name=="add_to_cart":
            product_id=arguments.get("product_id")
            quantity=arguments.get("quantity")
            result=self.store.add_to_cart(product_id=product_id,quantity=quantity)
            return {"result":result}
        elif tool_name=="checkout":
            result=self.store.checkout()
            return {"result":result}
        else:
            return {"error":"Tool not found"}