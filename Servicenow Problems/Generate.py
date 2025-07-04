def generate(arr,tar,ind,curr):
    if curr==tar:
        out.append(st[:])
        return
    if curr>tar:
        return

    for i in range(ind,len(arr)):
        st.append(arr[i])
        generate(arr,tar,i,curr+arr[i])
        st.pop()




a=[1,2,3,4]
t=4
out=[]
st=[]
generate(a,t,0,0)
print(out)