arr=[-2,-1,0,4,7,-1,2,1,-5,-7]
Max=0
curr=0
ar=[]
ma=[]
for i in arr:
    curr=curr+i
    ar.append(i)
    
    if curr < 0:
        curr=0
        ar.clear()
    if curr >Max:
        Max=curr
        ma=ar.copy()
print(Max)
print(ma)


    #    int[] arr={2,1,2,3,8,9};
    #    int s=0;
    #    int e=arr.length;
    #    int k=3;
    #    int t=0;
    #    while (s<e){
    #       if(s==k){
    #           t+=1;
    #           s=t;
    #           k+=1;
    #           System.out.println();
    #       }
    #         System.out.print(arr[s]+" ");
    #       s+=1;
       
    

    