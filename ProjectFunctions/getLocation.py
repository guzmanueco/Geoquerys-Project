def getLocation(lst):
    for i in range(len(lst)):
        longitude = lst[i]['geometry']['location']['lng']
        latitude = lst[i]['geometry']['location']['lat']
        loc = {
            'type':'Point',
            'coordinates':[latitude, longitude]
        }
        lst[i]['loc']=loc

    return lst