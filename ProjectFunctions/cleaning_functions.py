def deleting_keys(json,lst_keys_no_req):
    for i in range(len(json)):
        for e in lst_keys_no_req:
            if e in json[i]:
                del json[i][e]
    return json
