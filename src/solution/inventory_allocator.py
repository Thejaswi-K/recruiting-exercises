class InventoryAllocator:
    @staticmethod
    def cheapest_shipment_calculator(ordered_items, warehouses):
        """
        returns a list of cheapest warehouses to direct shipment
        :param ordered_items:
        :param warehouses:
        :return: list of warehouses with their shipments
        """
        res = []
        if InventoryAllocator.__is_cart_quantity_not_empty(ordered_items):
            for warehouse in warehouses:
                inventory = warehouse['inventory']

                matching_items = set(ordered_items.keys()).intersection(
                    set(inventory.keys()))

                matching_items = {
                    i for i in matching_items if inventory[i] > 0 and ordered_items[i] > 0}

                if matching_items:
                    for item in matching_items:
                        ordered_items[item] -= inventory[item]
                    res.append(warehouse)

        return [] if InventoryAllocator.__is_cart_quantity_not_empty(ordered_items) else res

    @staticmethod
    def __is_cart_quantity_not_empty(ordered_items):
        """
        checks if the ordered items have quantity greater than zero
        :param ordered_items:
        :return: list of item name having quantity greater than zer0
        """
        ans = [k for k, v in ordered_items.items() if v > 0]
        return ans


if __name__ == '__main__':
    allocator = InventoryAllocator()
    print(allocator.cheapest_shipment_calculator({'apple': 10, 'orange': 7}, [
        {'name': 'abc', 'inventory': {'apple': 6, 'orange': 6}},
        {'name': 'def', 'inventory': {'banana': 4}},
        {'name': 'ghi', 'inventory': {'banana': 3, 'apple': 5}}
    ]))

    print(allocator.cheapest_shipment_calculator(
        {'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}]))

    print(allocator.cheapest_shipment_calculator(
        {'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 0}}]))

    print(allocator.cheapest_shipment_calculator({'apple': 10}, [{'name': 'owd', 'inventory': {'apple': 5}},
                                                                 {'name': 'dm', 'inventory': {'apple': 5}}]))
