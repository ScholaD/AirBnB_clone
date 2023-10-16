#!/usr/bin/env python3

from models import storage
from models.base_model import BaseModel


print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print(".........")

my_model.my_number = 1000000001
my_model.save()
all_objs = storage.all()
print("-- new Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
