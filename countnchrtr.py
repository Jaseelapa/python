def Countchar(inputString):
    Count={}
    for char in inputString:
        if char in count:
            count[char] +=1
        else:
            Count[char]=1
    return count
str2=input("Enter a string:")
result=countChar(str2)
print(result)
