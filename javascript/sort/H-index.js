function solution(citations) {
    citations.sort((a,b) => b-a)
    let i = 0;
    while (i+1 <= citations[i]) {
        i++
    }
    return i
}
/* 너무 비효율적인 나의 코드...
function solution(citations) {
    const N = citations.length;
    let quotation
    citations.sort((a,b) => b-a)
    for (let h = 10000; h > -1; h--) {
        quotation = 0;
        citations.forEach(c => {
            if (c >= h) {
                quotation += 1
            }
        });
        if (h <= quotation && h >= N-quotation){
            return h
        }
    }
}
*/
console.log(solution([3, 0, 6, 1, 5]))
console.log(solution([4, 4, 4]))