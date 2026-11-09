
from src.agent_eval.environment.mock_store import MockStore

store = MockStore()

def test_store_initialization():
    assert len(store.products)==5
    assert store.cart=={}


def test_search_products():
    # Test searching by category
    laptops = store.search_products(category="laptop")
    assert len(laptops)==5

    # Test searching by max price
    affordable_laptops = store.search_products(max_price=50000)
    assert len(affordable_laptops)==3

    # Test searching by min RAM
    high_ram_laptops = store.search_products(min_ram=16)
    assert len(high_ram_laptops)==3

    # Test searching with multiple criteria
    specific_laptops = store.search_products(category="laptop", max_price=60000, min_ram=16)
    assert len(specific_laptops)==3