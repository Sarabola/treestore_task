from typing import Optional

class TreeStore:
    """Класс реализующий древесную структуру."""
    def __init__(self, items: list[dict[str, str | int]]):
        self.items = items
        self._items_dict = {}
        self._children_dict = {}

        for item in items:
            self._items_dict[item["id"]] = item
            parent_id = item.get("parent")

            if parent_id not in self._children_dict:
                self._children_dict[parent_id] = []

            self._children_dict[parent_id].append(item)

    def getAll(self) -> list[dict[str, str | int]]:
        """Возвращает изначаольный массив."""
        return self.items

    def getItem(self, item_id: int) -> Optional[dict[str, str | int]]:
        """Возвращает элемент по его ID."""
        return self._items_dict.get(item_id)

    def getChildren(self, parent_id: int) -> list[Optional[dict[str, str | int]]]:
        """Возвращает дочерние элементы родительского класса."""
        return self._children_dict.get(parent_id, [])

    def getAllParents(self, children_id: int) -> list[Optional[dict[str, str | int]]]:
        result = []
        current_id = children_id

        while current_id is not None and current_id != "root":
            item = self.getItem(current_id)

            if item is None:
                break

            if item["id"] == children_id:
                current_id = item.get("parent")
                continue

            result.append(item)
            current_id = item.get("parent")

        return result


if __name__ == "__main__":
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)

    getall = [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
    getitem7 = {"id":7,"parent":4,"type":None}
    getchildren4 =  [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
    getchildren5 = []
    getallparents7 = [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]

    print("Expected:", getall)
    print("Result:", ts.getAll())

    print("Expected:", getitem7)
    print("Result:", ts.getItem(7))

    print("Expected:", getchildren4)
    print("Result:", ts.getChildren(4))

    print("Expected:", getchildren5)
    print("Result:", ts.getChildren(5))

    print("Expected:", getallparents7)
    print("Result:", ts.getAllParents(7))

