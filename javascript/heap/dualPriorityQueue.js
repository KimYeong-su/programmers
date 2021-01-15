function solution(operations) {
    let tmp = [];
    operations.forEach(t => {
        if (t[0] === 'I') {
            tmp.push(+(t.split(" ")[1]));
        } else {
            if (!tmp.length) return;
            
            let num = (t[2] === '-' ? Math.min : Math.max)(...tmp);
            let delIndex = tmp.findIndex(t => t === num);
            
            tmp.splice(delIndex, 1);
        }
    })
    return tmp.length ? [Math.max(...tmp), Math.min(...tmp)] : [0, 0];
}

console.log(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
console.log(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))