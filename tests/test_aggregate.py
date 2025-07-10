from csv_utils.aggregate import aggregate_column


def test_aggregate_avg():
    data = [{"price": "100"}, {"price": "200"}, {"price": "300"}]
    result = aggregate_column(data, "price=avg")
    assert "200.0" in result


def test_aggregate_min():
    data = [{"rating": "3.5"}, {"rating": "5.0"}]
    result = aggregate_column(data, "rating=min")
    assert "3.5" in result


def test_aggregate_max():
    data = [{"views": "12"}, {"views": "50"}, {"views": "34"}]
    result = aggregate_column(data, "views=max")
    assert "50.0" in result
