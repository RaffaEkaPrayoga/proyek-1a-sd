from .inventory import Inventory
from .models import Product


def _read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input tidak boleh kosong.")


def _read_non_negative_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print("Nilai tidak boleh negatif.")
                continue
            return value
        except ValueError:
            print("Masukkan angka yang valid.")


def _read_non_negative_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                print("Nilai tidak boleh negatif.")
                continue
            return value
        except ValueError:
            print("Masukkan bilangan bulat yang valid.")


def _show_product(product: Product) -> None:
    print("\n--- DETAIL PRODUK ---")
    print(f"ID       : {product.product_id}")
    print(f"Nama     : {product.name}")
    print(f"Kategori : {product.category}")
    print(f"Harga    : Rp{product.price:,.2f}")
    print(f"Stok     : {product.stock}")
    print("---------------------")


def _add_product(inventory: Inventory) -> None:
    print("\n[TAMBAH PRODUK]")
    try:
        product = Product(
            product_id=_read_non_empty("ID produk     : "),
            name=_read_non_empty("Nama produk   : "),
            category=_read_non_empty("Kategori      : "),
            price=_read_non_negative_float("Harga (Rp)    : "),
            stock=_read_non_negative_int("Jumlah stok   : "),
        )
        inventory.add_product(product)
        print(f"Berhasil: produk '{product.product_id}' ditambahkan.")
    except (ValueError, TypeError) as error:
        print(f"Gagal menambahkan produk: {error}")


def _search_product(inventory: Inventory) -> None:
    print("\n[CARI PRODUK]")
    product_id = _read_non_empty("Masukkan ID produk: ")
    product = inventory.get_product(product_id)

    if product is None:
        print(f"Produk dengan ID '{product_id}' tidak ditemukan.")
    else:
        _show_product(product)


def _remove_product(inventory: Inventory) -> None:
    print("\n[HAPUS PRODUK]")
    product_id = _read_non_empty("Masukkan ID produk: ")
    removed = inventory.remove_product(product_id)

    if removed is None:
        print(f"Produk dengan ID '{product_id}' tidak ditemukan.")
    else:
        print(f"Produk '{removed.name}' ({removed.product_id}) berhasil dihapus.")


def _show_all(inventory: Inventory) -> None:
    products = inventory.get_all_products()
    print(f"\n[DAFTAR PRODUK] Total: {len(products)}")

    if not products:
        print("Inventaris masih kosong.")
        return

    print("-" * 88)
    print(f"{'ID':<14} {'NAMA':<25} {'KATEGORI':<18} {'HARGA':>15} {'STOK':>8}")
    print("-" * 88)
    for product in products:
        print(
            f"{product.product_id:<14} "
            f"{product.name[:24]:<25} "
            f"{product.category[:17]:<18} "
            f"{product.price:>15,.2f} "
            f"{product.stock:>8}"
        )
    print("-" * 88)


def _load_sample_data(inventory: Inventory) -> None:
    samples = [
        Product("EL-001", "Laptop ASUS Vivobook", "Elektronik", 8_500_000, 15),
        Product("EL-002", "Mouse Logitech M331", "Aksesori", 175_000, 50),
        Product("EL-003", "Keyboard Mechanical", "Aksesori", 450_000, 25),
    ]
    for product in samples:
        if inventory.get_product(product.product_id) is None:
            inventory.add_product(product)


def main() -> None:
    inventory = Inventory()
    _load_sample_data(inventory)

    while True:
        print("\n" + "=" * 45)
        print("       SISTEM MANAJEMEN INVENTARIS")
        print("=" * 45)
        print("1. Tambah produk")
        print("2. Cari produk berdasarkan ID")
        print("3. Hapus produk berdasarkan ID")
        print("4. Tampilkan semua produk")
        print("5. Lihat jumlah produk")
        print("0. Keluar")
        print("=" * 45)

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            _add_product(inventory)
        elif choice == "2":
            _search_product(inventory)
        elif choice == "3":
            _remove_product(inventory)
        elif choice == "4":
            _show_all(inventory)
        elif choice == "5":
            print(f"Jumlah produk saat ini: {len(inventory)}")
        elif choice == "0":
            print("Terima kasih. Program inventaris selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


if __name__ == "__main__":
    main()
