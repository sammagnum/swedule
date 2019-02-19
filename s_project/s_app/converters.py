import datetime


class DateConverter:
    regex = '[0-9]{4}-[0-1]?[0-9]-[0-3]?[0-9]'

    def to_python(self, value):
        arg_list = value.split('-')
        year = int(arg_list[0])
        month = int(arg_list[1])
        day = int(arg_list[2])
        return datetime.date(year, month, day)

    def to_url(self, date):
        return str(date).split(' ')[0]
