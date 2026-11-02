from abc import ABC, abstractmethod

from .models import Product


class InventoryADT(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_product(self, product_id: str) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    def remove_product(self, product_id: str) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError
