marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]
valid=[]
grades={}
grade_count={}
count=0
for i in marks:
    if i<0 or i>100:
        continue
    else:
        valid.append(i)
print(valid)
for i in valid:
    if i>=80:
        grades[i]='A'
    elif 70<=i<80:
        grades[i]='B'
    elif 60<=i<70:
        grades[i]='C'
    else:
        grades[i]='Fail'

for value in grades.values():
    grade_count[value]=grade_count.get(value,0)+1

for i in valid:
  count+=i

average=count/len(valid)


print(grades)
print(grade_count)
print(average)