s=input()
d={"(":")"}
st=[]
def funct(s):
    for i in s:
        if i in d.keys():
            st.append(i)
        else:
            if not st:
                return False
            else:
                if i ==d[st[-1]]: 
                    st.pop()
    if st==[]:
        return True
    else:
        return False
        
        

print(funct(s))
