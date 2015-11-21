j = 3
k = 7
s = [8, 6, 7, 5, 3, 0, 9]
for n in range(10):
    for i in range(len(s)):
        if i is 0:
            out = (s[j-1] + s[k-1]) % 10 # the pseudorandom output
        elif 0 < i < 6:
            s[i] = s[i+1] # shift the array
        else:
            s[i] = out
            print(s[i]) # print the result
