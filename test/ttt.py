with open("a.txt", mode="r", encoding="utf-8") as f:
    res=f.read().splitlines()
    print(res,type(res))
