def myzip(name, id, point, strct = False):
    if strct:
        if len(name) == len(id) and len(id) == len(point):
            pass
        else:
            return "Unequal Lengths"
    return list(zip(name, id, point))

print(myzip(["aakri", "utk", "ras"], ["122", "123"], ["122", "1234"]))