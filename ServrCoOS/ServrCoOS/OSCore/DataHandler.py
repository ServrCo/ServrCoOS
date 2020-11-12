from OSCore import variables


def readProductType():
    f = 0
    f = open("OSData/ProductType.scos")

    ProductType = f.read()
    f.close()
    return ProductType

def open_log():
    return 0
def log(text):
    return 0

def close_log():
    return 0