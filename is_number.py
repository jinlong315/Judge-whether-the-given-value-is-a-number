import unicodedata

def is_number(data):
    """judge the data type of the given data"""
    try:
        float(data)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(data)
        return True
    except (TypeError, ValueError):
        pass

    return False
