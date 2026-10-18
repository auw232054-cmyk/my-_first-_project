scores = {
"Amina": {"python": 82, "statistics": 76, "calculus": 88},
"Maya": {"python": 58, "statistics": 64, "calculus": 61},
"Disha": {"python": 91, "statistics": 89, "calculus": 94},
"Nora": {"python": 45, "statistics": 52, "calculus": 56}
}
new_dic={}
highest_score=[]

average=0
for i,j in scores.items():
    total=0
    for name,score in j.items():
        total+=score
    average=total/len(j)
    if average<=60:
        status="fail"
    else:
        status="pass"
    new_dic[i]={"Average":average,"Status":status}

highest = max(new_dic, key=lambda i: new_dic[i]["Average"])

print("Rounded average",new_dic)
print(highest, new_dic[highest]["Average"])

