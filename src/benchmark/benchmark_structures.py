
from time import perf_counter
from statistics import median

# 1. MODEL DATA
class Product:
    def __init__(self, product_id):
        self.product_id = product_id


# 2. CUSTOM LINKED LIST
class Node:
    def __init__(self, product):
        self.product = product
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, product):
        new_node = Node(product)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def search(self, product_id):
        current = self.head

        while current:
            if current.product.product_id == product_id:
                return current.product
            current = current.next

        return None

    def delete(self, product_id):
        current = self.head
        previous = None

        while current:
            if current.product.product_id == product_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current == self.tail:
                    self.tail = previous

                return current.product

            previous = current
            current = current.next

        return None


# 3. DATA PERSIAPAN
def generate_ids(size):
    return [f"PRD-{i:07d}" for i in range(size)]


def build_structure(ids, structure):
    if structure == "List":
        return [Product(pid) for pid in ids]

    elif structure == "Linked List":
        data = LinkedList()
        for pid in ids:
            data.append(Product(pid))
        return data

    elif structure == "Hash Table":
        return {pid: Product(pid) for pid in ids}


# 4. PENGUKURAN WAKTU
def measure_insert(ids, structure):
    start = perf_counter()

    if structure == "List":
        data = []
        for pid in ids:
            data.append(Product(pid))

    elif structure == "Linked List":
        data = LinkedList()
        for pid in ids:
            data.append(Product(pid))

    else:
        data = {}
        for pid in ids:
            data[pid] = Product(pid)

    return (perf_counter() - start) * 1000


def measure_search(data, target, structure):
    start = perf_counter()

    if structure == "List":
        result = next(
            (p for p in data if p.product_id == target), None
        )

    elif structure == "Linked List":
        result = data.search(target)

    else:
        result = data.get(target)

    return (perf_counter() - start) * 1000


def measure_delete(data, target, structure):
    start = perf_counter()

    if structure == "List":
        index = next(
            (i for i, p in enumerate(data)
             if p.product_id == target), None
        )
        result = data.pop(index) if index is not None else None

    elif structure == "Linked List":
        result = data.delete(target)

    else:
        result = data.pop(target, None)

    return (perf_counter() - start) * 1000


# 5. BENCHMARK
def benchmark():
    sizes = [100, 1000, 10000, 100000]
    structures = ["List", "Linked List", "Hash Table"]
    repeats = 7

    print("\n=== BENCHMARK SISTEM INVENTARIS ===")
    print("Waktu dalam milidetik (ms)")
    print("Median dari 7 pengujian\n")

    for size in sizes:
        ids = generate_ids(size)
        target = ids[size // 2]

        print(f"\nJUMLAH DATA: {size}")
        print("-" * 65)
        print(
            f"{'Operasi':<15} {'Struktur Data':<18} "
            f"{'Waktu (ms)':>12}"
        )
        print("-" * 65)

        for operation in ["Penyisipan", "Pencarian", "Penghapusan"]:
            for structure in structures:

                results = []

                for _ in range(repeats):
                    if operation == "Penyisipan":
                        elapsed = measure_insert(ids, structure)

                    else:
                        # Persiapan data tidak dihitung dalam waktu operasi.
                        data = build_structure(ids, structure)

                        if operation == "Pencarian":
                            elapsed = measure_search(
                                data, target, structure
                            )
                        else:
                            elapsed = measure_delete(
                                data, target, structure
                            )

                    results.append(elapsed)

                average = median(results)

                print(
                    f"{operation:<15} {structure:<18} "
                    f"{average:>12.6f}"
                )


if __name__ == "__main__":
    benchmark()
