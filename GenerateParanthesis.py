def Generate(open,close,n):


    if open==close==n:
        out.append("".join(st))
        return
    if open<n:
        st.append('(')
        Generate(open+1,close,n)
        st.pop()
    if open>close:
        st.append(')')
        Generate(open,close+1,n)
        st.pop()

n=2
st = []
out = []
Generate(0,0,n)
print(out)
