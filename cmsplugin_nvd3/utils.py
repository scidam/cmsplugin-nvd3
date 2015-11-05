from django.conf import settings


def _xdataloader(xdata):
    data = None
    try:
        data = xdata.split(settings.CMSNVD3_DATASEP)
    except AttributeError:
        pass
    return [x.strip() for x in data]


def _ydataloader(ydata):
    data = []
    try:
        for item in ydata.split(settings.CMSNVD3_YDATAGROUPSEP):
            try:
                data.append([x.strip() for x in item.split(
                                            settings.CMSNVD3_DATASEP)])
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
