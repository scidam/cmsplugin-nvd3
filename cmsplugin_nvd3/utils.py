from cmsplugin_nvd3.settings import DATASEP,\
                YDATAGROUPSEP, MAX_CONTAINER_DIM


def _xdataloader(xdata):
    data = None
    try:
        data = xdata.split(DATASEP)
    except AttributeError:
        pass
    return [x.strip() for x in data]


def _ydataloader(ydata):
    data = []
    try:
        for item in ydata.split(YDATAGROUPSEP):
            try:
                data.append([x.strip() for x in item.split(DATASEP)])
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
    if res < 0.0 or res > MAX_CONTAINER_DIM:
        return None
    return res
