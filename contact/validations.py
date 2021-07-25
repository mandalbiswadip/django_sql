import numpy as np
from django.core.exceptions import ValidationError


def validate_len(self, fix_len, elm, field="number"):
    if not np.isnan(elm):
        if len(elm) != fix_len:
            ValidationError(
                "Value of {} is not of length {}".format(field, l))
