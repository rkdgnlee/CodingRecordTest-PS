function solution(x) {
    let str_x = x.toString();
    let sum = 0;
    for (let i=0 ; i < str_x.length ; i++) {
        sum += parseInt(str_x[i])
    }
    if (x % sum == 0 ) {
        return true;
    } else if (x % sum !== 0) {
        return false;
    }
}