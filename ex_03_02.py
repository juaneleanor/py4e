hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
if hrs > 40:
    pay = 40 * rate
    overtime = hrs - 40
    rate *= 1.5
    pay += overtime * rate
else:
    pay = hrs * rate
    
print(pay)