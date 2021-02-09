def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)
    start0 = [sticker[0], sticker[0], sticker[0]+sticker[2]] 
    start1 = [0, sticker[1], max(sticker[1],sticker[2])]
    for i in range(3, len(sticker)):
        start0.append(max(start0[i-2], start0[i-3]) + sticker[i])
        start1.append(max(start1[i-2], start1[i-3]) + sticker[i])
    return max(start0[-2], start0[-3], start1[-1], start1[-2])

print(solution([14, 6, 5, 11, 3, 9, 2, 10])) # 36
print(solution([1, 3, 2, 5, 4])) # 8