/* 
x*y = brown + yellow 와 2(x+y) = brown + 4
두 식의 근의 공식
*/

function solution(brown, yellow) {
    var answer = [];
    const x = ((2+brown/2) + Math.sqrt(Math.pow(2+brown/2, 2) - 4*(brown + yellow))) / 2
    const y = ((2+brown/2) - Math.sqrt(Math.pow(2+brown/2, 2) - 4*(brown + yellow))) / 2
    
    if (x > y) {
        answer.push(x);
        answer.push(y);
    } else {
        answer.push(y);
        answer.push(x);
    }
    return answer;
}

console.log(solution(10, 2))
console.log(solution(8,1))
console.log(solution(24, 24))