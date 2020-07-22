import re


def ignore_delimiters(str):
    str = str.lower()
    return "".join(re.split("[\W+ _]", str))


def get_offset(str, substr):
    return str.find(substr)

