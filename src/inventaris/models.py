from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Product:
    product_id: str
    name: str
    category: str
    price: float
    stock: int

    def __post_init__(self) -> None:
        # Normalisasi ID agar pencarian konsisten.
        normalized_id = self.product_id.strip().upper()
        object.__setattr__(self, "product_id", normalized_id)

        if not normalized_id:
            raise ValueError("ID produk tidak boleh kosong.")
        if not self.name.strip():
            raise ValueError("Nama produk tidak boleh kosong.")
        if not self.category.strip():
            raise ValueError("Kategori produk tidak boleh kosong.")
        if self.price < 0:
            raise ValueError("Harga tidak boleh bernilai negatif.")
        if self.stock < 0:
            raise ValueError("Stok tidak boleh bernilai negatif.")
