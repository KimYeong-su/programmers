def solution(n):
    global answer
    answer = 0
    cols = [0] * (n+1)
    
    def promissing(level):
        for i in range(1,level):
            if cols[i]==cols[level] or (level-i) == abs(cols[level]-cols[i]): return False
        return True
    
    def queen(level):
        global answer                      
        if level == n:                
            answer += 1                 
            return
        for i in range(1,n+1):
            cols[level+1] = i 
            if promissing(level+1):
                queen(level+1)          
        return
    queen(0)
    return answer

print(solution(4))