# 2...
#  Write a Python script to merge two Python dictionaries.

d1 = {
    "f1" : "Mango",
    "f2" : "watermelon"
}
print("Dictionary d1 is",d1)

d2 = {
    "f3" : "Apple",
    "f4" : "Orange"
}
print("Dictionary d2 is",d2)

d1.update(d2)
print("Updated dictionary is",d1)