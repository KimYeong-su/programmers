function solution(numbers) {
    var answer = '';
    var newArray = numbers.map(x => ({
        origin : String(x),
        change : String(x)+String(x)+String(x)
    }));
    newArray.sort((a,b) => {
        if(a.change < b.change) return 1;
        if(a.change > b.change) return -1;
        if(a.change === b.change) return 0;
    })
    for (let i =0 ; i < newArray.length; i++) {
        answer += newArray[i].origin
    }
    if (Number(answer)) {
        return answer
    } else {
        return "0"
    }
}

console.log(solution([6, 10, 2]))
console.log(solution([3, 30, 34, 5, 9]))