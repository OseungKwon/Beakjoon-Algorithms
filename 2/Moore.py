def Shift(pat): # shift table
    NUM = 27
    M = len(pat)
    skip = [M for i in range(NUM)]
    for i in range(M):
        skip[ord(pat[i]) - ord('A')] = M - i - 1 # 아스키 값을 변환
    return skip

def Moore(pat, txt):
    M = len(pat)
    N = len(txt)
    skip = Shift(pat)
    i = M-1
    j = M-1

    while j >= 0:
        while txt[i] != pat[j]:
            k = skip[ord(txt[i]) - ord('A')]
            if M - j > k:
                i = i + M - j
                print(M,j,k,i,txt[i])
            else:
                i = i + k

            if i >= N:
                return 'not exist'
            j = M - 1
        i = i-1
        j = j-1
    return i+1
print(Shift("ACITON"))
print(Moore("ATION","VISOINQUESTIONONIONCAPTIONGRADUATION"))
print(list(range(3)))