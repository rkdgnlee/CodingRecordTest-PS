function solution(s){
    let pcount = 0;
    let ycount = 0;
    for (let i = 0 ; i < s.length ; i++) {
        if (s[i] == "p" || s[i] == "P") {
            pcount += 1;
        } else if (s[i] == "y" || s[i] == "Y") {
            ycount += 1;
        }
    }   
    if (pcount == ycount) {
        return true;
    } else {
        return false;
    }
} 