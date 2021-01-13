function solution(clothes) {
    var answer = 1;
    const dict = {}
    for (let i=0; i<clothes.length; i++) {
        let c = clothes[i][0]
        let k = clothes[i][1]
        if (k in dict) {
            dict[k] += 1
        } else {
            dict[k] = 1
        }
    }
    for (let key in dict) {
        answer *= dict[key] + 1
    }
    return answer-1;
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))