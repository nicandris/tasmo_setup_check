class _bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_title(title):
    print(_bc.OKCYAN + title + _bc.ENDC)


def print_result(error: False, value):
    if error:
        print(_bc.OKGREEN + value + _bc.ENDC)
    else:
        print(_bc.WARNING + value + _bc.ENDC)


def print_error(error):
    print(_bc.FAIL + str(error) + _bc.ENDC)


def print_status(url, value, status):
    print(_bc.OKCYAN + url + ' - ', _bc.OKGREEN + value,
          _bc.OKCYAN + str(status) + _bc.ENDC)
