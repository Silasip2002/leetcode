const missingNumber = (array,n) => {
     for(let i = 0 ; i < n ; i ++){
         if(array.indexOf(i+1) === -1){
             return (i+1);
         }
     }
}


let array = [6,1,2,8,3,4,7,10,5];
let n = 10;

console.log(missingNumber(array,n));