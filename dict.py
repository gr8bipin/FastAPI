def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

process_items({"Tomato": 100.0, "Potato": 50.0})