stock = {"pen": 12, "book": 3, "bag": 2,
"ruler": 9, "calculator": 1}
total=0
quantities_below_5={}
for item,price in stock.items():
    total+=price
    if price<5:
        quantities_below_5[item]=price
    else:
       continue

print('Total:',total)
print("Low stock:",quantities_below_5)