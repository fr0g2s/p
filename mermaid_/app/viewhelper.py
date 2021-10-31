def get_cityinfo(filedir, filename):
    cityinfo = []
    if filename is None:
        return None
    
    try:
        with open(filedir+filename) as f:
            content = list(filter(lambda x: x != '', f.read().split('\n')))
            for city in content:
                cityinfo.append(tuple(city.split(',')))          
    except Exception as e:
        print(e)
        return None
    return tuple(cityinfo)