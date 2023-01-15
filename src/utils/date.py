from datetime import datetime as _datetime
from datetime import timedelta as _timedelta
from dateutil.parser import isoparse as _parse


def convert_string(value, format='%H:%M:%S %d-%m-%Y'):
    return _parse(value).strftime(format)


def compare_dates(value, now=_datetime.now().isoformat()):
    return (_parse(value) + _timedelta(minutes=-1)) <= _parse(now) <= (_parse(value) + _timedelta(minutes=1))
