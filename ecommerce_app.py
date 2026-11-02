

# {"shopname": "tan", "category": "cloth", "products": [{"product": "vv", "price": "200"}, {"product": "vv", "price": "300"}]}*

import json
def calculateData(data1):
    data2=data1
    print('www',data2)
    WantedProduct= data2.get('products')
    chooseproduct=input('enter the product you wanna buy : ')
    print('tantan',WantedProduct)
    for chProduct in WantedProduct:
            if chProduct.get('product') == chooseproduct:
             print('your product is : ',chProduct.get('product'))
             quantity= int(input("enter your quantity : "))
             if quantity > chProduct.get("quatity"):
                  print(f"sorry your quantity of product is {quantity} ,but we have limited stock of {chProduct.get("quatity")}")
             else:
              cost=quantity*int(chProduct.get("price"))
              print("the total cost for the produt you gonna buy is this ", cost)
              payment=int(input("enter your paisa:"))
              if payment==cost:
                  print("your payment is sucessful,you can take your product")
              elif payment>cost:
                  extraMoney=payment-cost
                  print("your payment is sucessful and your left money is:",extraMoney)
              elif payment<cost:
                  print('your amount is insufficient')
            else:
                print("there isnot such product avaible: sorry")
             
def choices(choice):
                    
       if choice == 'open':
              products_list=[]
              while True:
               products_list=[]
               shope_name = input('enter your shope name : ')
               category_name= input('enter your category: ')
               while True:
                                      product_name= input('enter your product name : ')
                                      product_price= int(input('enter your product price : '))
                                      product_quntity= int(input('enter your product quantity : '))
                                      products_list.append({"product":product_name,"price": product_price,"quatity":product_quntity})
                                      addProduct= input('do you wanna add more product (yes/no)?').lower()
                                      if addProduct =="no":
                                       break
               shopList_dict_cred={"shopname":shope_name, "category": category_name, "products":products_list}                   
            #    print(shopeName)
               confrimation= input(' do you wanna add ths data to the file ? yes or no : ').lower()
               if confrimation == "yes":
                   with open ('shop.txt','a') as file:
                          shoplist= json.dumps(shopList_dict_cred)
                          file.write(
                f"{shoplist}\n" )
                          print(shoplist)
               else:
                  print("ok we got your product. thankyou")
               addEcomShop=input("do you wanna add new shop? (yes/no) ? ").lower()
               if addEcomShop=='no' :
                    print("ok we gt your shops name")
                    break   
                   
            
       else:        
             site_name = input('enter which shop you wanna visit ?: ')
             display = False
             found = False

             with open('shop.txt', 'r') as file:
              while True:
                for ecomshop in file:
                 if ecomshop != "":
                   dict_sholist = json.loads(ecomshop)

                   if dict_sholist.get('shopname')== site_name:
                    found = True
                    data_to_calculate= dict_sholist
                    print("finally , shop")
                    print('kkk',data_to_calculate)
                    calculate=calculateData(data_to_calculate)
                    print('cc',calculate)   
                   else:
                        print("that shop isnot avaible")
                break
              
                
# ////// from this it will run ....
while True:
    choice = input('Enter 1 to open an ecommerce shop, 2 to visit the ecommerce shop : ' )
    match choice:
        case '1':
            choices('open')
        case '2':
            choices('visit')
            break
        case _:
            print('Data is invalid')          

           

       
        
    
