from csv_utils.filter import filter_rows


def test_filter_greater_than():
    data = [{"price": "100"}, {"price": "300"}, {"price": "50"}]
    result = filter_rows(data, "price>100")
    assert len(result) == 1
    assert result[0]["price"] == "300"


def test_filter_equal():
    data = [{"brand": "apple"}, {"brand": "samsung"}]
    result = filter_rows(data, "brand=apple")
    assert len(result) == 1
    assert result[0]["brand"] == "apple"


def test_filter_less_than():
    data = [{"rating": "4.1"}, {"rating": "4.9"}]
    result = filter_rows(data, "rating<4.5")
    assert len(result) == 1
    assert result[0]["rating"] == "4.1"
