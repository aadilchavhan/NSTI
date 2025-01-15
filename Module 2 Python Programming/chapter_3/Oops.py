# # class ai:
# #     institute="NSTI"

# #     def __init__(self,name,age,address):
# #         self.name=name
# #         self.age= age
# #         self.address=address

# # Student=ai("Aadil",22,"M.H")

# # print(f'{Student.name},{Student.age},{Student.address}')

"""________________________________________________"""


# # class andriod:
# #     Xiomi="Redmi"

# #     def __init__(self,name,processor,storage):
# #         self.name= name
# #         self.processor= processor
# #         self.storage= storage


# # Mobile=andriod("REDMI_note_14_PRO","Snapdragan","8*256")

# # print(f'{Mobile.name},{Mobile.processor},{Mobile.storage}')

"""________________________________________________"""



# class Library:
#     a="Book"
#     b= "Dua"

#     def xyz(self):
#         print("Hello : " ,self.a)

#         print("Hello : " ,self.b)

#     def abc(self):
#         print("All The Books")

#     def add(self, a,b):
#         return a + b
    
#     def mod(self, a,b):
#         return a % b

# kitab=Library()

# print(kitab.a)
# print(kitab.b)
# #OR# print(f'{kitab.a},{kitab.b}')
# kitab.xyz()
# kitab.abc()

# print(kitab.add(13,10))
# print(kitab.mod(40,90))

"""________________________________________________"""


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class ShoppingCart:
#     def __init__(self):
#         self.cart = []

#     def add_item(self, product):
#         self.cart.append(product)
#         print(f'Added {product.name} to the cart.')

#     def remove_item(self, product_name):
#         for product in self.cart:
#             if product.name == product_name:
#                 self.cart.remove(product)
#                 print(f'Removed {product.name} from the cart.')
#                 break
#         else:
#             print(f'Product {product_name} not found in the cart.')

#     def display_cart(self):
#         if self.cart:
#             print("Cart contents:")
#             for product in self.cart:
#                 print(f'- {product.name}: {product.price}')
#         else:
#             print("Your cart is empty.")

#     def calculate_total_cost(self):
#         total = sum(product.price for product in self.cart)
#         print(f'Total cost: {total}')

# shopping_cart = ShoppingCart()

# # Creating products
# product1 = Product("Smartphone", 30000)
# product2 = Product("Laptop", 60000)
# product3 = Product("Headphones", 3000)

# # Adding items to the cart
# shopping_cart.add_item(product1)
# shopping_cart.add_item(product2)
# shopping_cart.add_item(product3)

# # Display cart contents
# shopping_cart.display_cart()

# # Removing an item from the cart
# shopping_cart.remove_item("Laptop")

# # Displaying the cart contents again
# shopping_cart.display_cart()

# # Calculating the total cost
# shopping_cart.calculate_total_cost()

"""________________________________________________"""



# class Wallet:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def add_money(self,money):
#         if money>0:
#             self.balance += money
#             print(f'Money added : {money} to {self.balance}')
#         else:
#             print("Enter a valid amount")

#     def spend(self,money):
#         if money> self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance -= money
#             print(f'Spent Amount {money} from  wallet . {self.name}\'s wallet. New balance: {self.balance}')

#     def check(self):
#         print(f'{self.name} balance is {self.balance}')

# x=Wallet("Aadil",5000)
# # y=Wallet("Saad",1000)

# x.add_money(5000)
# # y.add_money(100)

# x.spend(3000)
# # y.spend(1100)

# x.check()
# # y.check()


"""________________________________________________"""

# class flipkart:
#     def __init__(self,name):
#         self.name=name
#         self.item=[]


#     def add_item(self,i_name,price):
#         self.item.append({'name':i_name,'price':price })
#         print(f'Added {i_name} to list with price {price}')



#     def remove(self,i_name):
#         for item in self.item:
#             if item ['name']==i_name:
#                 self.item.remove(item)
#                 print(f'Removed {i_name}')
#                 return
#         print(f'{i_name} not found')


    
#     def display_c(self):
#         if self.item:
#             print("Cart for {self.name}")

#         for item in self.item:
#             print(f'{item['name']} : {item['price']}')
#         else:
#             print("Cart is empty")


# x=flipkart("Aadil")

# x.add_item("Laptop", 50000)

# x.display_c()

# x.remove("Laptop")




