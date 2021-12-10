hrs = input("Enter Hours:")
rate = input("Enter the rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, write a number')

if h <= 40:
    p = h*r
    print('pay:', p)
else:
    p = (h-40)*1.5*r+(40*r)
    print('pay:', p)
    