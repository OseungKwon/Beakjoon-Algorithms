n=int(input())
num=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
Min=1e+9
Max=-1e+9

def find(i,result,add,sub,mul,div):
    global Max,Min
    if i==n:
        Max=max(result,Max)
        Min=min(result,Min)
        return
    else:
        if add:
            find(i+1,result+num[i],add-1,sub,mul,div)
        if sub:
            find(i+1,result-num[i],add,sub-1,mul,div)
        if mul:
            find(i+1,result*num[i],add,sub,mul-1,div)
        if div:
            find(i+1,int(result/num[i]),add,sub,mul,div-1)

find(1,num[0],add,sub,mul,div)
print(Max)
print(Min)
            
