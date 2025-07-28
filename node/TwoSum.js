function checksum(target, array){
    let visitedNums = new Map()

    for (let i=0; i < array.length; i++){
        let complement = target - array[i]
        if(visitedNums.has(complement)){
            return [visitedNums.get(complement), i];
        }
        visitedNums.set(array[i], i)
    }
}

let returned = checksum(9, [2, 7, 11, 15])
console.log("Returned: ", returned)