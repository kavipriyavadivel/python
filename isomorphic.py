def isIsomorphic(s, t):
        freq1 = [0] * 200
        freq2 = [0] * 200
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            if freq1[ord(s[i])] != freq2[ord(t[i])]:
                return False
            freq1[ord(s[i])] = i+1
            freq2[ord(t[i])] = i+1
        return True

s=input()
t=input()
print(isIsomorphic(s,t))