function solution(answers) {
    var answer = [];
    const s1 = [1,2,3,4,5];
    const s2 = [2,1,2,3,2,4,2,5];
    const s3 = [3,3,1,1,2,2,4,4,5,5];
    
    const a1 = answers.filter((a,idx) => a == s1[idx%s1.length]).length;
    const a2 = answers.filter((a,idx) => a == s2[idx%s2.length]).length;
    const a3 = answers.filter((a,idx) => a == s3[idx%s3.length]).length;
    
    const maximum = Math.max(a1, a2, a3);
    
    if (maximum == a1) answer.push(1);
    if (maximum == a2) answer.push(2);
    if (maximum == a3) answer.push(3);
    return answer;
}

console.log(solution([1,2,3,4,5]))
console.log(solution([1,3,2,4,2]))