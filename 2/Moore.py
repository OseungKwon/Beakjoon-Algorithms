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
    print(M,N)
    i = M-1
    j = M-1

    while j >= 0:
        while txt[i] != pat[j]:
            k = skip[ord(txt[i]) - ord('A')]
            print('1->',txt[i],j,k)
            if M - j > k:
                i = i + M - j
            else:
                i = i + k

            if i >= N:
                return 'not exist'
            j = M - 1
            print('2->',txt[i],j,k,end="\n\n")
        i = i-1
        j = j-1
        print('----')
    return i+1

print(Moore("ATION","VISOINQUESTIONONIONCAPTIONGRADUATION"))