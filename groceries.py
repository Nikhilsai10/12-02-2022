Chicken=200
Eggs=10
Softdrinks=100
Snacks=100
Chocolates=200
cname=input('Enter the customer name: ')
cnum=input('Enter customer phone number: ')
cp=int(input('Enter the quantity of chicken in Kgs: '))
ep=int(input('Enter the number of eggs: '))
sp=int(input('Enter the number of softdrinks: '))
snp=int(input('Enter the number of snacks: '))
chp=int(input('Enter the number of chocolates: '))
bill=(Chicken*cp)+(Eggs*ep)+(Softdrinks*sp)+(Snacks*snp)+(Chocolates*chp)
Total= print("TOTAL BILL:",bill,)
if bill>=5000:
     discount=bill*10/100
     tax=0
     print("DISCOUNT RECEIVED:",discount,)
elif bill>=3000:
     discount=bill*8/100
     tax=0
     print("DISCOUNT RECEIVED:",discount,)
elif bill>=2000:
     discount=bill*5/100
     print("DISCOUNT RECEIVED:",discount,)
elif bill>=1000:
     discount=bill*3/100
     print("DISCOUNT RECEIVED:",discount,)    
elif bill>=3000:
     discount=bill*10/100
     print("DISCOUNT RECEIVED:",discount,)
else:
     print("Invalid Amount")
     

print("AMOUNT TO BE PAID BY THE CUSTOMER:",bill-discount)
