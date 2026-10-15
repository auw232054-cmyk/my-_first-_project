words = ["model", "data", "python", "data",
"model", "analysis", "data"]
frequency={}
requested_word=[]
for item in words:
    frequency[item]=frequency.get(item,0)+1
for key,value in frequency.items():
    if value>=2:
        requested_word.append(key)

print("Frequency",frequency)
print("Repeated word",requested_word)
    
