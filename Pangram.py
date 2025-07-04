def pangram(sentence):
    letters=set("abcdefghijklmnopqrstuvwxyz")
    sentence= sentence.lower()
    return letters.issubset(set(sentence))



if __name__ =="__main__":
    sen="The quick brown fox jumps over the lazy dog abcdefghijklmnopqrstuvwxyz"
   
    # if pangram(sen):
    #     print("1",end='\t')
    # else:
    #     print("0",end='\t')
    #

    if len(set(sen))==26:
        print("pangram")
    else:
        print("Not")


        