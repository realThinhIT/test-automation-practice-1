import calendar
import time


def get_current_timestamp():
    return calendar.timegm(time.gmtime())


def generate_unique_email():
    return 'test.automation+{}@got-it.ai'.format(get_current_timestamp())
