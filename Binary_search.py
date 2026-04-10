# l1=[x for x in range(1,100001)]
# print(l1)
l1=[10,20,30,40,50,60,70]
key=int(input("key:"))
first=0
last=len(l1)-1
found=False
lc=0
while first<=last:
    mid=(first+last)//2
    
    if key<l1[mid]:
        last=mid-1
    elif key>l1[mid]:
        first=mid+1
    else:
        print(f"{key} is found at the index {mid}")
        found=True
        break
if not found:
    print(f"{key} is not found")
        