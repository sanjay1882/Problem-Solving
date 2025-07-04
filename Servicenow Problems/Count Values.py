# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
s1,s2,s3=list(s1),list(s2),list(s3)
st=[]
ind=0
s1ind=0
s2ind=0

while ind<len(s3):

    if s1ind<len(s1):
        st.append(s1[s1ind])
        if st[:]!=s3[:ind+1]:
            st.pop()
        else:
            s1ind+=1
            ind+=1
    if s2ind<len(s2):
        st.append(s2[s2ind])
        if st[:]!=s3[:ind+1]:

            st.pop()

        else:
            s2ind+=1
            ind+=1

print(st==s3)









