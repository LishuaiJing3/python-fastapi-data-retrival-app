from python_fastapi_data_retrival_app.fastAPi_backend import normalize_date_format


def test_normalize_date_format():
    assert normalize_date_format("2022-01-01") == "2022-01-01"
    assert normalize_date_format("2022/01/01") == "2022-01-01"
    assert normalize_date_format("01/01/2022") == "2022-01-01"
    assert normalize_date_format("2022-01-01T00:00:00.000Z") == "2022-01-01"
    assert normalize_date_format("2022-01-01T00:00:00") == "2022-01-01"