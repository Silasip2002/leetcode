/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


 var twoSum = function(nums, target) {
    const dic = new Map();
    let result = [];
    
    nums.forEach((num,index) => {
        if(dic.get(num) != undefined){
            result.push (dic.get(num))
            result.push (index);
        }else{
            const reminder = target - num;
            dic.set(reminder,index);
        }
    })
    console.log(result);
}; 

const nums = [2,7,11,15]
const target = 9

twoSum(nums,target);
