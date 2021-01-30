def solution(n):
    def hanoi(n, from_pos, to_pos, aux_pos, move):
        if n == 1:
            move.append([from_pos, to_pos])
        else:
            hanoi(n-1, from_pos, aux_pos, to_pos, move)
            move.append([from_pos, to_pos])
            hanoi(n-1, aux_pos, to_pos, from_pos, move)
        
    answer = []    
    hanoi(n, 1, 3, 2, answer)
    return answer

print(solution(2)) # [[1,2], [1,3], [2,3]]