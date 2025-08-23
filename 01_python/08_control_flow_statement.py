# conditional statemnet 
# <, >, <=, >=, ==, !=




if 5 > 2:
    print("5 is greater than 2")
elif 5 == 5:  # ye condition tab use kerty ha ager first condition false ho jaye
    # aur hum chahte hain ke koi dosri condition check ho jaye or ager tb bi ye false ho jaye to else block execute ho jaye
    # elif ka matlab hota hai "else if"
    print("5 is equal to 5")
else:
    print("5 is not greater than 2")




# for loop
for i in range(5):  # ye loop 0 se lekar 4 tak chale ga
    print(i)  # ye print kare ga 0,1,2,3,4
    # 2nd example
    menu=["Biryani", "Karahi", "Nihari", "Korma"]
for item in menu:
    print(item)



# while loop
i=2
while i < 5:  # ye loop tab tak chale ga jab tak i ki value 5 se choti hai
    print(i)  # ye print kare ga 2,3,4
    i=i+1  # ye i ki value ko 1 se barha de ga
    



# break statement
for i in range(10):
    if i == 5:  # jab i ki value 5 ho jaye to loop break ho jaye ga
        break
    print(i)  # ye print kare ga 0,1,2,3,4

# continue statement
for i in range(10):
    if i == 5:  # jab i ki value 5 ho jaye to loop continue ho jaye ga
        continue  # ye i ki value ko skip kare ga
    print(i)  # ye print kare ga 0,1,2,3,4,6,7,8,9
# pass statement
for i in range(10):
    if i == 5:  # jab i ki value 5 ho jaye to loop pass ho jaye ga
        pass  # ye i ki value ko skip nahi kare ga, lekin koi action nahi lega
    print(i)  # ye print kare ga 0,1,2,3,4,5,6,7,8,9


    