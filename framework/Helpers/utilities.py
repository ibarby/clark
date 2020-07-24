import random
import string


class GeneratorUtilities(object):
    @staticmethod
    def get_random_email(length):
        symbols = string.ascii_lowercase + string.digits
        index = "".join([random.choice(symbols) for i in range(length)])
        return f'qa+{index}@mailinator.com'

    @staticmethod
    def get_random_digit_number(length):
        return "".join([random.choice(string.digits) for i in range(length)])
