function solution(n, lost, reserve) {
    var answer = 0;
    let newLost = lost.filter(l => reserve.includes(l)===false)
    let newReserve = reserve.filter(r => lost.includes(r)===false)
    lost = newLost
    reserve = newReserve
    for (let i = 1; i < n+1; i++) {
        if (lost.includes(i)) {
            if(reserve.includes(i-1)) {
                lost.splice(lost.indexOf(i),1)
                reserve.splice(reserve.indexOf(i-1),1)
                answer++
            } else if (reserve.includes(i+1)) {
                lost.splice(lost.indexOf(i),1)
                reserve.splice(reserve.indexOf(i+1),1)
                answer++
            }
        } else {
            answer++
        }
    }
    return answer;
}

/*
function solution(n, lost, reserve) {      
    return n - lost.filter(a => {
        const b = reserve.find(r => Math.abs(r-a) <= 1)
        if(!b) return true
        reserve = reserve.filter(r => r !== b)
    }).length
}
*/
console.log(solution(5, [2,4], [1,3,5]))
console.log(solution(5, [2,4], [3]))
console.log(solution(3, [3], [1]))