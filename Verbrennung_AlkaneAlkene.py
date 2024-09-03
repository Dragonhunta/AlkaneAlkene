# -*- coding: cp1252 -*-

c = int(input("Anzahl der C-Atome: "))
group = input("Alkan oder Alken: ")
kind = input("Endprodukt (CO2 / CO / C): ")

c2 = c
h = 0

if group.lower() == "alkan":
    h = c * 2 + 2
elif group.lower() == "alken":
    h = c * 2
else:
    print("Fehler")

h2o = h

if kind.lower() == "co2":
    o2 = (c2 * 2 + h) / 2
    remainder = (c2 * 2 + h) % 2
elif kind.lower() == "co":
    o2 = (c2 + h) / 2
    remainder = (c2 + h) % 2
elif kind.lower() == "c":
    o2 = h / 2
    remainder = h % 2
else:
    print("Fehler")

if remainder > 0:
    c2 = c2 * 2
    h2o = h2o * 2
    o2 = o2 * 2
    if kind == "CO2" or kind == "co2":
        print("2 C%sH%s + %s O2 --> %s CO2 + %s H2O" % (c, h, o2, c2, h2o))
    elif kind.lower() == "co":
        print("2 C%sH%s + %s O2 --> %s CO + %s H2O" % (c, h, o2, c2, h2o))
    elif kind.lower() == "c":
        print("2 C%sH%s + %s O2 --> %s C + %s H2O" % (c, h, o2, c2, h2o))
else:
    if kind == "CO2" or kind == "co2":
        print("C%sH%s + %s O2 --> %s CO2 + %s H2O" % (c, h, o2, c2, h2o))
    elif kind.lower() == "co":
        print("C%sH%s + %s O2 --> %s CO + %s H2O" % (c, h, o2, c2, h2o))
    elif kind.lower() == "c":
        print("C%sH%s + %s O2 --> %s C + %s H2O" % (c, h, o2, c2, h2o))
