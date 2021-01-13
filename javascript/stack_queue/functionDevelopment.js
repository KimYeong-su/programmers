function solution(progresses, speeds) {
    var answer = [];
    const time = [];
    for (let i=0; i < progresses.length; i++) {
        let day = Math.ceil((100 - progresses[i]) / speeds[i])
        time.push(day)
    }
    let maximum = 0;
    for (let i=0; i < progresses.length; i++){
        if (time[i] > maximum) {
            maximum = time[i]
            answer.push(1)
        } else {
            answer[answer.length-1] += 1
        }
        
    }
    return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]))
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))