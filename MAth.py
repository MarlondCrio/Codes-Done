interest_rate= .06
inital_value= 100
years=0
new_value= 100
count=0
if interest_rate > 0 and interest_rate < 1:
    new_value= inital_value
    while new_value < 2*inital_value: 
        years = years + 1
        new_value =new_value + new_value * interest_rate
    print (years)
elif interest_rate == 0 :
    print ('None')

else:
    print (1)
