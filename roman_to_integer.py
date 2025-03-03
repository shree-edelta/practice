roman_dict = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'L':50,'C':100,'D':500,'M':1000}

roman = input("Enter a roman number: ")
total = 0
for i in range(len(roman)):
    try:
        if roman[i] in roman_dict:
            if i+1<len(roman) and roman_dict[roman[i]]<roman_dict[roman[i+1]]:
                total -= roman_dict[roman[i]]
            else:
                total += roman_dict[roman[i]]
        else: 
            print("Invalid roman number.")
            break
    except:
        print("Invalid roman number.")
print(total)