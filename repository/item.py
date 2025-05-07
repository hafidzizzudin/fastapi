from models.item import Item, items


class ItemRepository:
    def __init__(self):
        self.items = items

    def get_items(self) -> list[Item]:
        return [item for item in self.items.values()]

    def get_item(self, item_id: int) -> Item:
        return self.items.get(item_id)

    def create_item(self, item: Item) -> Item:
        last_id = max(self.items.keys())
        item.id = last_id + 1
        self.items[item.id] = item
        return item

    def update_item(self, item_id: int, item: Item) -> Item:
        self.items[item_id] = item
        return item
