import numpy as np
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\d{3}-{0,1}\d{3}-{0,1}\d{4}$')
zip_regex = RegexValidator(regex=r'^\d{5}$')


def validate_nan(x) -> bool:
    """
    return True if valid entry
    """
    if isinstance(x, str):
        if x:
            return True
        else:
            return False
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return False
    return True


def normalize_nans(data):
    for k, v in data.items():
        if not validate_nan(v):
            data[k] = ""
    return data


def validate_len(self, fix_len, elm, field="number"):
    if not np.isnan(elm):
        if len(elm) != fix_len:
            ValidationError(
                "Value of {} is not of length {}".format(field, l))


def normalize_raw_data(data):
    """
    Normalize request data to use
    @param data:
    @return:
    """
    norm_data = {}
    for key, val in dict(data.lists()).items():
        norm_data[key] = val[0]
    return norm_data
