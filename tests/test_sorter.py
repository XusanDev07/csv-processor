from csv_utils.sorter import sort_rows


def test_sort_ascending_numeric():
    data = [{"price": "300"}, {"price": "100"}, {"price": "200"}]
    result = sort_rows(data, "price=asc")
    assert result[0]["price"] == "100"


def test_sort_descending_text():
    data = [{"brand": "apple"}, {"brand": "samsung"}, {"brand": "xiaomi"}]
    result = sort_rows(data, "brand=desc")
    assert result[0]["brand"] == "xiaomi"
