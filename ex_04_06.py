def computepay(h, r):

    if h > 40:
        pay = 40 * r
        rate = r * 1.5
        overtime = h - 40
        pay += overtime * rate
    else:
        pay = h * r
    
    return pay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)

print("Pay", p)