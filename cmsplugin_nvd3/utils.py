from django.conf import settings


def _try_all_numeric(array):
    '''tries to convert array of strings to array of numerical values.
    If floating point (symbol <.>)
    occurs in any array item, all values treated as floats.
    '''

    if any([True if settings.CMSNVD3_FLT_DELIMITER in x else False for x in array]):
        try:
            res = [float(x) for x in array]
        except:
            res = list(array)
    else:
        try:
            res = [int(x) for x in array]
        except:
            res = list(array)
    return res


def _xdataloader(xdata):
    data = None
    try:
        data = xdata.split(settings.CMSNVD3_DATASEP)
    except AttributeError:
        pass
    return _try_all_numeric([x.strip() for x in data])


def _ydataloader(ydata):
    data = []
    try:
        for item in ydata.split(settings.CMSNVD3_YDATAGROUPSEP):
            try:
                data.append(_try_all_numeric([x.strip() for x in item.split(
                                            settings.CMSNVD3_DATASEP)]))
            except:
                pass
    except AttributeError:
        pass
    return data


def _safe_int(x):
    try:
        res = int(x)
    except:
        return None
    if res < 0.0 or res > settings.CMSNVD3_MAX_CONT_DIM:
        return None
    return res
