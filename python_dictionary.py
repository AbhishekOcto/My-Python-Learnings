# Create a dictionary that contain three dictionaries
# nested dictionary
myfamily = {
    "child1": {
        "name": "Sunny",
        "year": 2005
    },
    "child2": {
        "name": "Anshu",
        "year": 2011
    },
    "child3": {
        "name": "Sohu",
        "year": 2007
    }
}
print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
student1 = {
    "name": "Abhishek",
    "roll": 1
}
student2 = {
    "name": "Avinash",
    "roll": 48
}
student3 = {
    "name": "ranjeet",
    "year": 35
}

students = {
    "student1": student1,
    "student2": student2,
    "student3": student3
}

print(students)


print(students["student2"]["roll"])    # access items in nested dictionary
