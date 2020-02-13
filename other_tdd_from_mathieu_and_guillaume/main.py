def theBossFunction(b=1):
    bossDict = {"chameau": b*2, "dromadaire": b}
    chameau = int(bossDict["chameau"])
    dromadaire = int(bossDict["dromadaire"])
    res = chameau + dromadaire
    rslt = print(f"Il y a {res} bosses.")
    return rslt

# Insoluble: Dictionnaire à la fois dans et hors la fonction
