def namelist(names):
    nam=[i['name'] for i in names]
    if len(nam) <= 1:
        return ' '.join(nam)
    else: 
        m = ', '.join(map(str,nam[:-1]))
        res = m + ' & '+ nam[-1]
        return res
