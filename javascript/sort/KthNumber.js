function solution(array, commands) {
    return commands.map(command => {
        const [sIndex, eIndex, index] = command
        const newArray = array.filter((value, fIndex) => sIndex-1<=fIndex && fIndex <= eIndex-1).sort((a,b)=>a-b)
        return newArray[index-1]
    })
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))