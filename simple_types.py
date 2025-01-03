def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

print(get_items("Bipin", 2, 86.38, True, (100).to_bytes(2, byteorder= 'big')))