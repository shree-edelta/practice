dict = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M',2000:'MM',3000:'MMM'}

num = int(input("Enter a number: "))

if num <= 1 and num > 4000:
    print("Enter a number between 1 and 3000")
else:
    reverse_dict = sorted(dict, reverse=True)
    for i in reverse_dict:
        if num >= i:
            print(dict[i], end='')
            num -= i
    
    