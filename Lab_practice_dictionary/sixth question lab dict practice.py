marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]
valid=[]
grades={}
for i in marks:
    if i<0 or i>100:
        continue
    else:
        valid.append(i)
print(valid)
if i>=80:
    grades[i]=