const solution = (data) => {
    let zeroArray = [];
    let consArray = [];

    data.forEach(element => {
        if(element === 0){
            zeroArray.push(element);
        }else{
            consArray.push(element)
        }
    });
    const res1 = [...zeroArray,...consArray];
    // const res2 =  zeroArray.concat(consArray);
    console.log(res1);
    // return res;
}

let input = [1,10,-1,11,5,0,-7,0,25,-35]

solution(input)

//merge two arrays
/**
 *  method 1: const newArray = [...oldArr1,...oldArr2];
 *  method 2 : const new Array = oldArr1.concat(oldArr2);
 */