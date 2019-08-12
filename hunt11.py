def rev(Sentence): 
    return ' '.join(word[::-1] for word in S.split(" ")) 
S = input()
print(rev(S)) 
