# person = ["quan", 20, "hanoi", ]
# print(person)

# person = {

# }

# print(person)

# person = {
#     "name": "quan"
# }
# print(person)

person = {
    "name": "quan",
    "age": 20,
    "city": "ha noi",
}

for k in person.keys():                   #in ra key
    print(k)
for v in person.values():                   # in ra values
    print(v)
for k, v in person.items():                    #in ra ca 2
    print(k, ":", v)
# print(person["status"])
# person["status"] = "complicated"
# print(person)
# del person["age"]
# print(person)
# print(person)
# print(person["city"])
# person["city"] = "da nang"
# print(person)
# key = "city"
# print(person[key])