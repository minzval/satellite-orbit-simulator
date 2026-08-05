from datetime import datetime

from sgp4.api import jday


def datetime_to_julian(dt: datetime):
    """
    Convert a Python datetime object into
    Julian Day + Fraction required by SGP4.
    """

    jd, fr = jday(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second + dt.microsecond / 1_000_000
    )

    return jd, fr