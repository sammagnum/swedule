import datetime


def get_date_range_m_f(date):
    dates_monday = date - datetime.timedelta(days=date.weekday())
    dates_friday = dates_monday + datetime.timedelta(days=5)
    dates_saturday = dates_monday + datetime.timedelta(days=6)
    return [dates_monday,dates_friday,dates_saturday]

