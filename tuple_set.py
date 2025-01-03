# Tuple and Set

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

print(process_items([1, 2, "Saroj"], {100, 200, 300}))