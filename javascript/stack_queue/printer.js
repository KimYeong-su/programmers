function solution(priorities, location) {
    var answer = 0;
    let queue = [];
    let qIndex = []
    let p;
    let idx;
    let maximum = Math.max(...priorities)
    for (let i=0; i < priorities.length; i++) {
        queue.push(priorities[i])
        qIndex.push(i)
    }
    while (queue) {
        p = queue.shift()
        idx = qIndex.shift()
        if (maximum == p) {
            answer += 1
            if (idx == location) {
                return answer
            }
            maximum = Math.max(...queue)
        } else {
            queue.push(p)
            qIndex.push(idx)
        }
    }
}

console.log(solution([2, 1, 3, 2], 2))
console.log(solution([1, 1, 9, 1, 1, 1], 0))