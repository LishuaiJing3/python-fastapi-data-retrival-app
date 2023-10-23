from dateutil import parser


def normalize_date_format(date_str):
    date = parser.parse(date_str)
    normalized_date_str = date.strftime("%Y-%m-%d")
    return normalized_date_str
