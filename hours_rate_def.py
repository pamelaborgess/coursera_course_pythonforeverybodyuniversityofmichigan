def computepay(h, r):
    if h <= 40:
        p = h*r
    else:
        p = (h-40)*r*1.5 + 40*r
    
    return p

hrs = input("Enter Hours:")
rate = input("Enter the rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay:", p)

