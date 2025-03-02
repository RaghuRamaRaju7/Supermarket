from datetime import datetime

name=input("Enter Your Name:")

lists='''
rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 15/kg
oil     Rs 100/kg
paneer  Rs 100/kg
chicken Rs 225/kg
colgate Rs 79/each
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

items={'rice':20,'sugar':30,'salt':15,'oil':100,'paneer':100,'chicken':225,'colgate':79}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter Your Items:")
        quantity=int(input("Enter Quantity:"))
    if item in items.keys():
        price=quantity*(items[item])
        totalprice += price
        pricelist.append((item,quantity,items[item],price,))
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
        gst=(totalprice*5)/100
        finalamount=gst+totalprice
    else:
        print("Sorry You Entered Item Is Not Available")
else:
    print("You Entered Wrong Number")

inp=input("Can I Bell The Items Yes Or No:")
if inp=='yes':
    pass
    if finalamount!=0:
        print(25*"=", "Raghu SuperMarket", 25*"=")
        print(28*" ","Rajahmundry")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
        for i in range(len(pricelist)):
            print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*' ',plist[i])
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',totalprice)
        print("gst amount",40*" ",'Rs.gst')
        print(75*"-")
        print(50*" ",'FinalAmount:','Rs',finalamount)
        print(75*"-")
        print(20*" ", "Thanks for Visiting")
        print(75*"-")

