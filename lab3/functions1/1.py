def grams_to_ounces(grams):
    ounces = grams * 28.3495231
    return ounces

gramm = float(input("gramm: "))
print("ounces = ", grams_to_ounces(gramm))
