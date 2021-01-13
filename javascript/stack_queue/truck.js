function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridgeWeight = 0;
    let index = 0;
    let time = []
    let w = []
    while (index < truck_weights.length) {
        answer += 1
        if (answer - time[0] === bridge_length) {
            bridgeWeight -= w[0]
            time.shift()
            w.shift()
        }
        if (bridgeWeight + truck_weights[index] <= weight) {
            bridgeWeight += truck_weights[index]
            w.push(truck_weights[index])
            time.push(answer)
            index += 1
        }
    }
    return answer + bridge_length;
}

console.log(solution(2, 10, [7,4,5,6]))
console.log(solution(100, 100, [10]))
console.log(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))