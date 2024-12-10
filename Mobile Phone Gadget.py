item_dict={}
f = open("E:\\mobileinfo.txt","r")
while True:
  item=f.readline()
  if item=="\n":
      break
  qntt=f.readline()
  uprc= f.readline()
  item= item[:len(item)-1]
  qntt=int(qntt[:len(qntt)-1])
  uprc=float(uprc[:len(uprc)-1])
  item_dict[item]=[qntt,uprc]
f.close()


"""
item_dict= {
    "napa":[500,1.5],
    "napa extra":[1200,2.50],
    "seclo":[28000,5.75],
    "fenadin":[3000,1.50],
    "ace plus":[50,3.75],
    "Paracitamol":[280,6.70]
    }

"""

import pandas
def show_dict():
  
  pdata = pandas.DataFrame(item_dict)
  print(pdata)
  
  


def present_data():
    print(30*"=")
    print("Available Mobile and Quantity")
    print(30*"=")
    for x in item_dict:
        print(x, (20-len(x))*" ",
              (6-len(str(item_dict[x][0])))*" ",item_dict[x][0])
    print(30*"_")
#present_data()

def dec_quant(item, amount):
    item_dict[item][0]-=amount

def inc_quant(item, amount):
    item_dict[item][0]+=amount
def receive_order():
    while True:
        item= input("item(type's' to stop): ")
        if item=='s':
            break
        amnt= int(input("Amount: "))
        if item not in item_dict:
            print("New Mobile Found.")
            uprice=float(input("Enter the unique price: "))
            item_dict[item]=[amnt,uprice]
            continue
        inc_quant(item,amnt)
    #present_data()
def process_demand():
    demand_list=[]
    while True:
        item= input("item(type's' to stop):")
        if item=='s':
            break
        if item not in item_dict:
            print("Sorry! The mobile is not available.")
            continue
        amnt= int(input("Amount:"))
        if amnt>item_dict[item][0]:
            print (f"Total {item_dict[item][0]} pcs availabe!")
            continue
        dec_quant(item,amnt)
        demand_list+=[item,amnt,
                      item_dict[item][1],
                      amnt*item_dict[item][1]],
    print(53*"=")
    print("** Mobile Gedget Receipt**".center(53))
    print(53*"=")
    print("Mobile Name",(18-len("Mobile Name"))*" ",
            (4-len("Quantity"))*" ","Quantity",
            (9-len("Uprice"))*" ","Uprice",
            (9-len("Sub_Total"))*" ","Sub_Total")
    print(53*"_")
    tprice=0
    for x in demand_list:
      tprice+=x[3]
      print(x[0].title(),(20-len(x[0]))*" ",
            (6-len(str(x[1])))*" ",x[1],
            (6-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
            (8-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print(53*"_")
    tprice="%.2f"%tprice
    print("Total price: ",(36-len(str(tprice)))*" ",tprice)
    print(53*"_")
    #present_data()


while True:
    present_data()
    print("Choose an option: ")
    print("Type '1': To process Demand")
    print("Type '2': To manager Mobile database")
    print("Type '3': To exit the Program")
    choice=input("Choice: ")
    if choice =='1':
        process_demand()
    elif choice=='2':
        receive_order()
    elif choice=='3':
        break
    else:
        continue
f = open("E:\\mobileinfo.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write((str(item_dict[x][0]))+"\n")
    f.write((str(item_dict[x][1]))+"\n")
f.write("\n")
f.close()
