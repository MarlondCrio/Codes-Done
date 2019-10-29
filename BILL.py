kwh_used = 3000
if kwh_used <= 500:
    bill=kwh_used*.58

elif kwh_used > 500 and kwh_used <= 1500:
    bill=(kwh_used-500)*.75+500*.58

elif kwh_used > 1500 and kwh_used <= 2500:
    bill=(kwh_used-1500)*1.20+500*.58+1000*.75

else:
    bill=(kwh_used-2500)*2.0+ 500*.58 + 1000*.75+ 1000*1.2

print(bill*1.2)
    
