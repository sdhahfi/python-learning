i=input("请输入数字,输入q后结束")
sum=0
j=0
while i!='q':
    sum+=int(i)
    j+=1
    i=input("请输入数字,输入q后结束")

if j==0:
    average=0
    print("没有输入数字")
    
else:
    average=sum/j
    print(sum)
    print(average)