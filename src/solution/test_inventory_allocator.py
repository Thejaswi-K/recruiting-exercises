from inventory_allocator import InventoryAllocator


def test_not_enough_inventory():
    allocator = InventoryAllocator()
    actual_result = allocator.cheapest_shipment_calculator({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 0}}])
    expected_result = []
    assert actual_result == expected_result


def test_exact_match():
    allocator = InventoryAllocator()
    actual_result = allocator.cheapest_shipment_calculator({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}])
    expected_result = [{'name': 'owd', 'inventory': {'apple': 1}}]
    assert actual_result == expected_result


def test_multiple_match1():
    allocator = InventoryAllocator()
    actual_result = allocator.cheapest_shipment_calculator({'apple': 10}, [{'name': 'owd', 'inventory': {'apple': 5}},
                                                                           {'name': 'dm', 'inventory': {'apple': 5}}])
    expected_result = [{'name': 'owd', 'inventory': {'apple': 5}},
                       {'name': 'dm', 'inventory': {'apple': 5}}]
    assert actual_result == expected_result


def test_multiple_match():
    allocator = InventoryAllocator()
    actual_result = allocator.cheapest_shipment_calculator({'apple': 10, 'orange': 7, 'onion': 0}, [
        {'name': 'abc', 'inventory': {'apple': 6, 'orange': 6}},
        {'name': 'def', 'inventory': {'banana': 4}},
        {'name': 'ghi', 'inventory': {'banana': 3, 'orange': 3, 'apple': 5}}
    ])
    expected_result = [{'name': 'abc', 'inventory': {'apple': 6, 'orange': 6}},
                       {'name': 'ghi', 'inventory': {'banana': 3, 'orange': 3, 'apple': 5}}]
    assert actual_result == expected_result


def test_partial_match():
    allocator = InventoryAllocator()
    actual_result = allocator.cheapest_shipment_calculator({'apple': 10, 'orange': 7, 'onion': 0}, [
        {'name': 'abc', 'inventory': {'apple': 6, 'orange': 6}},
        {'name': 'def', 'inventory': {'banana': 4}},
        {'name': 'ghi', 'inventory': {'banana': 3, 'apple': 5}}])
    expected_result = []
    assert actual_result == expected_result


def test_partial_match1():
    allocator = InventoryAllocator()
    actual_result = allocator.cheapest_shipment_calculator({'apple': 12, 'orange': 7, 'banana': 5}, [
        {'name': 'abc', 'inventory': {'apple': 6, 'orange': 6}},
        {'name': 'def', 'inventory': {'banana': 4}},
        {'name': 'ghi', 'inventory': {'banana': 3, 'orange': 3, 'apple': 5}}
    ])
    expected_result = []
    assert actual_result == expected_result
