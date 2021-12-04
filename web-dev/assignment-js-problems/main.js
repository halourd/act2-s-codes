console.log("1.Write a loop that makes seven calls to console.log to output the following triangle. \nCode:")

const printTri = function(){
    var str1 = ""
    for(let x = 0; x < 7; x++){
        str1 += "#";
        console.log(str1)
    }
}
console.log(printTri())


console.log("2. Write a program that uses console.log to print all the numbers from 1 to 100, with two exceptions. For numbers divisible by 3, print \"X\" instead of the number, and for numbers divisible by 5 (and not 3), print \"0\" instead. Tip: Use % operator. \nCode:")

const printNum = function(){
    var nums = "";
    for(let i = 1; i <= 100; i++){
        nums = i;
        if(i % 3 == 0){
            nums = "X";
        }
        else if(i%5==0 && i%3!=0){
            nums = "0";
        }
        console.log(nums)
    }
}

console.log(printNum())