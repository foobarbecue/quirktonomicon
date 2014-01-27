import calendar

def dt2jsts(mdatetime):
    """
    Given a python datetime, convert to javascript timestamp format (milliseconds since Jan 1 1970).
    Do so with microsecond precision, and without adding any timezone offset.
    """
    return calendar.timegm(mdatetime.timetuple())*1e3+mdatetime.microsecond/1e3