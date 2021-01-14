function solution(jobs) {
    var answer = 0;
    let now = 0;
    let last = -1;
    let count = 0;
    const N = jobs.length
    let heap = [];
    while (count < N) {
        for (let i = 0; i < N; i++) {
            if (last < jobs[i][0] && jobs[i][0] <= now) {
                heap.push([jobs[i][1], jobs[i][0]])
            }
        }
        if (heap.length > 0) {
            heap.sort((a,b) => a[0]-b[0])
            // console.log(heap)
            let job = heap.shift()
            last = now
            now += job[0]
            answer += (now - job[1])
            count += 1
        } else {
            now += 1
        }
    }
    return Math.floor(answer/N);
}

console.log(solution([[0, 3], [1, 9], [2, 6]]))
console.log(solution([[0, 3], [1, 9], [2, 6], [4, 3]]))
console.log(solution([[0, 1], [0, 1], [0, 1]]))
console.log(solution([[100, 100], [1000, 1000]]))
console.log(solution([[10, 10], [30, 10], [50, 2], [51, 2]]))
console.log(solution([[0, 1], [0, 1], [1, 0]]))
console.log(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))