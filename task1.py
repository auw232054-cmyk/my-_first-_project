shopping_li=['Shirt', 'pants', 'coat', 'jacket', 'sweater', 'Socks', 'shoes', 'boots', 'hat']
items_prices=[900,500,700,400,400,70,300,500,100]

items_and_price=[]
choice=input("Please inter the item you want to purchase:")

for i,j in zip(shopping_li,items_prices):
       zipped=(i,j)
       items_and_price.append(zipped)
       #print(items_and_price)
found=False
for i ,j in items_and_price:
       if choice==i: 
          print(f"{i} is {j} TK")
          found=True
          break
          
if found== False:
          items_and_price.append((choice,0))
          print("item is not found,so its added to the list")

    
#print(f"{i} is {j} TK")
print(items_and_price)
