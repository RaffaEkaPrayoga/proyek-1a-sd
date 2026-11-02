import pytest

from inventaris import Inventory, Product


@pytest.fixture
def inventory() -> Inventory:
    return Inventory()


def sample_product(product_id: str = "EL-001") -> Product:
    return Product(product_id, "Laptop", "Elektronik", 8_000_000, 10)


def test_add_and_get_product(inventory: Inventory) -> None:
    product = sample_product()
    inventory.add_product(product)

    assert inventory.get_product("EL-001") == product
    assert len(inventory) == 1


def test_search_is_case_insensitive_for_id(inventory: Inventory) -> None:
    product = sample_product("el-001")
    inventory.add_product(product)

    assert inventory.get_product(" EL-001 ") == product


def test_duplicate_id_is_rejected(inventory: Inventory) -> None:
    inventory.add_product(sample_product())

    with pytest.raises(ValueError, match="sudah terdaftar"):
        inventory.add_product(sample_product())


def test_remove_product(inventory: Inventory) -> None:
    product = sample_product()
    inventory.add_product(product)

    removed = inventory.remove_product("EL-001")

    assert removed == product
    assert inventory.get_product("EL-001") is None
    assert len(inventory) == 0


def test_remove_missing_product_returns_none(inventory: Inventory) -> None:
    assert inventory.remove_product("NOT-FOUND") is None


def test_product_rejects_negative_price() -> None:
    with pytest.raises(ValueError, match="Harga"):
        Product("EL-009", "Produk", "Kategori", -1, 0)


def test_get_all_products_returns_snapshot(inventory: Inventory) -> None:
    inventory.add_product(sample_product())

    result = inventory.get_all_products()

    assert len(result) == 1
    assert isinstance(result, tuple)
