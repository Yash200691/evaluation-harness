from src.agent_eval.environment.mock_store import MockStore
from langchain_core.tools import tool

store = MockStore()

@tool
def search_products(category: str|None=None, max_price: float|None=None, min_ram: int|None=None):
    """
    Search for products based on category, maximum price, and minimum RAM.

    Args:
        category (str): The category of the product to search for.
        max_price (float): The maximum price of the product.
        min_ram (int): The minimum RAM required for the product.

    Returns:
        dictionary: A dictionary containing the search results with product details.
    """
    products = store.search_products(category, max_price, min_ram)
    return {
        "products": [product.model_dump() for product in products]
    }

@tool
def get_product_details(product_id: str):
    """
    Get the details of a specific product by its ID.

    Args:
        product_id (str): The ID of the product to retrieve details for.

    Returns:
        dictionary: A dictionary containing the product details.
    """
    product = store.get_product_details(product_id)
    if product:
        return {
            "product": product.model_dump()
        }
    else:
        return {
            "error": f"Product with ID '{product_id}' not found."
        }

@tool
def add_to_cart(product_id: str, quantity: int):
    """
    Add product to shopping cart.
    
    Args:
        product_id(str):The id of the product to add to the cart.
        quantity(int):the quantity of the product to add to the cart.
        
        Returns:
        dict: A dictionary containing the result of the operation.
        """
    if(quantity<=0):
        return {
            "success": False,
            "message": "Quantity must be greater than zero",
            "product_id": product_id,
            "quantity": quantity
        }
    result=store.add_to_cart(product_id,quantity=quantity)
    return result

@tool
def checkout():
    """
    Checkout the items in the shopping cart.

    Returns:
        dict: A dictionary containing the result of the checkout operation.
    """
    result=store.checkout()
    return result

shopping_tools=[
    search_products,
    get_product_details,
    add_to_cart,
    checkout
]

