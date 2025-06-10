info = {
    "key" : "value",
    "name" : "BIDUR",
    "learning" : "coding",
    "age" : 25,
    "is_adult" : True

 }
info["surname"] = "shrestha" #adding key and value
print(info)
print(info["name"])

# nested dictionaries
student = {
    "name" : "biman",
    "subjects" : {
        "phy": 97,
        "chem":96,
        "math":92,
    }
}
print(student)
print(student["subjects"])
# dictionaries methods
print(student.keys())
print(len(student))
print(student.values())
print(student.items())
print(student.get("subjects"))

new_dict={"sity":"ktm"}
student.update(new_dict)