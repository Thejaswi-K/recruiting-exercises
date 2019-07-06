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
        ordered_items_keys = ordered_items.keys()
        if InventoryAllocator.__is_cart_quantity_not_empty(ordered_items):
            for warehouse in warehouses:
                inventory = warehouse['inventory']

                # Get the common items among the ordered items and inventory items
                matching_items = set(ordered_items_keys).intersection(
                    set(inventory.keys()))

                # filter the items to eliminate already processed items and make sure inventory items don't have zero quantity
                matching_items = {
                    i for i in matching_items if inventory[i] > 0 and ordered_items[i] > 0}

                if matching_items:
                    shipment_config = {}
                    for item in matching_items:
                        # calculating the shipment quantity for items
                        shipment_config[item] = ordered_items[item] if ordered_items[item] < inventory[item] else \
                            inventory[item]
                        # if inventory stock is more than ordered stock update ordered items to 0
                        # else update diff in ordered items
                        ordered_items[item] = ordered_items[item] - inventory[item] if inventory[item] < ordered_items[
                            item] else 0

                    shipment = {warehouse['name']: shipment_config}
                    res.append(shipment)

            # check if the quantities are all less than or equal to zero
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
    actual_result = allocator.cheapest_shipment_calculator({'apple': 10, 'orange': 7, 'banana': 4}, [
        {'name': 'abc', 'inventory': {'apple': 6, 'orange': 6}},
        {'name': 'def', 'inventory': {'banana': 4, 'orange': 1}},
        {'name': 'ghi', 'inventory': {'banana': 3, 'orange': 3, 'apple': 5}}
    ])

    print(actual_result)
