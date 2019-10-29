toppings = ['bacon','bacon', 'anchovies' ]    ##List of toppings
size = 'large'                  ##Size of pizza
base_cost= 0
count=0                         ##Number of toppings
if size == 'small':
    base_cost = 14
    
elif size == 'medium':
     base_cost = 16

else:
    size == 'large'
    base_cost = 18
    
if 'bacon' or 'anchovies' in toppings:
    final_price = base_cost + 5

for elements in toppings:
    count = count + 1

final_price = final_price + .1 * base_cost * count
print (final_price)
