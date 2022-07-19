# when we create an Object in python, it's gonna be associated to a data type e.g a string. integer, dict, array.
# an Object -- might be perceived as some kind of empty box. that you can put any sort of thing.
# it could hold a switch configuration, firewall policy or a hostname of a firewall.
# but when you create that object, python would try it's best to infer what type of data it is.

# ------
# ospf = 10
# type(ospf)

# so, we can perform actions on them based on the kind of data that they are.
# hostname = "router1"
# can't do arithmetic or carry out integer methods on a string.
# print(ospf)

# Lists
# devices = ["", ""] etc.
# index = 0

# Dicts
# they are great for storing complex structure of data.
# using keys and values.
# myDict = {
# "neighbour_ipAddr": "1.1.1.1", "asn": 50001,}
# print(myDict["asn"])