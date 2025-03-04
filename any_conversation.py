import re
dict = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M',2000:'MM',3000:'MMM'}

reverse_dict = sorted(dict, reverse=True)
num = input("Enter convertion number or roman number: ")

if num.isdigit():
    num = int(num)
   
    if num <= 1 and num > 10000:
        print("Enter a number between 1 and 10000")
    else:
        for i in reverse_dict:
            if num >= i:
                roman = dict[i]
                print(roman, end='')
                num -= i     
elif num.isalpha():
    
    num = num.upper()
    total = 0
    is_roman = bool(re.search("^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",num))
 
    if is_roman:
        for i in range(len(num)):
            for  k,v in dict.items():
                if v==num[i]:
                    if i+1<len(num) and num[i]<num[i+1]:
                        total -= k
                    elif i+1<len(num) and num[i]>num[i+1]:
                        total += k
                    else:
                        total += k
        print(total)
    else:
        print("Invalid roman number.")
else:
    print("enter a valid number or roman number.")