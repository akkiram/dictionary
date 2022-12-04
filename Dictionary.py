# Dictionary is used to store data values in key value pair
# orderedd
# duplicates are not allowed
# changable/mutable


# myDictionary = {
#     "name":"Ram",
#     "age":18,
#     "class":12,
#     "percentage":"81%"
# }
# a = myDictionary["name"]
# b = myDictionary.get("name")
# a = myDictionary.keys()
# a = myDictionary.values()
# a = myDictionary.items()
# myDictionary.update({"age":19})
# a = myDictionary.keys()
# b = myDictionary.values()
#myDictionary.pop("age")
#print(myDictionary



myDictionary = {
    "class":{
        "student":{
            "name" : "abc",
            "marks" : {
                "python" : 90,
                "web" : 95
            }
        }
    }
}

a = myDictionary["class"]["student"]["marks"]["web"]
print(a)