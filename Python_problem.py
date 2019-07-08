input_string=input()
ans=set(input_string) #Here it will remove the duplicate characters
length=0;
for i in range(0,len(ans)):
    length=length+1;
print(length)
