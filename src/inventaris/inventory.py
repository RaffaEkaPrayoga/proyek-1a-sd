from .interfaces import InventoryADT
from .models import Product


class Inventory(InventoryADT):
    def __init__(self) -> None:
        self._products: dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Data yang ditambahkan harus berupa objek Product.")

        if product.product_id in self._products:
            raise ValueError(
                f"Produk dengan ID '{product.product_id}' sudah terdaftar."
            )

        self._products[product.product_id] = product

    def get_product(self, product_id: str) -> Product | None:
        normalized_id = self._normalize_id(product_id)
        return self._products.get(normalized_id)

    def remove_product(self, product_id: str) -> Product | None:
        normalized_id = self._normalize_id(product_id)
        return self._products.pop(normalized_id, None)

    def __len__(self) -> int:
        return len(self._products)

    @staticmethod
    def _normalize_id(product_id: str) -> str:
        if not isinstance(product_id, str):
            raise TypeError("ID produk harus berupa string.")
        return product_id.strip().upper()

    def get_all_products(self) -> tuple[Product, ...]:
        return tuple(self._products.values())
