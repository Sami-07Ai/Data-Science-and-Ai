# nested for loops
colors = ["red", "green", "blue"]
fruits = ["apple", "banana", "cherry"]
for color in colors:
    for fruit in fruits: # lop ke andar loop
        print(color, fruit)  # ye hum revers ma bi print kar sakty hain
        # print(fruit, color)  # ye bhi chale ga, lekin order change ho jaye ga
# This will print each combination of color and fruit
# Output:
# red apple   
# red banana
# red cherry    
# green apple
# green banana
# green cherry
# blue apple
# blue banana
# blue cherry



# nested while loops
i = 0
while i < 3:  # outer loop
    j = 0
    while j < 2:  # inner loop
        print(i, j)  # ye print kare ga i aur j ki value
        j += 1  # inner loop ki value ko barha de ga
    i += 1  # outer loop ki value ko barha de ga