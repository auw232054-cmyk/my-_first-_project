delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}
marged=delivery_1|delivery_2
New_dict={}
total=0

for i in marged:
    New_dict[i]=delivery_1.get(i,0)+delivery_2.get(i,0)

for i,j in New_dict.items():
    total+=j

print("Combined dictionary:",New_dict)
print("Total",total)
    


    